from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/introductory')
def introductory():
    return render_template('introductory.html')

@app.route('/advanced')
def advanced():
    return render_template('advanced.html')

@app.route('/project')
def project():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True)