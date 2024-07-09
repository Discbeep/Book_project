from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://openlibrary.org/search.json?q=python')
    books = response.json()['docs'][:10]
    return render_template('home.html', books=books)

@app.route('/book/<book_id>')
def book_details(book_id):
    response = requests.get(f'https://openlibrary.org/works/{book_id}.json')
    book = response.json()
    return render_template('book_details.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)