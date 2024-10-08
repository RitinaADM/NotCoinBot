import json

import pyrogram
from better_proxy import Proxy
from loguru import logger

from data import config
from database import actions as db_actions


async def create_sessions() -> None:
    API_ID: int | str = config.API_ID
    API_HASH: str = config.API_HASH
    while True:
        if not API_ID or not API_HASH:
            API_ID: int | str = input('\nВведите ваш API_ID (для выхода нажмите Enter): ')
            API_HASH: str = input('\nВведите ваш API_HASH (для выхода нажмите Enter): ')

        session_name: str = input('\nВведите название сессии (для выхода нажмите Enter): ')

        if not session_name or not API_ID or not API_HASH:
            return

        config_data = {
            'API_ID': API_ID,
            'API_HASH': API_HASH
        }

        with open('settings.json', 'w') as file:
            json.dump(config_data, file, indent=4, ensure_ascii=False)

        while True:
            proxy_str: str = input('Введите Proxy (type://user:pass@ip:port // type://ip:port, для использования без '
                                   'Proxy нажмите Enter): ').replace('https://', 'http://')

            if proxy_str:
                try:
                    proxy: Proxy = Proxy.from_str(
                        proxy=proxy_str
                    )

                    proxy_dict: dict = {
                        'scheme': proxy.protocol,
                        'hostname': proxy.host,
                        'port': proxy.port,
                        'username': proxy.login,
                        'password': proxy.password
                    }

                except ValueError:
                    logger.error(f'Неверно указан Proxy, повторите попытку ввода')

                else:
                    break

            else:
                proxy: None = None
                proxy_dict: None = None
                break

        session: pyrogram.Client = pyrogram.Client(
            api_id=API_ID,
            api_hash=API_HASH,
            name=session_name,
            workdir='sessions',
            proxy=proxy_dict
        )

        async with session:
            user_data = await session.get_me()

        logger.success(f'Успешно добавлена сессия {user_data.username} | {user_data.first_name} {user_data.last_name}')

        await db_actions.add_session(session_name=session_name,
                                     session_proxy=proxy.as_url if proxy else '')
