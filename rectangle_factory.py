from Style_factory import StyleFactory, Container

width = 50
# 具体的矩形工厂
class RectangleFactory(StyleFactory):
    def create_container(self, name, icon_factory):
        return RectangleContainer(name, icon_factory)

    def create_leaf(self, name, value, icon_factory):
        return RecLeaf(name, value, icon_factory)

# 定义矩形叶子节点
class RecLeaf(Container):
    def __init__(self, name, value, icon_factory):
        super().__init__(name, icon_factory)
        self.value = value
        
    def draw(self, level=0, is_last=False, imple_list=[]):
        icon = self.icon_factory.get_icon('leaf')
        prefix = '├─ '
        if self.value is None:
            line = "│  " * (level - 1) + prefix + icon + ' ' + self.name + ' '
        else:
            line = "│  " * (level - 1) + prefix + icon + ' ' + self.name + ': ' + str(self.value) + ' '
        line_length = len(line)
        remaining_length = width - line_length - 1
        print(line + '─' * remaining_length + '┤')

# 定义矩形容器
class RectangleContainer(Container):
    def draw(self, level=0, is_last=False, imple_list=[]):
        icon = self.icon_factory.get_icon('internal')
        prefix = '├─ '
        if level == 0:
            print('┌' + '─' * (width - 2) + '┐')
        else:
            line = "│  " * (level - 1) + prefix + icon + ' ' + self.name + ' '
            line_length = len(line) 
            remaining_length = width - 1 - line_length
            print(line + '─' * remaining_length + '┤')

        for i, child in enumerate(self.children):
            child_is_last = i == len(self.children) - 1
            child.draw(level + 1, child_is_last)

        if level == 0:
            print('└' + '─' * (width - 2) + '┘')