# Flask

### Start
```python
from flask import Flask  # import

app = Flask(__name__) # initialization class 

@app.route('/')  # create route
def index():
    return "Hello, world!"

if __name__ == '__main__':  # run flask as a file
    app.run(host='localhost', port=5000)
```

### Маршруты
Маршрут (иначе "путь") используется во фреймворке Flask для привязки URL к функции. <br>
Во Flask такая функция называется функцией представления. Она отвечает на запрос <br>
данных конкретной страницы. Во Flask декоратор route используется, <br>
чтобы связать URL-адрес с функцией.

### Множественные маршруты
```bash
@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"
```

###  Динамические маршруты
```bash
@app.route("/albums/<album_number>")
def albums(album_number):
    return f"The album number is {album_number}"
```

### Динамические переменные с конвертером
```bash
@app.route("/albums/<int:album_number>/<string:album_title>")
```

**Виды конвертеров:**
1. `string` строка
2. `int` число
3. `float` число с плавающей точкой
4. `path` полный путь, включая слеши
5. `uuid` принимает строки uuid (символьные id)

### Структура проекта
- папка static (статичные файлы)
  - папка img
    - картинка 1
    - картинка 2
  - папка css
    - style.css
    - style2.css
  - папка js
    - file.js
    - file2.js
- папка templates (шаблоны html файлов)
  - first_page.html
  - second_page.html

### Отладка

**Трассировка стека** — это список методов, которые были вызваны до момента, когда в приложении произошло исключение. 

### Подключение элементов

**Подключение шаблонов в функции представления**
```python
from flask import render_template

def function():
    return render_template('template.html')
```

### Request 

```python
from flask import request

request.method  # вернет POST или GET
request.form.get  # получение данных, отправленных в форме
```

### WTForms
WTForms – это библиотека, написанная на Python и независимая от фреймворков. <br>
Она умеет генерировать формы, проверять их и предварительно заполнять информацией и т.д. <br>
Для установки WTForms используется Flask-WTF.

Flask-WTF – расширение для Flask, которое интегрирует WTForms во Flask. Оно же <br>
предлагает дополнительные функции, такие как: загрузка файлов, reCAPTCHA, <br>
интернационализация (i18n) и другие. 

Установка
```bash
pip install flask-wtf
```
