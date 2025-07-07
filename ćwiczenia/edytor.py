from abc import ABC, abstractmethod

class AbstractText(ABC):
    @abstractmethod
    def render(self):
        pass

class Text(AbstractText):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class AbstractTextDecorator(AbstractText):
    def __init__(self, decorated_text):
        self.decorated_text = decorated_text

    def render(self):
        return self.decorated_text.render()

class Bold(AbstractTextDecorator):
    def __init__(self, decorated_text):
        AbstractTextDecorator.__init__(self, decorated_text)

    def render(self):
        return '**'+self.decorated_text.render() + '**'

class Italic(AbstractTextDecorator):
    def __init__(self, decorated_text):
        AbstractTextDecorator.__init__(self, decorated_text)

    def render(self):
        return '*'+self.decorated_text.render()+'*'

class UnderLine(AbstractTextDecorator):
    def __init__(self, decorated_text):
        AbstractTextDecorator.__init__(self, decorated_text)
    def render(self):
        return '__'+self.decorated_text.render()+'__'