# __author:Smita Nannaware
# data:3/31/2022
from flask import Flask, render_template, request

#import model_recommender

app = Flask(__name__)


# default-page
@app.route('/')
def home():
    #movieList = ['test1', 'test2', 'test3']
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getMovies():
    search_text = request.form.get('searchText')
    print(search_text)
    movieList = ['test1', 'test2', 'test3']
    return render_template('results.html', movieList=movieList)


if __name__ == '__main__':
    app.run()
