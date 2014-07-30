import bacon



bacon.window.width = 640
bacon.window.height = 540
bacon.window.fullscreen = False

class Interface(bacon.Game):
	def on_tick(self):
		bacon.push_color()
		bacon.set_color(0, 0, 0, 1)
		bacon.draw_rect(0,0, 640, 540)
		bacon.pop_color()
		bacon.set_color(1, 1, 1, 1)
		bacon.draw_rect(10, 10, 630, 530)
		bacon.pop_color()


bacon.run(Interface())