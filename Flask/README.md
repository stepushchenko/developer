# Flask

### Import Flask
```python
from flask import Flask
```

### Initialization class 
```python
app = Flask(__name__)
```

### Add route
```python
@app.route('/')
def index():
    return "Hello, world!"
```

### Run as a file
```python
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
def function():
    return render_template('template.html')
```
