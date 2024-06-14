from Style_factory import StyleFactory, Container, Leaf

# 具体的树形工厂
class TreeFactory(StyleFactory):
    def create_container(self, name, icon_factory):
        return TreeContainer(name, icon_factory)

    def create_leaf(self, name, value, icon_factory):
        return TreeLeaf(name, value, icon_factory)
    
# 定义树形叶子节点
class TreeLeaf(Leaf):
    def accept(self, visitor):
        return visitor.draw_tree_leaf(self)

# 定义树形容器
class TreeContainer(Container):
    def accept(self, visitor):
        return visitor.draw_tree_container(self)
