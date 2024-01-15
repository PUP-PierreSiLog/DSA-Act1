from flask import Flask, render_template, request
from computations import Circle, Triangle
from HashFunction import HashTable

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
        if input_radius.isdigit():
            input_radius=int(input_radius)
            circle_calculations=Circle(input_radius)
            area=circle_calculations.calculate_area()
        else:
            area="Please input a valid integer."
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
        else:
            area="Please input a valid integer."
    return render_template('areaOfTriangle.html', area=area)

hash_table=HashTable(32)
@app.route('/HashFunction', methods=['GET', 'POST'])
def HashFunction():
    hash_option = None
    hash_result = None
    hash_function = None
    data_input = None

    if request.method == 'POST':
        hash_option = request.form.get('HashOptions')
        print(f"Received hash_option: {hash_option}")
        integer_select = int(request.form['IntegerSelect'])
        data_input = request.form['DataInput']

        print(f"Received integer_select: {integer_select}")
        print(f"Received data_input: {data_input}")

        # Validate hash option
        valid_options = ['Option1', 'Option2', 'Option3']
        if hash_option not in valid_options:
            return "Invalid hash option"

        # Choose the appropriate hash function based on the selected option
        if hash_option == 'Option1':
            hash_function = hash_table.hash_function_1
        elif hash_option == 'Option2':
            hash_function = hash_table.hash_function_2
        elif hash_option == 'Option3':
            hash_function = hash_table.hash_function_3
        else:
            return "Invalid hash option"

        # Insert or delete data based on the number of integers specified
        if integer_select == 1:
            # Assuming "del " prefix for deletion
            if data_input.startswith("del "):
                word_to_delete = data_input[4:]
                hash_table.delete(word_to_delete)
            else:
                hash_table.insert(data_input, hash_function)

            # Calculate hash result
        key = sum(ord(char) for char in data_input)
        hash_result = hash_function(key)
        print(f"Calculated key: {key}, hash_result: {hash_result}")

        # Display the updated hash table
        hash_table.display()

        # Pass the updated hash_result to the template
        return render_template('HashFunction.html', hash_option=hash_option, hash_result=hash_result)
if __name__ == "__main__":
    app.run(debug=True)
