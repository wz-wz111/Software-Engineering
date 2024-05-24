import argparse
import json
import Icon_factory 
import Container

# 建造者模式（客户端）
class FunnyJsonExplorer:
    def __init__(self, style, icon_family, config_file='icon_config.json'):
        self.load_config(config_file)
        
        if style == 'tree':
            self.container_class = Container.TreeContainer
            self.leaf_class = Container.Tree_Leaf
        elif style == 'rectangle':
            self.container_class = Container.RectangleContainer
            self.leaf_class = Container.Rec_Leaf
        else:
            raise ValueError('Unsupported style')
        
        if icon_family in self.icon_families:
            icons = self.icon_families[icon_family]
            self.icon_factory = Icon_factory.ConfigurableIconFactory(icons)
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
        # 调用容器的draw方法
        root.draw()

    def create_container(self, name, data):
        container = self.container_class(name, self.icon_factory)
        for key, value in data.items():
            if isinstance(value, dict):
                child_container = self.create_container(key, value)
                container.add(child_container)
            else:
                leaf = self.leaf_class(key, value, self.icon_factory)
                container.add(leaf)
        return container


def main():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', type=str, required=True, help='JSON file to visualize')
    parser.add_argument('-s', '--style', type=str, required=True, help='Style of visualization')
    parser.add_argument('-i', '--icon', type=str, required=True, help='Icon family for visualization')
    args = parser.parse_args()

    fje = FunnyJsonExplorer(style=args.style, icon_family=args.icon)
    data = fje.load(args.file)
    fje.show(data)

if __name__ == '__main__':
    main()

# if __name__ == '__main__':
#     # fje = FunnyJsonExplorer(style='tree', icon_family='icon_B')
#     # fje = FunnyJsonExplorer(style='rectangle', icon_family='icon_A')
#     fje = FunnyJsonExplorer(style='rectangle', icon_family='icon_C')
#     data = fje.load('example.json')
#     # data = fje.load('src/test.json')
#     fje.show(data)