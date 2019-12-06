PROBA = 'src/proba.py'
STAT  = 'src/stat.py'

default : stat

proba :
	python $(RPOBA)

stat :
	python $(STAT)
