from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'You\'ve reached a Blank Page!'

@app.route('/play')
def index():
    return render_template("index.html", number = 3, color = 'lightskyblue')

@app.route('/play/<int:number>')
def box_multiplier(number):
    return render_template("index.html", number = number, color = 'lightskyblue')

@app.route('/play/<int:number>/<string:color>')
def box_multiplier_with_color(number, color):
    return render_template("index.html", number = number, color = color)

if __name__=="__main__":
    app.run(debug=True)