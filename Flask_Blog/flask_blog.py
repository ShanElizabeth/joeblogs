from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {"author" : "Rihanna Fenty",
     "title": "Trophy Wife 2017",
     "content": "Highlight to the Gods",
     "date_posted": "June 20, 2017"
    },

    {"author" : "Beyonce Knowles",
     "title": "Cochella 2018",
     "content": "First Perfomance Entry",
     "date_posted": "April 20, 2018"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/page3")
def page3():
    return render_template('page3.html')


@app.route("/page4")
def page4():
    return render_template('page4.html')


if __name__ == "__main__":
	app.run(debug = True)