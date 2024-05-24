from abc import ABC, abstractmethod

width = 50
# 定义容器和叶子类(叶子是特殊的容器)
class Container(ABC):
    def __init__(self, name, icon_factory):
        self.name = name
        self.icon_factory = icon_factory
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    @abstractmethod
    def draw(self, level=0, is_last=False, imple_list=[]):
        pass

class Tree_Leaf(Container):
    def __init__(self, name, value, icon_factory):
        super().__init__(name, icon_factory)
        self.value = value

    def draw(self, level=0, is_last=False, imple_list=[]):
        icon = self.icon_factory.get_icon('leaf')
        prefix = '└─ ' if is_last else '├─ '
        for i in range(1, level):
            if(i in imple_list):
                print('│  ', end='')
            else:
                print('   ', end='')

        if(self.value == None):
            line = prefix + icon + ' ' + self.name + ' '
        else:
            line = prefix + icon + ' ' + self.name + ': ' + str(self.value) + ' '
        print(line)
        
class Rec_Leaf(Container):
    def __init__(self, name, value, icon_factory):
        super().__init__(name, icon_factory)
        self.value = value
        
    def draw(self, level=0, is_last=False, imple_list=[]):
        icon = self.icon_factory.get_icon('leaf')
        prefix = '├─ '
        if(self.value == None):
            line = "│  " * (level - 1)  + prefix + icon + ' ' + self.name + ' '
        else:
            line = "│  " * (level - 1)  + prefix + icon + ' ' + self.name + ': ' + str(self.value) + ' '
        line_length = len(line)
        # 对齐
        remaining_length = width - line_length - 1
        print(line + '─' * remaining_length + '┤')


# 定义树形和矩形容器
class TreeContainer(Container):
    def draw(self, level=0, is_last=False, imple_list=[]):
        icon = self.icon_factory.get_icon('internal')
        prefix = '└─ ' if is_last else '├─ '

        # 删除多余竖线
        if(is_last and level in imple_list):
            imple_list.remove(level)
            
        for i in range(1, level):
            if(i in imple_list):
                print('│  ', end='')
            else:
                print('   ', end='')
        if(level > 0):
            print(prefix + icon + ' ' + self.name)   
        if(not is_last and level > 0):
            imple_list.append(level)
            
        for i, child in enumerate(self.children):
            child_is_last = i == len(self.children) - 1
            child.draw(level + 1, child_is_last, imple_list)

class RectangleContainer(Container):
    def draw(self, level=0, is_last=False, imple_list=[]):
        icon = self.icon_factory.get_icon('internal')
        prefix = '├─ '
        # 矩形容器的第一行
        if level == 0:
            print('┌' + '─' * (width - 2) + '┐')
        else:
            line = "│  " * (level-1) + prefix + icon + ' ' + self.name + ' '
            line_length = len(line) 
            remaining_length = width - 1 - line_length
            print(line + '─' * remaining_length + '┤')

        for i, child in enumerate(self.children):
            child_is_last = i == len(self.children) - 1
            child.draw(level + 1, child_is_last)

        # 矩形容器的最后一行
        if level == 0:
            print('└' + '─' * (width - 2) + '┘')