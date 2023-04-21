from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def login():
    if(request.method == "POST"):
        email = request.form.get('fEmail')
        password = request.form.get('fPassword')
        print(email, password)
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template("register.html")
    
if __name__ == "__main__":
    app.run(debug=True)