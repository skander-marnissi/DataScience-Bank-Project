# DataScience-Bank-Project

Three session website applications that uses machine learning models, developed with flask, flask_wtf and wtforms on python 3.6.


*Note: you can find the models under ./models directory*

## Installation
Open terminal and type the following commands: 

```bash
git clone https://github.com/SkanderMarnissi/DataScience-Bank-Project/
```
Then type 

```bash
cd DataScience-Bank-Project
pip install -r requirements.txt
```

## How it works?
Each session represents a different bank(American, German and Taiwanese),the purpose of this project is to predict if a given customer will be able to repay or not his bank loan and this will be done with the help of the developed and trained machine learning models(Since we have three banks and three different datasets, we trained three models to be able to predict with more accuracy.).


## Usage: 
In order to process the program and make it work you need to :

### Step 1: 
Run the flask server from the server.py folder

#### To run the server: 

In order to run your server you should open your terminal and enter: 

```bash

python server.py

```

### Step 2: 
Open your browser on the localhost URL and browse to /login.html page

#### To login: 

You have three different logins/password for each session respectively:

**American bank session: login="american"| password="american".**

**German bank session: login="german"| password="german".**

**Taiwanese bank session: login="taiwan"| password="taiwan".**

You will be redirected to the/home.html page of the country session

*Note: you can find a dashboard describing the data visualisation of the current data set of the country that you can find under .dataset/ directory.*


### Step 3: 
Now to predict if a given customer is able to repay or not his bank loan browse to the /register.html page and fill the given form

*Note: Each Bank session(American|German|Taiwan) has it's own form with different fields according to their dataset (That you can inspect under .dataset/ directory).*


### Step 4:
After processing you will obtain the result and be redirect the first time to the /result.html page you can then browse to the /home.html page.

*Note: you can find all the html pages under .templates/ directrory.*



*SKANDER MARNISSI COPYRIGHT © 2019 - ALL RIGHTS RESERVED*