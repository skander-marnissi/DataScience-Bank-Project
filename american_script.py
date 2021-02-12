# Author: Skander Marnissi 

import pandas as pd
import numpy as np 
import pickle

from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler, OneHotEncoder, LabelBinarizer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from forms import AmericanRegistrationForm, LoginForm

def Americandata_process() :
    print("______________________")
    print("im in Americandata_process method ")

    form = AmericanRegistrationForm()

    if form.validate_on_submit():

        clage=form.clage.data
        debtinc=form.debtinc.data
        reason = dict(form.reason.choices).get(form.reason.data)
        job= dict(form.job.choices).get(form.job.data)
        delinq= int(dict(form.delinq.choices).get(form.delinq.data))
        derog= int(dict(form.derog.choices).get(form.derog.data))

        # Test Data:
        # Ces données sont remplies statiquement, il fause juste remplacer les 6 variables avec les données récupérées à
        # partir du formulaire
        
        data = [[clage, debtinc, reason, job, delinq, derog]]
        columns = ["CLAGE", "DEBTINC", "REASON", "JOB", "DELINQ", "DEROG"]
        input_data = pd.DataFrame(data, columns=columns)

        american = pd.read_csv("./dataset/Bank_of_America_data.csv")
        with_median = make_pipeline(
            SimpleImputer(missing_values=np.nan, strategy='mean')
        )
        median_vars = ["LOAN", "MORTDUE", "VALUE", "DEBTINC", "CLAGE"]
        american[median_vars] = with_median.fit_transform(american[median_vars])

        # Converting Discrete columns to type object
        discrete_columns = ["REASON", "JOB", "DEROG", "DELINQ", "NINQ", "CLNO", "YOJ"]
        american[discrete_columns] = american[discrete_columns].astype(object)
        most_frequent = make_pipeline(
            SimpleImputer(missing_values=np.nan, strategy='most_frequent')
        )
        most_frquent_value_vars = discrete_columns
        american[discrete_columns] = most_frequent.fit_transform(american[discrete_columns])

        y = american["BAD"]
        X = american.copy()
        X = X[["CLAGE", "DEBTINC", "REASON", "JOB", "DELINQ", "DEROG"]]

        total = input_data.append(X)
        total = pd.get_dummies(total)
        obj_a_predire = total.iloc[0]
        total.drop(total.index[0])
        X = pd.get_dummies(X)

        clf = RandomForestClassifier(n_estimators=6)
        clf.fit(X,y)

        pickle.dump(clf, open('./models/american_model.pkl', 'wb'))
        loaded_model = pickle.load(open('./models/american_model.pkl','rb'))
        classe = loaded_model.predict([obj_a_predire])
        
        print("_________________________________________________________ Result :")
        print(classe[0])

        return(classe[0])
    
    return(-1)    
