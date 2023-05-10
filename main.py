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
"name": "Jordan 5 Retro Off-White",
"image": "img/jordan-retro-5.jpg",
"description": "Este lanzamiento rinde homenaje a los primeros Jordan que Virgil tuvo, los Air Jordan 5. De una manera tradicional, Virgil rediseñó esta silueta clásica subrayando la importancia de la tecnología Nike Air.Estos Jordan 5 están confeccionados con un upper de malla Sail con paneles de red translúcidos e inserciones por todo el sneaker.",
"price": "110€"
},
{
"name": "Air Jordan 1 Low",
"image": "img/jordan-low.jpg",
"description": "Las Air Jordan 1 Mid están confeccionadas con materiales de alta calidad y ofrecen una comodidad excepcional. Estas zapatillas son perfectas para el uso diario y para cualquier ocasión.",
"price": "180€"
},
]
@app.route("/")
def index():
    return render_template('index.html', products=products)

@app.route('/air-jordan-1')
def jordan_4():
    return render_template('air_jordan_1.html')

@app.route('/air-jordan-mid')
def air_jordan_1():
    return render_template('air_jordan_mid.html')

@app.route('/jordan_5_offwhite')
def jordan_5_offwhite():
    return render_template('jordan_5_offwhite.html')
@app.route('/jordan_1_low')
def jordan_1_low():
    return render_template('jordan_1_low.html')
@app.route('/cuidados_nike_air_jordan')
def cuidados_nike_air_jordan():
    return render_template('cuidados_nike_air_jordan.html')

if __name__ == '__main__':
    app.run(debug=True)