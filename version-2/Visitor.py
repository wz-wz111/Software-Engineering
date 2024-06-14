
width = 50
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
