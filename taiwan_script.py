# Author: Skander Marnissi 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from flask import Flask, render_template, url_for, flash, redirect
from forms import TaiwanRegistrationForm, LoginForm
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

import pickle
from sklearn.model_selection import train_test_split

def Taiwandata_process() :

    form = TaiwanRegistrationForm()

    if form.validate_on_submit():
        print(dict(form.sex.choices).get(form.sex.data))
        limit_bal=int(form.limit_bal.data)
        sex=int(dict(form.sex.choices).get(form.sex.data))
        education=int(dict(form.education.choices).get(form.education.data))
        marriage=int(dict(form.marriage.choices).get(form.marriage.data))
        age=int(form.age.data)
        
        pay_1=int(dict(form.pay_1.choices).get(form.pay_1.data))
        pay_2=int(dict(form.pay_2.choices).get(form.pay_2.data))
        pay_3=int(dict(form.pay_3.choices).get(form.pay_3.data))
        pay_4=int(dict(form.pay_4.choices).get(form.pay_4.data))
        pay_5=int(dict(form.pay_5.choices).get(form.pay_5.data))
        pay_6=int(dict(form.pay_6.choices).get(form.pay_6.data))

        bill_amt1=int(form.bill_amt1.data)
        bill_amt2=int(form.bill_amt2.data)
        bill_amt3=int(form.bill_amt3.data)
        bill_amt4=int(form.bill_amt4.data)
        bill_amt5=int(form.bill_amt5.data)
        bill_amt6=int(form.bill_amt6.data)
        
        pay_amt1=int(form.pay_amt1.data)
        pay_amt2=int(form.pay_amt2.data)
        pay_amt3=int(form.pay_amt3.data)
        pay_amt4=int(form.pay_amt4.data)
        pay_amt5=int(form.pay_amt5.data)
        pay_amt6=int(form.pay_amt6.data)
        
        
        
        lst=[-1,limit_bal,sex,education,marriage,age,pay_1,pay_2,pay_3,pay_4,pay_5,pay_6,bill_amt1,bill_amt2,bill_amt3,bill_amt4,bill_amt5,bill_amt6,pay_amt1,pay_amt2,pay_amt3,pay_amt4,pay_amt5,pay_amt6]

        headers = ["ID",
            "LIMIT_BAL",
            "SEX",
            "EDUCATION",
            "MARRIAGE",
            "AGE",
            "PAY_1",
            "PAY_2",
            "PAY_3",
            "PAY_4",
            "PAY_5",
            "PAY_6",
            "BILL_AMT1",
            "BILL_AMT2",
            "BILL_AMT3",
            "BILL_AMT4",
            "BILL_AMT5",
            "BILL_AMT6",
            "PAY_AMT1",
            "PAY_AMT2",
            "PAY_AMT3",
            "PAY_AMT4",
            "PAY_AMT5",
            "PAY_AMT6",
            ]
        
        df=pd.DataFrame([lst],columns =headers)

        bigdf=pd.read_excel("./dataset/default-of-credit-card-clients.xls", header=1)

        bigdf.drop(bigdf.columns[len(bigdf.columns)-1], axis=1, inplace=True)

        bigdf.columns = headers

        df = df.append(bigdf)

        print("--------------bigDF")
        print(bigdf.head())
        
        print("--------------Df complete")
        print(df.head())

        df.drop(columns = ["AGE", "EDUCATION", "MARRIAGE", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6"], inplace  = True)
        df = df.replace({'PAY_1' : -2,
                              'PAY_2' : -2,
                              'PAY_3' : -2,
                              'PAY_4' : -2,
                              'PAY_5' : -2,
                              'PAY_6' : -2}, np.NaN)
        df.dropna(axis = 'index', inplace = True)
        cols = df.columns.to_list() 

        for col in ["SEX", "PAY_1", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6"]:
            cols.remove(col)

        scaler = StandardScaler()
        for i in cols:
            df[i] = scaler.fit_transform(df[i].values.reshape(-1, 1))


        #Proceder au modele
        print("__________________________________________")
        loaded_model = pickle.load(open('./models/taiwan_model.sav', 'rb'))
        print(loaded_model)
        X=df.values
        print("Data[0] : ")
        print(df.loc[[0]])    
        print("X[0] : ")
        print("************************************************")
        print(X[0])
        l0=X[0]
        predict=loaded_model.predict(l0.reshape(1,-1)) # Clasteur 0 Bad , 1 Good

        print(predict[0])

        return(predict[0])

    return(-1)