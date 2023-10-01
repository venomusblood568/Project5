from flask import Flask, jsonify

app = Flask(__name__)

# Home page
@app.route('/', methods=['GET'])
def home():
    welcome_message = "Welcome to the Calculator API!"
    instructions = """
    To perform calculations, use the following endpoints:<br>
    1. For addition: /add/int(a)/int(b)<br>
    2. For subtraction: /sub/int(a)/int(b)<br>
    3. For multiplication: /multiply/int(a)/int(b)<br>
    4. For division: /divide/int(a)/int(b)<br>
    5. For square: /square/int(a)<br>
    6. For cube: /cube/int(a)<br>
    """
    return f"{welcome_message}<br><br>{instructions}"
# square root calculation
@app.route('/square/<int:a>', methods=['GET'])
def square(a):
    result = a ** 2
    return f'The square of {a} is: {result}'

# cube root calculation
@app.route('/cube/<int:a>', methods=['GET'])
def cube(a):
    result = a ** 3
    return f'The cube of {a} is: {result}'

# addition calcultion
@app.route('/add/<int:a>/<int:b>',methods =['GET'])
def add(a,b):
    result = a + b
    return f'The sum of {a} and {b} is:{result}'

# subtraction calculation 
@app.route('/sub/<int:a>/<int:b>',methods=['GET'])
def sub(a,b):
    result = a - b
    return f'The subtarction of {a} and {b} is:{result}'

# multiply calculation 
@app.route('/multiply/<int:a>/<int:b>',methods= ['GET'])
def multiply(a,b):
    result = a * b
    return f'The multiplication of {a} and {b} is: {result}'

# divide calculation
@app.route('/divide/<int:a>/<int:b>',methods = ['GET'])
def divide(a,b):
    if b != 0:
        result = a / b
        return f'The division of {a} and {b} is: {result}'
    else:
        return 'Error: Division by zero is not allowed.'

if __name__ == "__main__":
    app.run(debug=True ,port=5001)
