from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():
    user_name = None
    user_feedback = None
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_feedback = request.form.get('feedback')
    return render_template('feedback.html', name=user_name, feedback=user_feedback)

if __name__ == '__main__':
    app.run(debug=True)
