from models import model1, model2, badmodel

def ReadModelFormat_BIS(modelname, goodmodel=None):
	print(modelname['B'])
	print(modelname['I'])
	print(modelname['S'])

ReadModelFormat_BIS(model1)
ReadModelFormat_BIS(model2)
ReadModelFormat_BIS(badmodel)