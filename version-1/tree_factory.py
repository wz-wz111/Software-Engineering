from Style_factory import StyleFactory, Container

# 具体的树形工厂
class TreeFactory(StyleFactory):
    def create_container(self, name, icon_factory):
        return TreeContainer(name, icon_factory)

    def create_leaf(self, name, value, icon_factory):
        return TreeLeaf(name, value, icon_factory)
    
# 定义树形叶子节点
class TreeLeaf(Container):
    def __init__(self, name, value, icon_factory):
        super().__init__(name, icon_factory)
        self.value = value

    def draw(self, level=0, is_last=False, imple_list=[]):
        icon = self.icon_factory.get_icon('leaf')
        prefix = '└─ ' if is_last else '├─ '
        for i in range(1, level):
            if i in imple_list:
                print('│  ', end='')
            else:
                print('   ', end='')

        if self.value is None:
            line = prefix + icon + ' ' + self.name + ' '
        else:
            line = prefix + icon + ' ' + self.name + ': ' + str(self.value) + ' '
        print(line)

# 定义树形容器
class TreeContainer(Container):
    def draw(self, level=0, is_last=False, imple_list=[]):
        icon = self.icon_factory.get_icon('internal')
        prefix = '└─ ' if is_last else '├─ '

        if is_last and level in imple_list:
            imple_list.remove(level)
            
        for i in range(1, level):
            if i in imple_list:
                print('│  ', end='')
            else:
                print('   ', end='')
        if level > 0:
            print(prefix + icon + ' ' + self.name)   
        if not is_last and level > 0:
            imple_list.append(level)
            
        for i, child in enumerate(self.children):
            child_is_last = i == len(self.children) - 1
            child.draw(level + 1, child_is_last, imple_list)