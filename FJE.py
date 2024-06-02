import argparse
import json
import Icon_factory
import tree_factory
import rectangle_factory

# 建造者模式（客户端）
# 功能：用于构建一个对象FunnyJsonExplorer，这个对象由两部分组成：StyleFactory和IconFactory
#       StyleFactory用于构建容器和叶子节点，IconFactory用于构建图标


class FunnyJsonExplorer:
    def __init__(self, style, icon_family, config_file='icon_config.json'):
        self.load_config(config_file)

        # 选择不同的style_factory
        if style == 'tree':
            self.style_factory = tree_factory.TreeFactory()
        elif style == 'rectangle':
            self.style_factory = rectangle_factory.RectangleFactory()
        else:
            raise ValueError('Unsupported style')
        
        # 选择不同的icon_factory
        if icon_family in self.icon_families:
            icons = self.icon_families[icon_family]
            self.icon_factory = Icon_factory.IconFactory(icons)
        else:
            raise ValueError('Unsupported icon family')

    def load_config(self, config_file):
        with open(config_file, 'r', encoding='utf-8') as file:
            config = json.load(file)
        self.icon_families = config['icon_families']

    def load(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
        return data

    def show(self, data):
        root = self.create_container('root', data)
        root.draw()

    def create_container(self, name, data):
        container = self.style_factory.create_container(name, self.icon_factory)
        for key, value in data.items():
            if isinstance(value, dict):
                # 递归创建容器
                child_container = self.create_container(key, value)
                container.add(child_container)
            else:
                # 创建叶子节点
                leaf = self.style_factory.create_leaf(key, value, self.icon_factory)
                container.add(leaf)
        return container


# def main():
#     parser = argparse.ArgumentParser(description='Funny JSON Explorer')
#     parser.add_argument('-f', '--file', type=str, required=True, help='JSON file to visualize')
#     parser.add_argument('-s', '--style', type=str, required=True, help='Style of visualization')
#     parser.add_argument('-i', '--icon', type=str, required=True, help='Icon family for visualization')
#     args = parser.parse_args()

#     fje = FunnyJsonExplorer(style=args.style, icon_family=args.icon)
#     data = fje.load(args.file)
#     fje.show(data)

# if __name__ == '__main__':
#     main()

if __name__ == '__main__':
    fje = FunnyJsonExplorer(style='tree', icon_family='icon_B')
    # fje = FunnyJsonExplorer(style='rectangle', icon_family='icon_A')
    # fje = FunnyJsonExplorer(style='rectangle', icon_family='icon_C')
    data = fje.load('example.json')
    # data = fje.load('src/test.json')
    fje.show(data)