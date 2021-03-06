# django-orm-watching-storage
## Пульт охраны банка
Проект позволяет отслеживать посещения хранилища банка.

## Подготовка к работе
Запросите доступ к БД у менеджера вашего банка. Для доступа вам понадобятся хост, порт, имя базы, имя пользователя, пароль, секретный ключ.
Создайте файл `.env` в головном каталоге. Заполните файл по образцу полученными данными. Среди настроек есть `DEBUG`, режим отладки. По умолчанию должен иметь значение `False`.
```
HOST=IP ADDRESS
PORT=PORT
NAME=BASENAME
MY_APP_USER=YOUR USERNAME
PASSWORD=YOUR PASSWORD
SECRET_KEY=YOUR SECRET KEY
DEBUG=False
```  

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Запуск программы
Запустите программу командой
```
python main.py runserver 0.0.0.0:8000
```  

Для просмотра введите в адресной строке браузера
```
http://127.0.0.1:8000/
``` 

## Примечания
Проект позволяет отслеживать онлайн кто из персонала и сколько времени находится в хранилище. Также можно посмотреть историю посещений по любому человеку.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org.](https://dvmn.org/) Моя часть кода подключает БД и выводит на сайт данные из этой базы.
