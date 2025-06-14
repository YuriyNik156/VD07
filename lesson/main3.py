from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Создаем приложение
app = Flask(__name__)

# Настраиваем базу данных
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///example.db" # Эта строчка нужна, чтобы мы могли подключиться к базе данных
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False # Эта строчка отключает сигнализацию об изменении объектов внутри базы данных

# Создаем объект SQLAlchemy
db = SQLAlchmy(app) # Создание объекта, через который мы будем работать с базой данных

# Определяем модель (таблицу в базе данных)
class User(db.Model): # В скобках указываем модель, чтобы в дальнейшем создать именно базу данных
    id = db.Column(db.Integer, primiry_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False) # В скобках описываем поля таблицы

    def __repr__(self): # Этот метод определяет, как объект модели будет выглядеть в виде строки
        return f"<User {self.username}>"

# Создаем таблицу в базе данных
with app.app_context(): # Функция создаёт контекст приложения, который нужен для работы с базой данных
    db.create_all() # Создание всей таблицы, которые определены в классе User

# Добавляем запись в таблицу
@ app.route("/add_user") # С помощью декоратора создаём маршрут, который будет вызывать функцию
def add_user(): # Функция будет создавать объект класса User
    new_user = User(username="new_username")
    db.session.add(new_user) # Добавляем в сессию
    db.session.commit() #  Сохраняем изменения в базу данных
    return "User added" # Вывод сообщения о том, что юзер добавлен в базу данных

# Получаем записи из таблицы
@ app.route("/add_user")
def get_users():
    users = User.query.all() # Получаем всех юзеров из базы данных и сохраняем в переменную users
    return str(users)

if __name__ == "__main__":
    app.run(debug=True)