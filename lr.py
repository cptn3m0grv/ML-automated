#!/usr/bin/env python

import pandas as pd

dataset = pd.read_csv('/root/titanic_train.csv')

gender = dataset['Sex']
age = dataset['Age']
dataset.isnull()

def lw(cols):
    age = cols[0]
    Pclass = cols[1]
    if pd.isnull(age):
        if Pclass == 1:
            return 38
        elif Pclass == 2:
            return 30
        elif Pclass == 3:
            return 25
        else:
            return 30
    else:
        return age

dataset['Age'] = dataset[['Age', 'Pclass']].apply(lw, axis = 1)
dataset.head(20)
dataset.drop('Cabin',
              axis = 1,
              inplace = True)

fare = dataset['Fare']
y = dataset['Survived']
sex = dataset['Sex']
sex = pd.get_dummies(sex, drop_first = True)
pclass = dataset['Pclass']
pclass = pd.get_dummies(pclass, drop_first = True)
sibsp = dataset['SibSp']
sibsp = pd.get_dummies(sibsp, drop_first = True)
parch = dataset['Parch']
parch = pd.get_dummies(parch, drop_first = True)
embarked = dataset['Embarked']
embarked = pd.get_dummies(embarked, drop_first = True)
X = dataset['Age']
X = pd.concat([X, embarked, parch, sibsp, pclass, sex], axis = 1)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

model.coef_
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
