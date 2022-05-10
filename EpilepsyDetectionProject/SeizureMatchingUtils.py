import pandas as pd
import DatasetProcessor


def checkPatientData(dataFilePath):
    clf = DatasetProcessor.dataSetClassifier()
    ESR = pd.read_csv(dataFilePath)
    ESR = ESR.drop(columns=ESR.columns[0])
    ESR.head()
    new_input1 = [ESR.iloc[0, :177]]
    new_output = clf.predict(new_input1)

    if new_output == [1]:

        return True
    else:

        return False
