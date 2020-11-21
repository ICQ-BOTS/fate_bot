import tarantool

connection = tarantool.connect('89.208.198.172', 3307)

space_default = connection.space('default')

space_prophecy = connection.space('prophecy')

space_color = connection.space('color')

space_number = connection.space('number')
		