[<img src="https://img.shields.io/badge/Telegram-%40Me-orange">](https://t.me/sho6ot)

![alt text](https://i.imgur.com/PDYwSJ9.png)

> 🇪🇳 README in english available [here](README-EN.md)

## Функционал  
+ _Многопоточность_
+ _Привязка прокси к сессии_
+ _Авто-покупка предметов при наличии денег (energy boost, speed boost, click boost)_
+ _Рандомное время сна между кликами_
+ _Рандомное количество кликов за запрос_
+ _Поддержка tdata / pyrogram .session / telethon .session_

## [Настройки](https://github.com/shamhi/NotCoinBot/blob/main/data/config.py">)
+ **API_ID / API_HASH** - Данные платформы, с которой запускать сессию Telegram (сток - Android)
***
+ **MIN_CLICKS_COUNT** - Минимальное количество кликов за один запрос (считается без множителя, т.е напр. при множителе x9: 1 клик будет равнятся 9 монетам, а не одной)
***
+ **MIN_AVAILABLE_COINS** - Минимальное количество коинов, при достижении которых будет задержка (напр. 200)
***
+ **AUTO_BUY_ENERGY_BOOST** - Автоматическая покупка Energy Boost при достижении баланса (True / False)
***
+ **AUTO_BUY_SPEED_BOOST** - Автоматическая покупка Speed Boost при достижении баланса (True / False)
***
+ **AUTO_BUY_CLICK_BOOST** - Автоматическая покупка Click Boost при достижении баланса (True / False)
***
+ **SLEEP_BY_MIN_COINS** - Использовать-ли задержку при достижении минимального количества коинов (True / False)
***
+ **USE_PROXY_FROM_FILE** - Использовать-ли Proxy из файла data/proxies.txt для аккаунтов, к которым не привязаны Proxy (True / False)
***
+ **SLEEP_BETWEEN_CLICK** - Диапазон задержки между кликами (в секундах)
***
+ **SLEEP_BEFORE_BUY_MERGE** - Диапазон задержки перед покупкой бустов (в секундах)
***
+ **SLEEP_BEFORE_ACTIVATE_FREE_BUFFS** - Диапазон задержки перед активацией ежедневных бустов (в секундах)
***
+ **SLEEP_BEFORE_ACTIVATE_TURBO** - Диапазон задержки перед активацией Turbo (в секундах)
***
+ **SLEEP_TO_UPDATE_USER_DATA** - Задержка перед обновлением данных о пользователе (в минутах)
***
+ **SLEEP_BY_MIN_COINS_TIME** - Задержка при достижении минимального количетсва коинов (в секундах)

## Установка
Вы можете скачать [**Репозиторий**](https://github.com/shamhi/NotCoinBot) клонированием на вашу систему и установкой необходимых зависимостей:
```
~ >>> git clone https://github.com/shamhi/NotCoinBot.git 
~ >>> cd NotCoinBot.git

# Linux
~/NotCoinBot >>> python3 -m venv venv
~/NotCoinBot >>> source venv/bin/activate
~/NotCoinBot >>> pip3 install -r requirements.txt
~/NotCoinBot >>> python3 main.py

# Windows
~/NotCoinBot >>> python -m venv venv
~/NotCoinBot >>> .\venv\Scripts\activate
~/NotCoinBot >>> pip install -r .\requirements.txt
~/NotCoinBot >>> python .\main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```
~/NotCoinBot >>> python3 main.py --action (1/2)
# Или
~/NotCoinBot >>> python3 main.py -a (1/2)

# 1 - Запускает регистратор сессии
# 2 - Запускает все сохраненные сессии
```
