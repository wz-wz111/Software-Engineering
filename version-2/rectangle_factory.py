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


# 定义矩形容器
class RectangleContainer(Container):
    def accept(self, visitor):
        return visitor.draw_rectangle_container(self)
