from Style_factory import StyleFactory, Container, Leaf

width = 50
# 具体的矩形工厂
class RectangleFactory(StyleFactory):
    def create_container(self, name, icon_factory):
        return RectangleContainer(name, icon_factory)

    def create_leaf(self, name, value, icon_factory):
        return RectangleLeaf(name, value, icon_factory)

# 定义矩形叶子节点
class RectangleLeaf(Leaf):
    def accept(self, visitor):
        return visitor.draw_rectangle_leaf(self)
    # def draw(self, level=0, is_last=False, imple_list=[]):
    #     icon = self.icon_factory.get_icon('leaf')
    #     prefix = '├─ '
    #     if self.value is None:
    #         line = "│  " * (level - 1) + prefix + icon + ' ' + self.name + ' '
    #     else:
    #         line = "│  " * (level - 1) + prefix + icon + ' ' + self.name + ': ' + str(self.value) + ' '
    #     line_length = len(line)
    #     remaining_length = width - line_length - 1
    #     print(line + '─' * remaining_length + '┤')

# 定义矩形容器
class RectangleContainer(Container):
    def accept(self, visitor):
        return visitor.draw_rectangle_container(self)
    # def draw(self, level=0, is_last=False, imple_list=[], iterator=None):
    #     icon = self.icon_factory.get_icon('internal')
    #     iterator = self.create_iterator()
    #     prefix = '├─ '
    #     if level == 0:
    #         print('┌' + '─' * (width - 2) + '┐')
    #     else:
    #         line = "│  " * (level - 1) + prefix + icon + ' ' + self.name + ' '
    #         line_length = len(line) 
    #         remaining_length = width - 1 - line_length
    #         print(line + '─' * remaining_length + '┤')

    #     while iterator.has_next():
    #         child = iterator.next()
    #         child_is_last = not iterator.has_next()
    #         child.draw(level + 1, child_is_last)

    #     if level == 0:
    #         print('└' + '─' * (width - 2) + '┘')
