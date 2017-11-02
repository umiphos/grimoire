from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
	PageLayout:
		RelativeLayout:
			background_color: (1, 50, 20, 1)
			text: 'Sensores'
			border: (10, 10, 10, 10)
			on_press: 
				root.manager.current = 'sensores'
				root.manager.transition.direction = 'up'

		Button:
			text: 'Actuadores'
			on_press:
				root.manager.current = 'actuadores'
				root.manager.transition.direction = 'up'

<Sensores>:
	BoxLayout:
		Button:
			border: (10, 10, 10, 10)
			text: 'Back to menu'
			on_press: 
				root.manager.current = 'menu'
				root.manager.transition.direction = 'down'
				

<Actuadores>:
	BoxLayout:
		Button:
			text: 'Back to menu'
			size: 50,50
			on_press:
				root.manager.current = 'menu'
				root.manager.transition.direction = 'down'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class Sensores(Screen):
    pass

class Actuadores(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Sensores(name='sensores'))
sm.add_widget(Actuadores(name='actuadores'))

class TestApp(App):
	def build(self):
		return sm

if __name__ == '__main__':
    TestApp().run()