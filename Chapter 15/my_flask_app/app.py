from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Render the index.html template and pass the title variable
    return render_template('index.html', title='Hello, Flask!')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the name from the form data
    name = request.form.get('name')
    return f'Thank you, {name}, for submitting the form!'

if __name__ == '__main__':
    app.run(debug=True)
