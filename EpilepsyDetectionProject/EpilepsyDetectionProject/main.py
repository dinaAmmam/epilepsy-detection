from API.epilepsyAPI import app

import SeizureMatchingUtils

# GoodPatientData.csv
# PatientData.csv
import Utils

# matchResult = SeizureMatchingUtils.checkPatientData('venv/input/GoodPatientData.csv')

# if matchResult:
#  print('"yes" you might get seizure be conscious about it')
# else:
# print('You are safe no worries :)')
if __name__ == '__main__':
    app.run()

# Utils.convertJSONoCSV();
# Utils.convertCSVtoJSON();
