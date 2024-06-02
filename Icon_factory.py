# 图标工厂类，用于获取图标
class IconFactory:
    def __init__(self, icons):
        self.icons = icons

    def get_icon(self, icon_type):
        return self.icons.get(icon_type, '?')