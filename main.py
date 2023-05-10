from flask import Flask, render_template, request
app = Flask(__name__)

products = [
    {
        "name": "Air Jordan 4 Retro PSG",
        "image": "img/jordan-retro-4.jpg",
        "description": "Las Air Jordan 4 Retro PSG son las zapatillas que empezaron todo en 1985. La versión actual conserva el diseño icónico de alta calidad de las originales y añade características modernas para una mayor comodidad y durabilidad.",
        "price": "200€"
},
{
"name": "Air Jordan 1 Mid",
"image": "img/air-jordan-mid.jpg",
"description": "Las Air Jordan 1 Mid están confeccionadas con materiales de alta calidad y ofrecen una comodidad excepcional. Estas zapatillas son perfectas para el uso diario y para cualquier ocasión.",
"price": "110€"
},
{
"name": "Air Jordan 1 Mid",
"image": "img/air-jordan-mid.jpg",
"description": "Las Air Jordan 1 Mid están confeccionadas con materiales de alta calidad y ofrecen una comodidad excepcional. Estas zapatillas son perfectas para el uso diario y para cualquier ocasión.",
"price": "110€"
}
]
@app.route("/")
def index():
    return render_template('index.html', products=products)

@app.route('/air-jordan-1')
def air_jordan_1():
    return render_template('air_jordan_1.html')

@app.route('/air-jordan-mid')
def air_jordan_mid():
    return render_template('air_jordan_mid.html')

if __name__ == '__main__':
    app.run(debug=True)