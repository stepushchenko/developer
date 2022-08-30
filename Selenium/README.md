# SELENIUM

### Drivers

Chromedriver permissions on MacOS
```bash
cd usr/local/bin
xattr -d com.apple.quarantine chromedriver 
```

### XPATH examples

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>
```

```html
login_form = driver.find_element_by_xpath("//form[1]")  <!-- первый form на странице -->
login_form = driver.find_element_by_xpath("//form[@id='loginForm']")  <!-- form с id=loginForm  -->

username = driver.find_element_by_xpath("//form[input/@name='username']")  <!-- form / input с name='username' -->
username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")  <!-- form с id='loginForm' / первый input -->
username = driver.find_element_by_xpath("//input[@name='username']")  <!-- input с name='username' -->

clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")  <!-- input с name='continue' и type='button' -->
clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")  <!-- form с id='loginForm' / четвертый input -->

password = driver.find_element_by_xpath("//input[@name='username']/following::input") <!-- следующий input после input c name='username' -->

```

```html
//*[contains(text(), 'Ваш текст')]  <!-- поиск элемента по тексту внутри -->
```
