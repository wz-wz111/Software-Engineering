from abc import ABC, abstractmethod

# 迭代器模式

# 声明迭代器接口
class Iterator:
    def get_element(self):
        pass

    def next(self):
        pass
    
    def has_next(self):
        pass

# 声明集合接口(不同迭代方式)
class IterableCollection:
    def create_iterator(self):
        pass

# 实现具体迭代器类（list）
class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0
    
    def get_element(self):
        return self._collection[self._index]
    
    def next(self):
        if self.has_next():
            self._index += 1
        else:
            raise StopIteration
    
    def has_next(self):
        return self._index < len(self._collection) 


# 访问者模式

# 声明访问者接口
class Visitor:
    def visit_container(self, container):
        pass

    def visit_leaf(self, leaf):
        pass

# 声明元素接口
class Element:
    def accept(self, visitor):
        pass

# 实现具体访问者类
# class DrawVisitor(Visitor):
#     def visit_container(self, container):
#         # 使用迭代器进行draw
#         if(container.__class__.__name__ == 'RectangleContainer'):
#             Draw().draw_rectangle_container(container)
#         else:
#             Draw().draw_tree_container(container)

#     def visit_leaf(self, leaf):
#         # 使用迭代器进行draw
#         leaf.draw()


width = 50
# 实现绘图类
class DrawVisitor(Visitor):
    def draw_rectangle_container(self, container, level=0, is_last=False, imple_list=[], iterator=None):
        icon = container.icon_factory.get_icon('internal')
        iterator = container.create_iterator()
        prefix = '├─ '
        if level == 0:
            print('┌' + '─' * (width - 2) + '┐')
        else:
            line = "│  " * (level - 1) + prefix + icon + ' ' + container.name + ' '
            line_length = len(line) 
            remaining_length = width - 1 - line_length
            print(line + '─' * remaining_length + '┤')

        while iterator.has_next():
            child = iterator.get_element()
            iterator.next()
            child_is_last = not iterator.has_next()
            if child.__class__.__name__ == 'RectangleLeaf':
                self.draw_rectangle_leaf(child, level + 1, child_is_last)
            else:
                self.draw_rectangle_container(child, level + 1, child_is_last)

        if level == 0:
            print('└' + '─' * (width - 2) + '┘')
    
    def draw_rectangle_leaf(self, leaf, level=0, is_last=False, imple_list=[]):
        icon = leaf.icon_factory.get_icon('leaf')
        prefix = '├─ '
        if leaf.value is None:
            line = "│  " * (level - 1) + prefix + icon + ' ' + leaf.name + ' '
        else:
            line = "│  " * (level - 1) + prefix + icon + ' ' + leaf.name + ': ' + str(leaf.value) + ' '
        line_length = len(line)
        remaining_length = width - line_length - 1
        print(line + '─' * remaining_length + '┤')
    
    def draw_tree_container(self, container, level=0, is_last=False, imple_list=[], iterator=None):
        icon = container.icon_factory.get_icon('internal')
        iterator = container.create_iterator()
        prefix = '└─ ' if is_last else '├─ '

        if is_last and level in imple_list:
            imple_list.remove(level)
            
        for i in range(1, level):
            if i in imple_list:
                print('│  ', end='')
            else:
                print('   ', end='')
        if level > 0:
            print(prefix + icon + ' ' + container.name)   
        if not is_last and level > 0:
            imple_list.append(level)
            
        while iterator.has_next():
            child = iterator.get_element()
            iterator.next()
            child_is_last = not iterator.has_next()
            if child.__class__.__name__ == 'TreeLeaf':
                self.draw_tree_leaf(child, level + 1, child_is_last, imple_list)
            else:
                self.draw_tree_container(child, level + 1, child_is_last, imple_list)

    def draw_tree_leaf(self, leaf, level=0, is_last=False, imple_list=[]):
        icon = leaf.icon_factory.get_icon('leaf')
        prefix = '└─ ' if is_last else '├─ '
        for i in range(1, level):
            if i in imple_list:
                print('│  ', end='')
            else:
                print('   ', end='')

        if leaf.value is None:
            line = prefix + icon + ' ' + leaf.name + ' '
        else:
            line = prefix + icon + ' ' + leaf.name + ': ' + str(leaf.value) + ' '
        print(line)

        

# 抽象工厂
# 功能：创建容器和叶子（推迟到子类实现）
class StyleFactory(ABC):
    @abstractmethod
    def create_container(self, name, icon_factory):
        pass

    @abstractmethod
    def create_leaf(self, name, value, icon_factory):
        pass

class Container(Element, IterableCollection):
    def __init__(self, name, icon_factory):
        self.name = name
        self.icon_factory = icon_factory
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def create_iterator(self):
        return ConcreteIterator(self.children)
    
    def accept(self, visitor):
        pass

    # @abstractmethod
    # def draw(self, level=0, is_last=False, imple_list=[], iterator=None):
    #     pass

class Leaf(Element):
    def __init__(self, name, value, icon_factory):
        self.name = name
        self.value = value
        self.icon_factory = icon_factory

    def accept(self, visitor):
        pass
    
    # @abstractmethod
    # def draw(self, level=0, is_last=False, imple_list=[]):
    #     pass

