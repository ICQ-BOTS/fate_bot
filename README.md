<img src="https://github.com/ICQ-BOTS/fate_bot/blob/main/fate.png" width="100" height="100">


# Нейрогадалка
[Нейрогадалка](https://icq.im/fate_bot)

Старт:
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
