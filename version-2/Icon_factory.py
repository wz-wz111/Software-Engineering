class IconFactory:
    def __init__(self, icons):
        self.icons = icons

    def get_icon(self, icon_type):
        return self.icons.get(icon_type, '?')
