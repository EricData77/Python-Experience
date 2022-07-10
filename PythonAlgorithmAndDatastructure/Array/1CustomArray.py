# Python Version
try:
    # Python 3
    from collections.abc import MutableSequence
except ImportError:
    # Python 2.7
    from collections import MutableSequence

class MyList(MutableSequence):
    def __init__(self, data = None):
        """
        Initialize the class
        """
        super(MyList, self).__init__()
        if(data):
            self._list = list(data)
        else:
            self._list = list()

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name, self._list)

    def __len__(self):
        return len(self._list)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.__class__(self._list[item])
        else:
            return self._list[item]

    def __delitem__(self, key):
        del self._list[key]

    def __setitem__(self, key, value):
        self._list[key] = value

    def __str__(self):
        return str(self._list)

    def insert(self, index, value):
        self._list.insert(index, value)

    def append(self, val):
        self.insert(len(self._list), val)

if __name__ == "__main__":
    foo = MyList([1, 2, 3, 4, 5])
    foo.append(6)
    print(foo)

    for idx, ii in enumerate(foo):
        print("MyList[%s] = %s" % (idx, ii))


