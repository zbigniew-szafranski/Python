class Button(object):
    html = ""
    def get_html(self):
        return self.html

class Image(Button):
    html = "<img></img>"

class Input(Button):
    html = "<input></input>"

class Link(Button):
    html = "<a></a>"

class Flash(Button):
    html = "<object></object>"

class ButtonFactory:
    @staticmethod
    def create_button(typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()

button_obj = ButtonFactory()
button = ["image", "input", "link", "flash"]

for b in button:
    print(button_obj.create_button(b).get_html())