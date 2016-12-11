from flask import Flask
from flask import request
from flask import redirect, url_for
from flask import render_template

    

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/find', methods=['POST'])
def find():
    if request.method == 'POST':
        language = request.form['language']
        salary = request.form['salary']
        accounts = [{}] # ВОТ ТУТ КОД, КОТОРЫЙ АККАУНТЫ ВЫБИРАЕТ ПО ПЕРЕДАННЫМ ПАРАМЕТРАМ. Accounts - массив словарей
    return render_template('result.html', accounts = accounts)

if __name__ == '__main__':
    app.run(host='localhost', port=80) # ВОТ ТУТ АДРЕС ВАШЕГО СЕРВА

