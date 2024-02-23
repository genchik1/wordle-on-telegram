import asyncio
import json
import os.path

from models import Words
from settings.db import async_session


async def filling_out_the_table_with_words() -> None:
    """Заполнение таблицы со словами"""

    with open('/data/words.json') as json_file:
        words = json.loads(''.join(json_file.readlines()))['words']  # type: ignore
    async with async_session() as session:
        word_instances = []
        for word in words:
            word_instances.append(Words(word=word))
        session.add_all(word_instances)
        await session.commit()


if __name__ == '__main__':
    asyncio.run(filling_out_the_table_with_words())
