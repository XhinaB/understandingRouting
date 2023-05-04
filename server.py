from flask import Flask, render_template

app = Flask (__name__)

@app.route('/repeat/<phrase>/<int:nr>')
def index(phrase, nr):
    return render_template('index.html',phrase=phrase, times=nr)

@app.route('/say/<name>')
def sayMyName(name):
    return "My name is" + name



if __name__=="__main__":
    app.run(debug=True)
