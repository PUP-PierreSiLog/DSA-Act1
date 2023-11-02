from flask import Flask, render_template, request
from computations import Circle
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contact')
def contact():
    return "Contact Page. please create me an html page with dummy contact info"

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfcircle():
    area=None
    if request.method == 'POST':
        input_radius=request.form.get('InputFloat', '')
        input_radius=int(input_radius)
        circle_calculations=Circle(input_radius)
        area=circle_calculations.calculate_area()
    return render_template('areaOfcircle.html', area=area)
 
if __name__ == "__main__":
    app.run(debug=True)
