from Style_factory import StyleFactory, Container, Leaf, DrawVisitor

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
    # def draw(self, level=0, is_last=False, imple_list=[]):
    #     icon = self.icon_factory.get_icon('leaf')
    #     prefix = '└─ ' if is_last else '├─ '
    #     for i in range(1, level):
    #         if i in imple_list:
    #             print('│  ', end='')
    #         else:
    #             print('   ', end='')

    #     if self.value is None:
    #         line = prefix + icon + ' ' + self.name + ' '
    #     else:
    #         line = prefix + icon + ' ' + self.name + ': ' + str(self.value) + ' '
    #     print(line)

# 定义树形容器
class TreeContainer(Container):
    def accept(self, visitor):
        return visitor.draw_tree_container(self)
    # def draw(self, level=0, is_last=False, imple_list=[], iterator=None):
    #     icon = self.icon_factory.get_icon('internal')
    #     iterator = self.create_iterator()
    #     prefix = '└─ ' if is_last else '├─ '

    #     if is_last and level in imple_list:
    #         imple_list.remove(level)
            
    #     for i in range(1, level):
    #         if i in imple_list:
    #             print('│  ', end='')
    #         else:
    #             print('   ', end='')
    #     if level > 0:
    #         print(prefix + icon + ' ' + self.name)   
    #     if not is_last and level > 0:
    #         imple_list.append(level)
            
    #     while iterator.has_next():
    #         child = iterator.next()
    #         child_is_last = not iterator.has_next()
    #         child.draw(level + 1, child_is_last, imple_list)


