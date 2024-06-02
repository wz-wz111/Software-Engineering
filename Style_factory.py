from abc import ABC, abstractmethod

# 抽象工厂
# 功能：创建容器和叶子（推迟到子类实现）

class StyleFactory(ABC):
    @abstractmethod
    def create_container(self, name, icon_factory):
        pass

    @abstractmethod
    def create_leaf(self, name, value, icon_factory):
        pass

# 定义容器(叶子是特殊的容器)
class Container(ABC):
    def __init__(self, name, icon_factory):
        self.name = name
        self.icon_factory = icon_factory
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    # 定义抽象方法（使用多态）
    @abstractmethod
    def draw(self, level=0, is_last=False, imple_list=[]):
        pass
