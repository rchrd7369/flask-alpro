from flask import Flask, render_template, request, jsonify
import csv
import json
import os

app = Flask(__name__)

# Function to generate Fibonacci sequence
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv():
    # Render CV page
    return render_template('cv.html')

@app.route('/portfolio')
def portfolio():
    # Render Portfolio page
    return render_template('portfolio.html')

@app.route('/biodata')
def biodata():
    # Render Biodata page
    return render_template('biodata.html')

@app.route('/other_biodata')
def other_biodata():
    # Render Biodata page
    return render_template('hobby.html')

@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        n = int(request.form['number'])
        result = generate_fibonacci(n)
        return render_template('fibonacci_result.html', result=result)
    return render_template('fibonacci.html')

@app.route('/jsondata')
def json_data():
    # Read data from CSV and return as JSON
    with open('data.csv', 'r') as file:
        csv_data = list(csv.DictReader(file))
    return jsonify(csv_data)

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('submission.html', name=name, email=email)

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, 'static', 'assets', 'datapribadi.csv')

def csv_to_json(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = [row for row in csv_reader]

    json_data = json.dumps(data)
    return json_data

def showdata():
    if os.path.exists(csv_file_path):
        json_data = csv_to_json(csv_file_path)
        return json_data
    else:
        return 'CSV file not found.'

@app.route('/showdata')
def get_data():
    return showdata()

@app.route('/getdata')
def retrieve_data():
    return render_template('JSON.html')

if __name__ == '__main__':
    app.run(debug=True)
