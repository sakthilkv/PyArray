class PyArray:

    def __init__(self,datatype,length):
        self.datatype = datatype
        self.length = length
        self._items = []
        
    def _check_datatype(self,item):
        if not isinstance(item, self.datatype):
            raise TypeError(f"Expected item of type {self.datatype.__name__}, got {type(item).__name__}")

    def append(self,item):
        if len(self._items) >= self.length:
            raise OverflowError("Array capacity exceeded")
        self._check_datatype(item)
        self._items.append(item)

    def __repr__(self):
        return repr(self._items)
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]

