import warnings

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

warnings.filterwarnings('ignore')


def dataSetClassifier():
    ESR = pd.read_csv('venv/input/Epileptic Seizure Recognition.csv')
    ESR = ESR.drop(columns=ESR.columns[0])
    ESR.head()

    cols = ESR.columns
    tgt = ESR.y
    tgt[tgt > 1] = 0
    ax = sn.countplot(tgt, label="Count")
    non_seizure, seizure = tgt.value_counts()
    print('The number of trials for the non-seizure class is:', non_seizure)
    print('The number of trials for the seizure class is:', seizure)

    ESR.isnull().sum().sum()

    ESR.describe()

    Y = ESR.iloc[:, 178].values

    Y[Y > 1] = 0

    X = ESR.iloc[:, 1:178].values

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    clf = SVC()
    clf.fit(X_train, y_train)
    y_pred_svc = clf.predict(X_test)
    acc_svc = round(clf.score(X_train, y_train) * 100, 2)
    print("Accuracy is:", (str(acc_svc) + '%'))
    return clf
