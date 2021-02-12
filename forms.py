# Author: Skander Marnissi 

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class GermanRegistrationForm(FlaskForm):
    
    duration = IntegerField('Duration in month', validators=[DataRequired()])

    credit = IntegerField('Credit amount', validators=[DataRequired()])

    rate = IntegerField('Installment rate in percentage of disposable income', validators=[DataRequired()])
    
    residence = IntegerField('Present residence since', validators=[DataRequired()])

    age = IntegerField("Age in years",validators=[DataRequired()])

    nbrcredit= IntegerField("Number of existing credits at this bank",validators=[DataRequired()])

    nbrperson= IntegerField("Number of people being liable to provide maintenance for",validators=[DataRequired()])

    credh = SelectField('Credit history', choices=[('A30', 'A30'),('A31','A31'),('A32','A32'),('A33','A33'),('A34','A34')])

    status = SelectField('Status of existing checking account', choices=[('A11','A11'), ('A12','A12'),('A13','A13'),('A14','A14')])

    purpose = SelectField('Purpose', choices=[('A40','A40'),('A41','A41'),('A42','A42'),('A43','A43'),('A44','A44'),('A45','A45'),('A46','A46'),('A47','A47'),('A48','A48'),('A49','A49'),('A410','A410')])

    saving = SelectField('Savings account/bonds', choices=[('A61','A61'),('A62','A62'),('A63','A63'),('A64','A64'),('A65','A65')])

    present = SelectField('Present employment since', choices=[('A71','A71'),('A72','A72'),('A73','A73'),('A74','A74'),('A75','A75')])

    personal = SelectField('Personal status and sex', choices=[('A91','A91'),('A92','A92'),('A93','A93'),('A94','A94'),('A95','A95')])

    other = SelectField('Other debtors / guarantors', choices=[('A101','A101'),('A102','A102'),('A103','A103')])

    otherInst = SelectField('Other installment plans', choices=[('A141','A141'),('A142','A142'),('A143','A143')])

    proper = SelectField('Property', choices=[('A121','A121'),('A122','A122'),('A123','A123'),('A124','A124')])
    
    housing = SelectField('Housing', choices=[('A151','A151'),('A152','A152'),('A153','A153')])

    job = SelectField('Job', choices=[('A171','A171'),('A172','A172'),('A173','A173'),('A174','A174')])

    telephone = SelectField('Telephone', choices=[('A191','A191'),('A192','A192')])

    foreign=SelectField('foreign worker', choices=[('A201','A201'),('A202','A202')])

    """
    duration = IntegerField('Duration in month', validators=[DataRequired()])

    credit = IntegerField('Credit amount', validators=[DataRequired()])

    rate = IntegerField('Installment rate in percentage of disposable income', validators=[DataRequired()])
    
    residence = IntegerField('Present residence since', validators=[DataRequired()])

    age = IntegerField("Age in years",validators=[DataRequired()])

    nbrcredit= IntegerField("Number of existing credits at this bank",validators=[DataRequired()])

    nbrperson= IntegerField("Number of people being liable to provide maintenance for",validators=[DataRequired()])

    credh = SelectField('Credit history', choices=[('A30', 'no credits taken / all credits paid back duly'),('A31','all credits at this bank paid back duly'),('A32','existing credits paid back duly till now'),('A33','delay in paying off in the past'),('A34','critical account / other credits existing (not at this bank)')])

    status = SelectField('Status of existing checking account', choices=[('A11','... <    0 DM'), ('A12','0 <= ... <  200 DM'),('A13','... >= 200 DM / salary assignments for at least 1 year'),('A14','no checking account')])

    purpose = SelectField('Purpose', choices=[('A40','car (new)'),('A41','car (used)'),('A42','furniture/equipment'),('A43','radio/television'),('A44','domestic appliances'),('A45','repairs'),('A46','education'),('A47','(vacation - does not exist?)'),('A48','retraining'),('A49','business'),('A410','others')])

    saving = SelectField('Savings account/bonds', choices=[('A61','... <  100 DM'),('A62','100 <= ... <  500 DM'),('A63','500 <= ... < 1000 DM'),('A64','.. >= 1000 DM'),('A65','unknown/ no savings account')])

    present = SelectField('Present employment since', choices=[('A71','unemployed'),('A72','... < 1 year'),('A73','1  <= ... < 4 years'),('A74','4  <= ... < 7 years'),('A75','.. >= 7 years')])

    personal = SelectField('Personal status and sex', choices=[('A91','male:divorced/separated'),('A92','female:divorced/separated/married'),('A93','male:single'),('A94','male:married/widowed'),('A95','female:single')])

    other = SelectField('Other debtors / guarantors', choices=[('101','none'),('A102','co-applicant'),('A103','guarantor')])

    otherInst = SelectField('Other installment plans', choices=[('141','bank'),('142','stores'),('A143','none')])

    proper = SelectField('Property', choices=[('A121','real estate'),('A122','building society savings agreement / life insurance'),('A123','car or other'),('A124','unknown / no property')])
    
    housing = SelectField('Housing', choices=[('A151','rent'),('A152','own'),('A153','for free')])

    job = SelectField('Job', choices=[('A171','unemployed/ unskilled  - non-resident'),('A172','unskilled - resident'),('A173','skilled employee / official'),('A174','management/ self-employed/highly qualified employee/ officer')])

    telephone = SelectField('Telephone', choices=[('A191','none'),('A192','yes, registered under the customers name')])

    foreign=SelectField('foreign worker', choices=[('A201','yes'),('A202','no')])
    """



    submit = SubmitField('Process German !')


class AmericanRegistrationForm(FlaskForm):
    
    clage = IntegerField('CLAGE', validators=[DataRequired()])

    debtinc = IntegerField('DEBTINC', validators=[DataRequired()])

    reason = SelectField('Reason of the debt', choices=[('HomeImp', 'HomeImp'), ('DebtCon', 'DebtCon')])

    job=SelectField('Job of the client', choices = [
                    ('Other', 'Other'), ('Office', 'Office'), ('Sales', 'Sales'), ('Mgr', 'Mgr'), ('ProfExe', 'ProfExe'), ('Self', 'Self')])

    delinq=SelectField('Delinq', choices = [('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')])

    derog=SelectField('Derog', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')])

    submit=SubmitField('Process  American !')

class TaiwanRegistrationForm(FlaskForm):
    limit_bal = IntegerField('Credit amount', validators=[DataRequired()])

    sex = SelectField('Gender', choices = [('1', '1'), ('2', '2')])

    education = SelectField('Education', choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])
    
    marriage = SelectField('Marriage', choices = [('1', '1'), ('2', '2'), ('3', '3')])

    age = IntegerField("Age in years",validators=[DataRequired()])

    pay_1 = SelectField("PAY 1", choices = [('-1', '-1'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')])
    pay_2 = SelectField("PAY 2", choices = [('-1', '-1'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')])
    pay_3 = SelectField("PAY 3", choices = [('-1', '-1'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')])
    pay_4 = SelectField("PAY 4", choices = [('-1', '-1'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')])
    pay_5 = SelectField("PAY 5", choices = [('-1', '-1'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')])
    pay_6 = SelectField("PAY 6", choices = [('-1', '-1'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')])

    bill_amt1 = IntegerField("Amount of bill statement 1", validators=[DataRequired()])
    bill_amt2 = IntegerField("Amount of bill statement 2", validators=[DataRequired()])
    bill_amt3 = IntegerField("Amount of bill statement 3", validators=[DataRequired()])
    bill_amt4 = IntegerField("Amount of bill statement 4", validators=[DataRequired()])
    bill_amt5 = IntegerField("Amount of bill statement 5", validators=[DataRequired()])
    bill_amt6 = IntegerField("Amount of bill statement 6", validators=[DataRequired()])

    pay_amt1 = IntegerField("Amount of previous payment 1",validators=[DataRequired()])
    pay_amt2 = IntegerField("Amount of previous payment 2",validators=[DataRequired()])
    pay_amt3 = IntegerField("Amount of previous payment 3",validators=[DataRequired()])
    pay_amt4 = IntegerField("Amount of previous payment 4",validators=[DataRequired()])
    pay_amt5 = IntegerField("Amount of previous payment 5",validators=[DataRequired()])
    pay_amt6 = IntegerField("Amount of previous payment 6",validators=[DataRequired()])
    

    submit = SubmitField('Process Taiwan !')




  


class LoginForm(FlaskForm):
    email = StringField('Bank Name', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')