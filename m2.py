from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty


class TextWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def buttonClicked(self):
        self.text = 'Hello World'



class TestApp(App):
#    pass
#    def build(self):
#        return Label(text='hello world')
  def __init__(self, **kwargs):
      super(TestApp, self).__init__(**kwargs)
      self.title = 'greeting'

  def build(self):
      return TextWidget()



if __name__ == '__main__':
    TestApp().run()


