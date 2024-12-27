from flask import Flask, render_template, redirect, url_for, request, flash
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Logic to handle user registration
        flash("Successfully Registered!", "success")
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic to handle login
        flash("Logged in successfully!", "success")
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    # Logic to fetch and display a specific blog post
    return render_template('post.html', post_id=post_id)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        # Logic to handle creating a new blog post
        flash("Post created successfully!", "success")
        return redirect(url_for('home'))
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run(debug=True)