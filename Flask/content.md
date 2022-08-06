### Import Flask
```bash
from flask import Flask
```

### Initialization class 
```bash
app = Flask(__name__)
```

### Add route
```bash
@app.route('/')
def index():
    return "Hello, world!"
```

### Run as a file
```bash
if __name__ == '__main__':
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

### Шаблоны 
**Jinja** - движок, встроенный во Flask, который на основе файлов в папке <br>
templates (включающих диманическую разметку на python) генерирует (отрисовывает) <br>
статические HTML документы, которые отдаются браузеру пользователя. 

Шаблоны помогают достичь разделения между визуальным отображением и логикой. 
