__author__ = 'Hansel Tertius'
from kivy.app import App
from kivy.app import Builder
from kivy.core.window import Window

class MilesToKilometerApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometeres"
        self.root = Builder.load_file('miles_to_kilometer.kv')
        return self.root

    def check(self):
        try:
            value = float(self.root.ids.miles.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, addsub):
        result = self.handle_calculate() + addsub
        self.root.ids.miles.text = str(result)
        self.handle_calculate()

    def handle_calculate(self):
        mile = self.check()
        km = mile * 1.60934
        if mile < 0:
            km = 0.0
        self.root.ids.result.text = str(km)
        return mile


MilesToKilometerApp().run()