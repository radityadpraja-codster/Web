from flask import Flask, render_template, url_for
import random
import os

print(os.getcwd())

app = Flask(__name__)

# Home/1st page
@app.route("/")
def pertama():
    # <a> anchor tag with its attribute
    return "<h1>Hello, World!</h1><br><p>Nice to see you</p><p>please check</p><a href='/random_fact'>View a random fact!</a><br><a href='/modern_fact'>View a modern fact!</a><br><a href='/random_image'>View a random image!</a><br>"
    
# 2nd page
@app.route("/random_fact")

def kedua():
    txt_name = random.choice(os.listdir("fact_list"))
    # formatted string
    with open(f'fact_list/{txt_name}', 'r') as f:
        document = f.read()
    return f'{document}'
# 2nd page
@app.route('/modern_fact')
def index():
    return render_template('dasar.html')#folder templates

@app.route("/random_image")
def random_image():
    images = [
        "img/dice.jpg",
        "img/mappa.jpg",
        "img/parrott.jpg",
        "img/wit.png"
    ]
    img_url = url_for("static", filename=random.choice(images))
    return f'<h1>Random Image</h1><img src="{img_url}" width="300">'

app.run(debug=True)

