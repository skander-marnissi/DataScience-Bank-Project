# Author: Skander Marnissi 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from flask import Flask, render_template, url_for, flash, redirect
from forms import GermanRegistrationForm, LoginForm
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pickle
from sklearn.model_selection import train_test_split

def Germandata_process() :

    form = GermanRegistrationForm()

    if form.validate_on_submit():

        
        status=dict(form.status.choices).get(form.status.data)
        duration=form.duration.data
        credh=dict(form.credh.choices).get(form.credh.data)
        purpose=dict(form.purpose.choices).get(form.purpose.data)
        credit=form.credit.data
        saving=dict(form.saving.choices).get(form.saving.data)
        present=dict(form.present.choices).get(form.present.data)
        rate=form.rate.data
        personal=dict(form.personal.choices).get(form.personal.data)
        other=dict(form.other.choices).get(form.other.data)
        residence=form.residence.data
        proper=dict(form.proper.choices).get(form.proper.data)
        age=form.age.data
        otherInst=dict(form.otherInst.choices).get(form.otherInst.data)
        housing=dict(form.housing.choices).get(form.housing.data)
        nbrcredit=form.nbrcredit.data
        job=dict(form.job.choices).get(form.job.data)
        nbrperson=form.nbrperson.data
        telephone=dict(form.telephone.choices).get(form.telephone.data)
        foreign=dict(form.foreign.choices).get(form.foreign.data)

        
        
        lst=[status,duration,credh,purpose,credit,saving,present,rate,personal,other,residence,proper,age,otherInst,housing,nbrcredit,job,nbrperson,telephone,foreign]

        headers = ["Status of existing checking account",
            "Duration in month","Credit history",
            "Purpose",
            "Credit amount",
            "Savings account/bonds",
            "Present employment since",
            "Installment rate in percentage of disposable income",
            "Personal status and sex",
            "Other debtors / guarantors",
            "Present residence since",
            "Property",
            "Age in years",
            "Other installment plans",
            "Housing",
            "Number of existing credits at this bank",
            "Job",
            "Number of people being liable to provide maintenance for",
            "Telephone",
            "foreign worker"]
        
        df=pd.DataFrame([lst],columns =headers)

        bigdf=pd.read_csv("./dataset/german.data", sep=" ", header=None)

        bigdf.drop(bigdf.columns[len(bigdf.columns)-1], axis=1, inplace=True)

        bigdf.columns=headers

        Status_of_existing_checking_account = {"A11" : "... <    0 DM",
                                       "A12" : "0 <= ... <  200 DM",
                                       "A13" : "... >= 200 DM / salary assignments for at least 1 year",
                                       "A14" : "no checking account"}
        df["Status of existing checking account"] = df["Status of existing checking account"].map(Status_of_existing_checking_account)
        bigdf["Status of existing checking account"]=bigdf["Status of existing checking account"].map(Status_of_existing_checking_account)

        Credit_history={"A30" : "no credits taken / all credits paid back duly",
                        "A31" : "all credits at this bank paid back duly",
                        "A32" : "existing credits paid back duly till now",
                        "A33" : "delay in paying off in the past",
                        "A34" : "critical account / other credits existing (not at this bank)"}
        df["Credit history"] = df["Credit history"].map(Credit_history)
        bigdf["Credit history"]=bigdf["Credit history"].map(Credit_history)

        Purpose={"A40" : "car (new)",
                "A41" : "car (used)",
                "A42" : "furniture/equipment",
                "A43" :"radio/television",
                "A44" : "domestic appliances",
                "A45" : "repairs",
                "A46" : "education",
                "A47" : "(vacation - does not exist?)",
                "A48" : "retraining",
                "A49" : "business",
                "A410" : "others"}
        df["Purpose"]=df["Purpose"].map(Purpose)
        bigdf["Purpose"]=bigdf["Purpose"].map(Purpose)

        Savings_account_bonds={"A61" : "... <  100 DM",
                            "A62" : "100 <= ... <  500 DM",
                            "A63" : "500 <= ... < 1000 DM",
                            "A64" : ".. >= 1000 DM",
                            "A65" : "unknown/ no savings account"}
        df["Savings account/bonds"]=df["Savings account/bonds"].map(Savings_account_bonds)
        bigdf["Savings account/bonds"]=bigdf["Savings account/bonds"].map(Savings_account_bonds)

        Present_employment_since={"A71" : "unemployed",
                                "A72" : "... < 1 year",
                                "A73" : "1  <= ... < 4 years",
                                "A74" : "4  <= ... < 7 years",
                                "A75" : ".. >= 7 years"}
        df["Present employment since"]=df["Present employment since"].map(Present_employment_since)
        bigdf["Present employment since"]=bigdf["Present employment since"].map(Present_employment_since)

        Personal_status_and_sex={"A91" : "male:divorced/separated",
                                "A92" : "female:divorced/separated/married",
                                "A93" : "male:single",
                                "A94" : "male:married/widowed",
                                "A95" : "female:single"}
        df["Personal status and sex"]=df["Personal status and sex"].map(Personal_status_and_sex)
        bigdf["Personal status and sex"]=bigdf["Personal status and sex"].map(Personal_status_and_sex)

        Other_debtors_guarantors={"A101" : "none",
                                "A102" : "co-applicant",
                                "A103" : "guarantor"}
        df["Other debtors / guarantors"]=df["Other debtors / guarantors"].map(Other_debtors_guarantors)
        bigdf["Other debtors / guarantors"]=bigdf["Other debtors / guarantors"].map(Other_debtors_guarantors)
   


        Property={"A121" : "real estate",
                "A122" : "building society savings agreement / life insurance",
                "A123" : "car or other",
                "A124" : "unknown / no property"}
        df["Property"]=df["Property"].map(Property)
        bigdf["Property"]=bigdf["Property"].map(Property)

        Other_installment_plans={"A141" : "bank",
                                "A142" : "stores",
                                "A143" : "none"}
        df["Other installment plans"]=df["Other installment plans"].map(Other_installment_plans)
        bigdf["Other installment plans"]=bigdf["Other installment plans"].map(Other_installment_plans)

        Housing={"A151" : "rent",
                "A152" : "own",
                "A153" : "for free"}
        df["Housing"]=df["Housing"].map(Housing)
        bigdf["Housing"]=bigdf["Housing"].map(Housing)

        Job={"A171" : "unemployed/ unskilled  - non-resident",
            "A172" : "unskilled - resident",
            "A173" : "skilled employee / official",
            "A174" : "management/ self-employed/highly qualified employee/ officer"}
        df["Job"]=df["Job"].map(Job)
        bigdf["Job"]=bigdf["Job"].map(Job)

        Telephone={"A191" : "none",
                "A192" : "yes, registered under the customers name"}
        df["Telephone"]=df["Telephone"].map(Telephone)
        bigdf["Telephone"]=bigdf["Telephone"].map(Telephone)

        foreign_worker={"A201" : "yes",
                        "A202" : "no"}
        df["foreign worker"]=df["foreign worker"].map(foreign_worker)
        bigdf["foreign worker"]=bigdf["foreign worker"].map(foreign_worker)

        df = df.append(bigdf)

        print("--------------bigDF")
        print(bigdf.head())
        
        print("--------------Df complete")
        print(df.head())

      
        
        # On crée une liste qui contient les variables quantitatives seulement
        var_num = ["Duration in month",
                "Credit amount",
                "Installment rate in percentage of disposable income",
                "Present residence since",
                "Age in years",
                "Number of existing credits at this bank",
                "Number of people being liable to provide maintenance for"]  

        # On récupére les données des variables quantitatives
        data_num = df[var_num]

        # On centre et on réduit les données
        data_num_scaled = StandardScaler().fit_transform(df[var_num])
        data_num_scaled = pd.DataFrame(data_num_scaled, columns = var_num)

        
        """
        status_list=["... <    0 DM","... <    0 DM","... <    0 DM","0 <= ... <  200 DM","... >= 200 DM / salary assignments for at least 1 year","no checking account","... <    0 DM","... <    0 DM","... <    0 DM","... <    0 DM","... <    0 DM","... <    0 DM","... <    0 DM"]
        credit_list=["no credits taken / all credits paid back duly","no credits taken / all credits paid back duly","no credits taken / all credits paid back duly","all credits at this bank paid back duly","existing credits paid back duly till now","delay in paying off in the past","critical account / other credits existing (not at this bank)","delay in paying off in the past","delay in paying off in the past","delay in paying off in the past","delay in paying off in the past","delay in paying off in the past","delay in paying off in the past"]
        pupose_list=["car (new)","car (new)","car (new)","car (used)","furniture/equipment","radio/television","domestic appliances","repairs","education","(vacation - does not exist?)","retraining","business","others"]
        saving_list=["... <  100 DM","... <  100 DM","... <  100 DM","100 <= ... <  500 DM","500 <= ... < 1000 DM",".. >= 1000 DM", "unknown/ no savings account","... <  100 DM","... <  100 DM","... <  100 DM","... <  100 DM","... <  100 DM","... <  100 DM"]
        present_list=["unemployed","unemployed","unemployed", "... < 1 year","1  <= ... < 4 years","4  <= ... < 7 years",".. >= 7 years","unemployed","unemployed","unemployed","unemployed","unemployed","unemployed"]
        personal_list=["male:divorced/separated","male:divorced/separated","male:divorced/separated","female:divorced/separated/married","male:single","male:married/widowed","female:single","female:single","female:single","female:single","female:single","female:single","female:single"]
        other_list=["none","none","none","co-applicant","guarantor","none","none","none","none","none","none","none","none"]
        proper_list=["real estate","real estate","real estate","building society savings agreement / life insurance","car or other","unknown / no property","real estate","real estate","real estate","real estate","real estate","real estate","real estate"]
        otherInst_list=["bank","bank","bank","stores","none","bank","bank","bank","bank","bank","bank","bank","bank"]
        housing_list=["rent","rent","rent","own","for free","own","own","own","own","own","own","own","own"]
        job_list=["unemployed/ unskilled  - non-resident","unemployed/ unskilled  - non-resident","unemployed/ unskilled  - non-resident","unskilled - resident","skilled employee / official", "management/ self-employed/highly qualified employee/ officer","unemployed/ unskilled  - non-resident","unemployed/ unskilled  - non-resident","unemployed/ unskilled  - non-resident","unemployed/ unskilled  - non-resident","unemployed/ unskilled  - non-resident","unemployed/ unskilled  - non-resident","unemployed/ unskilled  - non-resident"]
        telephone_list=["none","none","none","yes", "registered under the customers name","none","none","none","none","none","none","none","none"]
        foreign_list=["yes","yes","yes","no","yes","yes","yes","yes","yes","yes","yes","yes","yes"]
        """

        # On crée une liste qui contient les variables qualitatives seulement
        var_quali = ["Status of existing checking account",
                    "Credit history",
                    "Purpose",
                    "Savings account/bonds",
                    "Present employment since",
                    "Personal status and sex",
                    "Other debtors / guarantors",
                    "Property",
                    "Other installment plans",
                    "Housing",
                    "Job",
                    "Telephone",
                    "foreign worker"]


                            
        # On transforme la table des données en un tableau disjonctif complet
  
        dummy_var_quali = pd.get_dummies(df[var_quali]) 
        
        print("----------------- dummy_var_quali ---------")
        print(len(dummy_var_quali.columns))

    
        # Unification des deux transformatin      
        data = pd.concat([data_num, dummy_var_quali], axis = 1)

        print(data.columns)
        
        #Proceder au modele
        loaded_model = pickle.load(open('./models/germanModel.sav', 'rb'))
        X=data.values
        print("Data[0] : ")
        print(data.loc[[0]])    
        print("X[0] : ")
        print(X[0])
        l0=X[0]
        predict=loaded_model.predict(l0.reshape(1,-1)) # Clasteur 0 Bad , 1 Good

        print(predict[0])

        return(predict[0])

    return(-1)