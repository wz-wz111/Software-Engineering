from abc import ABC, abstractmethod
from Visitor import Element
from Iterator import IterableCollection, ConcreteIterator

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


class Leaf(Element):
    def __init__(self, name, value, icon_factory):
        self.name = name
        self.value = value
        self.icon_factory = icon_factory

    def accept(self, visitor):
        pass
    
