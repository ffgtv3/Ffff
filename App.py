# Импортировать библиотеку Flask
from flask import Flask, request, redirect, url_for

# Создать экземпляр приложения Flask
app = Flask(__name__)

# Определить маршрут для корневого URL-адреса ('/')
@app.route('/')
def index():
    # Проверить, есть ли в запросе параметр 'url'
    url = request.args.get('url')

    # Если параметра 'url' нет, перенаправить на домашнюю страницу
    if not url:
        return redirect(url_for('home'))

    # В противном случае перенаправить на указанный URL-адрес
    return redirect(url)

# Определить маршрут для домашней страницы ('/home')
@app.route('/home')
def home():
    # Возвращает сообщение с домашней страницы
    return '<h1>Добро пожаловать на домашнюю страницу!</h1>'

# Запустить приложение
if __name__ == '__main__':
    app.run(debug=True)
