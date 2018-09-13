from flask import Flask
import random
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    tommorrows_movie = get_random_movie()
    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"
    content += "<h3><em>Tommorrow's Movie</em></h3>"
    content += "<ul>"
    content += "<li>" + tommorrows_movie + "</li>"
    content += "</ul>"
    # TODO: pick another random movie, and display it under
    # render the heading 
    # select a movie
    #add movie to string which is composed of html
    # heading==> "<h1>Tommorrow's Movie</h1>"



    return content

def get_random_movie():
    movies = ['Ace Ventura: Pet Detective','The Grinch','Ernest: Scared Silly','Avengers','Grease']

    # TODO: randomly choose one of the movies, and return it
    a_movie = movies[random.randrange(0,len(movies))]
    return a_movie


app.run()
