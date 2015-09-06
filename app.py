from flask import Flask

from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    # return "Welcome!"
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp')
def signUp():
    # create user code will be here!!

if __name__ == "__main__":
    app.run()
