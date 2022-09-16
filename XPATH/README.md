# XPATH

```html

<!-- ATTRIBUTES -->

//form[@id='loginForm']  <!-- form с id=loginForm  -->
//input[@name='username']  <!-- input с name='username' -->
//input[@name='continue'][@type='button']  <!-- input с name='continue' и type='button' -->

<!-- COUNT -->

//form[1]  <!-- первый form на странице -->
//form[@id='loginForm']/input[4]  <!-- form с id='loginForm' -> четвертый input -->
//form[@id='loginForm']/input[1]  <!-- form с id='loginForm' -> первый input -->

<!-- FOLLOWING -->

//input[@name='username']/following::input <!-- следующий input после input c name='username' -->

<!-- CONTAINS -->

//*[contains(text(), 'Ваш текст')]  <!-- поиск элемента по тексту внутри -->
```
