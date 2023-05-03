from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/air-jordan-1')
def air_jordan_1():
    return render_template('air_jordan_1.html')

@app.route('/air-jordan-mid')
def air_jordan_mid():
    return render_template('air_jordan_mid.html')

if __name__ == '__main__':
    app.run(debug=True)