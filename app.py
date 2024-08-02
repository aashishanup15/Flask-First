from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


def login_success(name, x):
    if x>=18: 
        return 'You can Vote'
    else:
        return 'You Cannot Vote'
    

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        age= int(request.form['age'])
        return login_success(name=user, x=age) 
        
if __name__ == '__main__':
    app.run()