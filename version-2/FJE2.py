import argparse
import json
import Icon_factory
import tree_factory
import rectangle_factory
from Visitor import DrawVisitor

class FunnyJsonExplorer:
    def __init__(self, style, icon_family, config_file='icon_config.json'):
        self.load_config(config_file)

        if style == 'tree':
            self.style_factory = tree_factory.TreeFactory()
        elif style == 'rectangle':
            self.style_factory = rectangle_factory.RectangleFactory()
        else:
            raise ValueError('Unsupported style')

        if icon_family in self.icon_families:
            icons = self.icon_families[icon_family]
            self.icon_factory = Icon_factory.IconFactory(icons)
        else:
            raise ValueError('Unsupported icon family')

    def load_config(self, config_file):
        with open(config_file, 'r', encoding='utf-8') as file:
            config = json.load(file)
        self.icon_families = config['icon_families']

    def load_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def build_structure(self, data, name="root"):
        if isinstance(data, dict):
            container = self.style_factory.create_container(name, self.icon_factory)
            for key, value in data.items():
                child = self.build_structure(value, key)
                container.add(child)
            return container
        elif isinstance(data, list):
            container = self.style_factory.create_container(name, self.icon_factory)
            for index, value in enumerate(data):
                child = self.build_structure(value, str(index))
                container.add(child)
            return container
        else:
            return self.style_factory.create_leaf(name, data, self.icon_factory)

    def draw_structure(self, root):
        visitor = DrawVisitor()
        root.accept(visitor)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', type=str, required=True, help='JSON file to visualize')
    parser.add_argument('-s', '--style', type=str, required=True, help='Style of visualization')
    parser.add_argument('-i', '--icon', type=str, required=True, help='Icon family for visualization')
    args = parser.parse_args()

    fje = FunnyJsonExplorer(style=args.style, icon_family=args.icon)
    data = fje.load_json(args.file)
    structure = fje.build_structure(data)
    fje.draw_structure(structure)



# if __name__ == '__main__':
#     # fje = FunnyJsonExplorer(style='tree', icon_family='icon_B')
#     # fje = FunnyJsonExplorer(style='tree', icon_family='icon_A')
#     # fje = FunnyJsonExplorer(style='rectangle', icon_family='icon_A')
#     fje = FunnyJsonExplorer(style='rectangle', icon_family='icon_C')
#     data = fje.load_json('example.json')
#     structure = fje.build_structure(data)
#     fje.draw_structure(structure)
#     # data = fje.load('src/test.json')
