# coding: utf-8
__version__ = "0.3.0"
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform


kv = '''
Button:
    text: 'push me!'
'''

class ServiceApp(App):
    def build(self):
        if platform == "android" :
            from android import AndroidService
            service = AndroidService('mica', 'synchronizing')
            service.start('service started')
            self.service = service

        return Builder.load_string(kv)

if __name__ == '__main__':
    ServiceApp().run()
