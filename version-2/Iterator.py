# 迭代器模式

# 声明迭代器接口
class Iterator:
    def get_element(self):
        pass

    def next(self):
        pass
    
    def has_next(self):
        pass

# 声明集合接口(不同迭代方式)
class IterableCollection:
    def create_iterator(self):
        pass

# 实现具体迭代器类（list）
class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0
    
    def get_element(self):
        return self._collection[self._index]
    
    def next(self):
        if self.has_next():
            self._index += 1
        else:
            raise StopIteration
    
    def has_next(self):
        return self._index < len(self._collection) 