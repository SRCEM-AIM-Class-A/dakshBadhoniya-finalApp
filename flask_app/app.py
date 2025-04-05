from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'password-3000'  # For development only; use a secure key for production

# Root route: render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route for greeting form and processing user input
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        # Basic error handling: ensure both fields are provided and age is numeric
        if not name or not age:
            flash("Please provide both your name and age.")
            return redirect(url_for('greet'))
        try:
            age = int(age)
        except ValueError:
            flash("Age must be a number.")
            return redirect(url_for('greet'))
        return render_template('greeting.html', name=name, age=age)
    return render_template('greet.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
