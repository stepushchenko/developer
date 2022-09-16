# XPATH

```html

<!-- ATTRIBUTES -->

//form[@id='loginForm']  <!-- найдет form с id=loginForm  -->
//input[@name='username']  <!-- найдет input с name='username' -->
//input[@name='continue'][@type='button']  <!-- найдет input с name='continue' и type='button' -->

<!-- COUNT -->

//form[1]  <!-- первый form на странице -->
//form[@id='loginForm']/input[4]  <!-- найдет четвертый input после form с id='loginForm' -->

<!-- CONTAINS -->

//*[contains(text(), 'Ваш текст')]  <!-- найдет элемент по тексту внутри -->
//*[contains(@id,"content-body")]  <!-- найдет элемент по значению id -->
//*[contains(@class,"content-body")  <!-- найдет элемент по значению class -->

<!-- STARTS-WITH -->

//*[starts-with(@id,'username')]  <!-- найдет все элементы, у которых id начинается с username (ex: username1, username-Bob)

<!-- FOLLOWING -->

//*[@name='username']/following::input <!--  найдет следующий input на одном уровне после элемента c name='username' -->

<!-- PARENT -->

//*[@name='username']/parent::input <!-- найдет родительский тег input для элемента c name='username' -->
```
