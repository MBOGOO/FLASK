from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management and flash messages

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your authentication logic here
        if username == 'admin' and password == 'password':  # Dummy check
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

