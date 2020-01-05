def Q567(plot=False, Q5=True, Q6=True, Q7=True):
    def model1(a0, a1, Sk):
        return a0 + a1*Sk

    def model2(b0, b1, Sk):
        return b0 + b1*Sk*Sk

    def lstqerr(model, points, *modelargs):
        err = 0
        for k in range(len(points[0])):
            x = points[0][k]
            err += (model(*modelargs, x) - points[1][k])**2
        return err

    df = readCPU2()
    MatrixSizes    = np.asarray(df[('MatrixSize',)])
    OperatingTimes = np.asarray(df[('OperatingTime',)])
    n1 = n2 = len(MatrixSizes)
    model1regr = linregress(MatrixSizes,    y=OperatingTimes)
    model1regr_SEE = lstqerr(model1, [MatrixSizes, OperatingTimes], *(model1regr.intercept, model1regr.slope))
    model2regr = linregress(MatrixSizes**2, y=OperatingTimes)
    model2regr_SEE = lstqerr(model2, [MatrixSizes, OperatingTimes], *(model2regr.intercept, model2regr.slope))
    model1regr_normal = (OperatingTimes - model1regr.intercept - model1regr.slope*MatrixSizes)
    model2regr_normal = (OperatingTimes - model2regr.intercept - model2regr.slope*MatrixSizes*MatrixSizes)

    if Q5:

        print('Model 1: Correlation coefficient: %.2f, least square err (SSE): %.2f, std: %.2f'%(model1regr.rvalue, model1regr_SEE, np.std(model1regr_normal)))
        print('Model 2: Correlation coefficient: %.2f, least square err (SSE):  %.2f, std:  %.2f\n'%(model2regr.rvalue, model2regr_SEE, np.std(model2regr_normal)))

        # F-test
        F = np.var(model1regr_normal)/np.var(model2regr_normal)
        print("F-value for the test: F = %.2f\n"%(F))

    Sk2, Z = 1E6, 1.96
    MatrixSizesSquared = np.power(MatrixSizes, 2)       # Sk^2
    s_mean = np.mean(MatrixSizesSquared)                # S^2 mean
    sxx = np.sum(np.power(MatrixSizesSquared-s_mean, 2))# sum((Sk^2-S^2)^2)
    S = np.sqrt(model2regr_SEE/(n2-2))                  # sqrt(SEE/(n-2))
    X_mean = model2regr.intercept + model2regr.slope * Sk2 # B0 + B1*Sk^2
    sqr = Z * S * np.sqrt(1+ (1/n2)+ (Sk2 - X_mean)/sxx)
    CIL, CIU = X_mean - sqr, X_mean + sqr
    if Q6 : print("95%% level confience interval : [%.2f, %.2f]\n"%(CIL, CIU))

    if Q7:
        norm = np.random.normal(scale=np.std(model2regr_normal),size=1000)
        X_mean = model2regr.intercept + model2regr.slope * 1E6 # B0 + B1*Sk^2
        distribution = X_mean + norm
        within = np.sum(np.logical_and(distribution>=CIL, distribution<=CIU))
        outside = 1000-within
        frac = within/1000



    if plot:
        height = 0
        if Q5 or Q6 : height+=1
        if Q7 : height+=1
        width = 1
        if Q5 and Q6 : width += 1
        plt.Figure()
        grid = plt.GridSpec(height, width, wspace=0.4, hspace=0.3)
        if Q5:
            plt.subplot(grid[0, 0])
            plt.title('Regression on operating times as a function of matrix sizes.')
            plt.xlabel('Matrix size')
            plt.ylabel('Operating time [sec]')
            matrix_ranger = np.linspace(np.min(MatrixSizes), np.max(MatrixSizes), 200)
            plt.scatter(MatrixSizes, OperatingTimes, color=blue)
            plt.plot(matrix_ranger, model1(model1regr.intercept, model1regr.slope, matrix_ranger), purple, label='Model 1 : $X_k = a_0+a_1 S_k$')
            plt.plot(matrix_ranger, model2(model2regr.intercept, model2regr.slope, matrix_ranger), orange, label='Model 2: $X_k = b_0+b_1 S_k^2$')
            plt.legend()
        if Q6:
            plt.subplot(grid[0, width-1])
            plt.title('The normal distribution for each model.')
            plt.xlabel('Matrix size')
            plt.ylabel('Operating time [sec]')
            plt.scatter(MatrixSizes, model1regr_normal, color=purple, label='Model 1 : $X_k = a_0+a_1 S_k$')
            plt.scatter(MatrixSizes, model2regr_normal, color=orange, label='Model 2: $X_k = b_0+b_1 S_k^2$')
            plt.legend()
        if Q7:
            plt.subplot(grid[height-1, :])
            plt.title('Verification for the 95% level confidence interval.')
            plt.xlabel('Operating time [sec]')
            plt.ylabel('')
            plt.axvline(CIU, color=blue, label='Lower/Upper bound')
            plt.axvline(CIL, color=blue)
            ranger = np.linspace(np.min(distribution)-1, np.max(distribution)+1, 200)
            kde = gaussian_kde(distribution)
            y = kde(ranger)
            ymax, ymin = np.max(y), np.min(y)
            plt.plot(ranger, y, color=orange, label='pdf from points cloud')
            plt.scatter(distribution, [ymax - 1.15*(ymax-ymin)]*len(distribution), color=purple, label='Normal distribution (%.2f %% between bounds)'%(100*frac))
            plt.legend()
        plt.show()

    return None
