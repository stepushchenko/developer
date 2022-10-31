# Internet

### Протоколы передачи данных по сети

TCP - один из протоколов передачи данных интернета. <br>
TCP реализован на уровне ядра операционной системы. <br>
TCP отвечает за то, что данные без потери были переданы <br>
от отправителя (процесс в операционной системе отправителя) <br>
к получателю (процесс в операционной системе получателя)

TCP/IP — набор протоколов передачи данных, получивший название от <br>
двух принадлежащих ему протоколов: TCP (англ. Transmission Control Protocol) <br>
и IP (англ. Internet Protocol)

- HTTP (передача гипертекста)
- FTP (передача файлов)
- POP3 (передача почты)
- SMTP (передача сведений о почтовых отправлениях)
- TELNET
- DTN (дальняя космическая связь)

### HTTP ports
- По умолчанию HTTP смотрит на порт 80. 
- По умолчанию HTTPS смотрит на порт 443.
- По умолчанию SSH смотрит на порт 22.

### HTTP methods
- Метод CONNECT : соединение с сервером
- Метод GET : запрос данных с сервера
- Метод POST : создание
- Метод PUT : для полного обновления данных (мы должны отправить все данные)
- Метод PATCH : для частичного обновления данных (отправляем только изменяемую часть)
- Метод DELETE : удаление
- Метод OPTIONS : возвращает методы запроса, поддерживаемые службой.
- Метод HEAD : возвращает метаинформацию, такую как заголовки ответа.

Дополнительно:

Метод PUT отличается от PATCH тем, что для обновления кусочка информации на сервере с PUT<br>
придется отправить весь объем сведений (включая измененную часть, что равно удалить и <br> 
создать заново), а с PATCH будет достаточно отправить только измененную часть и <br> 
дальше произойдет merge.

### Форматы HTTP request

Для каждого формата задается content-type в заголовке. <br> 

- form-data (используется при отправке данных из формы на сайте)
  - можно отправить текстовые пары (ключ + значение) и файл
  - content-type == multipart/form-data
- x-www-form-urlencoded
  - можно отправить текстовые пары (ключ + значение)
  - content-type == application/x-www-form-urlencoded
- binary
  - можно отправить файлы
- json
  - content-type == application/json
- xml
  - content-type == application/xml
- text
  - content-type == text/plain
- JavaScript
  - content-type == application/javascript
- HTML
  - content-type == text/html


### HTTP response сервера состоит из
1. протокол + статус кода
2. заголовков (или нуля, если заголовков нет) и пустой строки, означающей окончание заголовков 
3. тела HTTP сообщения (необязательно)

### Код состояния HTTP response
- **1XX Information**
  - 100 Continue
  - 101 Switching Protocols
  - 102 Processing
  - 103 Early Hints
- **2XX Success**
  - 200 OK
  - 201 Created
  - 202 Accepted
  - 203 Non-Authoritative Information
  - 205 Reset Content
  - 206 Partial Content
  - 207 Multi-Status (WebDAV)
  - 208 Already Reported (WebDAV)
  - 226 IM Used (HTTP Delt Encoding)
- **3XX Redirection**
  - 300 Multiply Choices
  - 301 Moved Permanently
  - 302 Found
  - 303 See Other
  - 304 Not Modified
  - 305 Use Proxy
  - 306 Unused
  - 307 Temporary Redirect
  - 308 Permanent Redirect
- **4XX Client Error**
  - 400 Bad Request
  - 401 Unauthorized
  - 402 Payment Required
  - 403 Forbidden
  - 404 Not Found
  - 405 Method not Allowed
  - 406 Not Acceptable
  - 407 Proxy Authentication Required
  - 408 Request Timeout
  - 409 Conflict
  - 410 Gone
  - 411 Length Required
  - 412 Precondition Failed
  - 413 Payload Too Large
  - 414 URI Too Large
  - 415 Unsupported Media Type
  - 416 Range Not Satisfiable 
  - 417 Exception Failed
  - 418 I'm a teapot
  - 421 Misdirected Request 
  - 422 Unprocessable Entity (WebDAV)
  - 423 Locked (WebDAV)
  - 424 Failed Dependency (WebDAV)
  - 425 Too Early
  - 426 Upgrade Required
  - 428 Precondition Required
  - 429 Too Many Requests 
  - 431 Request Header Fields Too Large
  - 451 Unavailable for Legal Reasons
  - 499 Client Closed Request
- **5XX Server Error Responses**
  - 500 Internal Server Error
  - 501 Not Implemented
  - 502 Bad Gateway
  - 503 Service Unabailable
  - 504 Gateway timeout
  - 505 HTTP Version Not Supported
  - 507 Insufficient Storage (WebDAV)
  - 508 Loop Detected (WebDAV)
  - 510 Not Extended
  - 511 Network Authentication Required 
  - 599 Network Connect Timeout Error

### Форматы передачи данных
- XML — используется в SOAP (всегда) и REST-запросах (реже); 
- JSON — используется в REST-запросах.
  
### Что такое URL, URI и URN
- URI пример `https://wiki.merionet.ru/images/vse-chto-vam-nuzhno-znat-pro-devops/1.png`
- URL пример `https://wiki.merionet.ru`
- URN пример `images/vse/1.png`
- URI = URL + URN

### Из чего состоит URI
1. `http://` протокол
2. `www.example.com` доменное имя (base URL, host, можно заменить на IP адрес)
3. `:80` порт
4. `/path/to/myfile.html` адрес ресурса на веб сервере
5. `?key1=value1&key2=value2` query параметры запроса
7. `#SomewhereInTheDocument` якорь