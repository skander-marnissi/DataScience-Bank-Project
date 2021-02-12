# Author: Skander Marnissi 

from flask import Flask, render_template, url_for, flash, redirect, session
from forms import GermanRegistrationForm, LoginForm, AmericanRegistrationForm, TaiwanRegistrationForm
from german_script import Germandata_process
from american_script import Americandata_process
from taiwan_script import Taiwandata_process

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018',
        'image_png':'german/d_german1.png'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018',
        'image_png':'german/d_german2.png'
    }
]
results = [
    {
        
        'title': 'Its a good client',
        
        'image_png':'german/good.png'
    },
    {
        'title': 'Its a bad client',

        'image_png':'german/bad.png'
    }
]

users = {
    "german": {
        "username": "german",
        "password": "german"
    },
    "american": {
        "username": "american",
        "password": "american"
        
    },
    "taiwan": {
        "username": "taiwan",
        "password": "taiwan"
    }
}


@app.route("/")
@app.route("/home")
def home():
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user = users[username]
        return render_template("home.html", user=user)
    else:
        print("No username found in session")
        return redirect(url_for("login"))


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if not session.get("USERNAME") is None:

            username = session.get("USERNAME")
            user = users[username]
            
            if user["username"] =="german":
                form = GermanRegistrationForm()
                if form.validate_on_submit():
                    score = Germandata_process()
                    
                    if score==1:
                        print("Good client")
                        return render_template('result.html', title='Result', result=results[0])
                    elif score==0:
                        print("Bad client")
                        return render_template('result.html', title='Result', result=results[1])
                    else:
                        print("ERROR")
                else:
                    return render_template('register_german.html', title='Register', form=form, user=user)


            elif user["username"] =="american":

                print("______________________")
                print("im in Amercian username ")

                form = AmericanRegistrationForm()

                if form.validate_on_submit():
                    
                    print("______________________")
                    print("im in Amercian submited ")
                    
                    score = Americandata_process()
                    
                    if score==1:
                        print("Good client")
                        return render_template('result.html', title='Result', result=results[0])
                    elif score==0:
                        print("Bad client")
                        return render_template('result.html', title='Result', result=results[1])
                    else:
                        print("ERROR")
                else:
                    return render_template('register_american.html', title='Register', form=form, user=user)

            else:
               
                print("______________________")
                print("im in Taiwan username ")

                form = TaiwanRegistrationForm()

                if form.validate_on_submit():
                    
                    print("______________________")
                    print("im in Taiwan submited ")
                    
                    score = Taiwandata_process()
                    
                    if score==1:
                        print("Good client")
                        return render_template('result.html', title='Result', result=results[0])
                    elif score==0:
                        print("Bad client")
                        return render_template('result.html', title='Result', result=results[1])
                    else:
                        print("ERROR")
                else:

                    return render_template('register_taiwan.html', title='Register', form=form, user=user)
  
          
    


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    username = form.email.data
    password = form.password.data

    if form.validate_on_submit():
    
        if not username in users:
            print("Username not found")
            return redirect(url_for("login"))
        else:
            user = users[username]

        if not password == user["password"]:
            print("Incorrect password")
            return redirect(url_for("login"))
        else:
            session["USERNAME"] = user["username"]
            print("session username set")
            return redirect(url_for("home"))

    return render_template('login.html', title='Login', form=form)
    
@app.route("/sign_out")
def sign_out():

    session.pop("USERNAME", None)

    return redirect(url_for("login")) 


if __name__ == '__main__':
    app.run(debug=True)
