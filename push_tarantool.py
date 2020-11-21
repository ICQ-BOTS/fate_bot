from tarantool_utils import *

default = [
	'Звезды говорят, что да',
	'Определенно нет',
	'Определенно да',
	'Возможно, возможно'
]

prophecy = [
	'Берегись белых кошек',
	'Завтра будет лучше, чем вчера, но хуже, чем послезавтра',
	'Сделай сегодня то, что давно откладывал',
	'Смысл жизни - 42'
]

color_start = [
	'Я думаю лучше',
	'Может'
]

color_stop = [
	'зеленый',
	'красный',
	'черный'
]

number = [
	'Твое число',
	'Полагаю',
	'Я бы выбрал',
	'Мой выбор -'
]

for c in default:
	space_default.insert((None, c))

for c in prophecy:
	space_prophecy.insert((None, c))

for c in number:
	space_number.insert((None, c))	

for c in color_start:
	space_color.insert((None, 'start', c))	

for c in color_stop:
	space_color.insert((None, 'end', c))		