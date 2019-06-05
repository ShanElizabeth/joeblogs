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
     },
    {"author" : "SHAN",
     "title": "HOW TO DROP BITCHES",
     "content": "HOW TO BE A BITCH",
     "date_posted": "April 20, 2018"
     },
    {"author" : "NEREYA",
     "title": "HOW TO EXTRA AF BUT NOH",
     "content": "JUDGE LIKE A QUEEN",
     "date_posted": "April 20, 2018"
     },


]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route("/page3")
def page3():
    return render_template('page3.html')


@app.route("/page4")
def page4():
    return render_template('page4.html')


if __name__ == "__main__":
	app.run(debug = True)