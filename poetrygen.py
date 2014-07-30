import bacon


window = game_function()
bacon.window.width = 640
bacon.window.height = 540
bacon.window.fullscreen = False

class Interface(bacon.Game):
	def on_tick(self):
