from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    posts = [
        {"title": "How to Style Your Basket", "content": "Discover tips to decorate your basket...", "link": "#"},
        {"title": "Eco-Friendly Baskets", "content": "Learn about sustainable basket production...", "link": "#"},
        {"title": "Perfect Gifts for Any Occasion", "content": "Explore how baskets make great gifts...", "link": "#"},
    ]
    return render_template('blog.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
