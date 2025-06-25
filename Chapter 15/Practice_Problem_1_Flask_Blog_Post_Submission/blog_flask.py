from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store blog posts
blog_posts = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            blog_posts.append({'title': title, 'content': content})
            return redirect(url_for('home'))
    return render_template('home.html', blog_posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)
