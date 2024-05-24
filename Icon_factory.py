from abc import ABC, abstractmethod

# 定义抽象工厂和具体工厂(图标)
class IconFactory(ABC):
    @abstractmethod
    def get_icon(self, icon_type):
        pass

class ConfigurableIconFactory(IconFactory):
    def __init__(self, icons):
        self.icons = icons

    def get_icon(self, icon_type):
        return self.icons.get(icon_type, '?')