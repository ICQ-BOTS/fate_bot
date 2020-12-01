
# [Нейрогадалка](https://icq.im/fate_bot)

<a href="https://icq.im/fate_bot"><img src="https://github.com/ICQ-BOTS/fate_bot/blob/main/fate.png" width="100" height="100"></a>

# Оглавление 
 - [Описание](https://github.com/ICQ-BOTS/fate_bot#описание)
 - [Установка](https://github.com/ICQ-BOTS/fate_bot#установка)
 - [Скриншоты работы](https://github.com/ICQ-BOTS/fate_bot#скриншоты-работы)


# Описание
Гадает, отвечает на вопросы да/нет, предсказывает будущие!

# Установка

1. Установка всех зависимостей 
```bash
pip install -r requirements.txt
```

2. Запуск space tarantool
```bash
tarantoolctl start fate.lua
```
> Файл из папки scheme нужно перекинуть в /etc/tarantool/instances.available

3. Запуск скрипта push_tarantool.py
```bash
python3 push_tarantool.py
```

4. Вставляем токен в fate.bot

5. Запуск бота!
```bash
python3 fate_bot.py
```


# Скриншоты работы
<img src="https://github.com/ICQ-BOTS/fate_bot/blob/main/img/1.png" width="400">
<img src="https://github.com/ICQ-BOTS/fate_bot/blob/main/img/2.png" width="400">