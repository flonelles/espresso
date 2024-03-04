from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '</br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!'])


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" width="100" height="111"
                         alt="здесь должна была быть картинка, но не нашлась">
                        <p>Вот она какая, красная планета</p>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
                        rel="stylesheet" 
                        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
                        crossorigin="anonymous">
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" width="100" height="111"
                         alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-dark" role="alert">Человечество вырастает из детства.</div>
                        <div class="alert alert-success" role="alert">Человечеству мала одна планета.</div>
                        <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты</div>
                        <div class="alert alert-warning" role="alert">И начнём с Марса!</div>
                        <div class="alert alert-danger" role="alert">Присоединяйся!</div>
                      </body>
                    </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
                            rel="stylesheet" 
                            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
                            crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                          <body>
                            <h1>Мое предложение: {planet_name}</h1>
                            <h2>Эта планета близка к земле;</h2>
                            <div class="alert alert-success" role="alert">На ней много необходимых ресурсов;</div>
                            <div class="alert alert-secondary" role="alert">На ней есть вода и атмосфера;</div>
                            <div class="alert alert-warning" role="alert">На ней есть небольшое магнитное поле;</div>
                            <div class="alert alert-danger" role="alert">Наконец, она просто красива!</div>
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
