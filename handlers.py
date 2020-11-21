import asyncio
from random import randint, choice
from tarantool_utils import space_default, space_prophecy, space_color, space_number


async def default_command(bot, event):
	await sleep_send(bot, event)
	await bot.send_text(
			chat_id=event.from_chat,
			text=choice(space_default.select())[1]
		)       


async def sleep_send(bot, event):
	await bot.send_actions(chat_id=event.data['chat']['chatId'], actions='typing')
	await asyncio.sleep(2)


async def rand_prophecy(bot, event):
	await sleep_send(bot, event)
	await bot.send_text(
			chat_id=event.from_chat,
			text=choice(space_prophecy.select())[1]
		)       


async def rand_number(bot, event):
	await sleep_send(bot, event)
	await bot.send_text(
			chat_id=event.from_chat,
			text=choice(space_number.select())[1] + ' ' + str(randint(1, 100))
		)       


async def rand_color(bot, event):
	await sleep_send(bot, event)
	await bot.send_text(
			chat_id=event.from_chat,
			text=choice(space_color.select('start', index='type'))[2] + ' ' + choice(space_color.select('end', index='type'))[2]
		)       


async def start(bot, event):
	await bot.send_text(
			chat_id=event.from_chat,
			text="""https://files.icq.net/get/09B9B000fg6W7luRnYpszQ5f85dcbe1ae
Приветствую тебя! 🧙🏼‍♀️

Я — нейрогадалка. Задавай вопрос, на который можно ответить да/нет или напиши «погадай». 

Погадаю, расскажу, что знаю, что вижу. А вижу я многое…. 👁"""
		)	


async def media(bot, event):
	await bot.send_text(
			chat_id=event.from_chat,
			text="Пришли, пожалуйста, текстовое сообщение"
		)	

