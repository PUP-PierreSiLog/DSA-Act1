from flask import Flask, render_template, request
from computations import Circle, Triangle

app = Flask(__name__, static_url_path='', static_folder='D:/CMPE201_DSA/Flask_Intro/Flask_Intro/static')

@app.route('/')
def index():
    return render_template('profile.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ToUppercase', methods=['GET', 'POST'])
def ToUppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works')
def works():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfcircle():
    area=None
    if request.method == 'POST':
        input_radius=request.form.get('InputFloat', '')
        input_radius=int(input_radius)
        circle_calculations=Circle(input_radius)
        area=circle_calculations.calculate_area()
    return render_template('areaOfcircle.html', area=area)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def areaOfTriangle():
    area=None
    if request.method == 'POST':
        input_base=request.form.get('InputFloat1', '')
        input_height=request.form.get('InputFloat2','')
        #Checks if the base and height are integers
        if input_height.isdigit() and input_base.isdigit():
            input_base=int(input_base)
            input_height=int(input_height)
            triangle_calculations=Triangle(input_base, input_height)
            area=triangle_calculations.calculate_area()
    return render_template('areaOfTriangle.html', area=area)
 
if __name__ == "__main__":
    app.run(debug=True)
