# Jinja

**Jinja** – один из самых мощных и популярных движков для обработки шаблонов на языке Python.

### Шаблоны 
Во Flask шаблонизатор использует шаблоны для создания html-страниц. <br>
Он предназначен для отделения внешнего вида приложения от его логики. <br>
Это улучшает читаемость кода и упрощает внесение изменений во внешний вид. <br>
Во Flask в качестве движка для обработки шаблонов используется Jinja.

```html
<p>Вот как его зовут: {{ name }}</p> <!-- {{ }} используются для вставки значений переменных -->
```

Для использования выражений доступны стандартные математические операторы, <br>
сравнения, присваивания и логические операторы внутри самих выражений. <br>
Можно написать и сложные уравнения, включенные в сам язык Python <br>
(стандартные библиотеки подключить не удастся, и не все функции будут доступны).

```html
<p>
  2 + 2 = {{ 2 + 2 }}; 
  0,33 / 2 = {{ '{:.1}'.format(0,33 / 2) }};
</p>
```

Можно передать список и вывести конкретный элемент. <br>
А еще возможен вариант, сочетающий использование выражения и переменной, <br> 
где вернули список шаблону из целых чисел от 0 до 4 включительно...

Функция представления:
```python
from flask import Flask  # import
from flask import render_template

app = Flask(__name__) # initialization class

@app.route('/')
def index():
  return render_template(
    'index1.html',
    nums=[i for i in range(5)],
  )
```
Шаблон:
```html
<p> 
  nums[3] * 2 = {{ nums[3] * 2 }}
</p>
```
Вывод: 
```html
num[3] * 2 = 6
```

### Фильтры в шаблонах

```html
{{ “ever lucky” | title }} <!-- выведет Ever Lucky, так как title делает первые буквы заглавными -->
{{ comment | title }}  <!-- сначала все слова в значении переменной comment напишет с заглавной буквы, а затем выведет результат -->
{{ <p>title</p> | striptags | title }} <!-- сначала удалит теги, потом напишет с большой буквы и выведет Title -->
{{ 1.23223112 | round(2) }} <!-- округлит значение до 2 знаков после точки и выведет 1.23 -->
```
Полный список фильтров на официальном сайте https://jinja.palletsprojects.com/en/2.10.x/templates/#list-of-builtin-filters

### Подключение CSS файлов из папки static в шаблоне
```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

### Подключение изображений из папки static в шаблоне
```html
<img src="{{ url_for('static', filename='img/girl.jpeg') }}" alt="girl img" width="240" height="240">
<!-- 
img -> тег
src -> ссылка на расположение картинки
alt -> замещающий текст
width -> ширина изображения
height -> высота изображения
-->
```

### Условия 
```html
{% if age % 10 == 0 %}
    <p>10</p>
{% elif age % 5 == 0 %}
    <p>5</p>
{% else %}
    <p>Other</p>
{% endif %}
```

### Переменные
```html
{% set listic = [] %}  <!-- создали переменную -->
{% listic[0] = a %}  <!-- присвоили переменной новое значение -->
```

### Списки
```html
{# Initialise myList with some values #}
{% set myList = [1,5,3,4,2] %}

{# add 5 to myList #} 
{% append 5 to myList %}

{# remove the second item from the list #} 
{% set temp = myList.pop(1) %}

{# find the index of the number 2 in myList #}
{% set myIndex = myList.index(2) %}

{# pop the number two from myList #} 
{% set temp = myList.pop(myIndex) %}

{# output the list and index of 1 #} 
{{ "values in my list:"}}
{{ myList }}
{% set indexOne = myList.index(1) %} 
{{ "</br> index of the number one:" }}
{{ indexOne }}
```

### Циклы 
```html
{% for name, details in {'Igor': [22, 'Trainer'], 'Ivan': [4, 'Admin']}.items() %}
    <p>{{ name }}</p>]
    <p>
        <ul>
            {% for detail in details %}
                <li>{{ detail }}</li>
            {% endfor %}
        </ul>
    </p>
{% endfor %}
```


### Макросы == Функции
```html
{% macro functionTitle(x, y=5) %}
    <h3>Sum {{ x }} + {{ y }}</h3>
    <p>{{ x + y }}</p>
{% endmacro %}

{{ functionTitle(3) }}
{{ functionTitle(4, 1) }}
```

Вместо того, чтобы использовать макросы прямо в шаблоне, <br>
лучше хранить их в отдельном файле и импортировать по надобности. <br>
Предположим, все макросы хранятся в файле macros.html в папке templates. <br>
Чтобы импортировать их из файла, нужно использовать инструкцию import:

```html
{% import "macros.html" as macros %}
```

Использование макросов из отдельного файла: 
```html
{% import "macros.html" as macros %}
{{ macros.functionTitle(1,4) }}
```
или
```html
{% from "macros.html" import functionTitle %}
{{ functionTitle(1, 9) }}
```

### Вложенные шаблоны 
Все шаблоны лежат на одном уровне в папке templates.
Чтобы вставить один шаблон в другой, необходимо вызвать в шаблоне:
```html
{% include 'template_title.html' %}
```

### Родительские и дочерние шаблоны
Чтобы шаблоны могли строиться по принципам ООП, необходимо дать возможность <br>
дочерним шаблонам переопределять содержимое родительского шаблона. 

Родительский шаблон в том месте, где контент будет переопределяться 
дочерними шаблонами должен иметь вставку:
```html
{% block blockTitle %}

{% endblock %}
```
Чтобы дочерний шаблон мог переписать контент родительского шаблона, 
дочерний шаблон должен сослаться на родителя: 
```html
{% extends 'parentTemplateTitle.html' %}

{% block blockTitle %}
<p>content</p>
{% endblock $}
```