import math


DEBUG = False


class BitVector():
    """
    Simple (slow) implementation of a Bit Vector.
    """
    def __init__(self, bits) -> None:
        self.bits = bits
        self.length = len(bits)
    
    def rank(self, bit, index):
        assert index < self.length
        assert bit == 0 or bit == 1

        _rank = 0
        for i in range(index):
            if self.bits[i] == bit:
                _rank += 1
        return _rank
    
    def select(self, bit, index):
        assert index < self.length
        assert bit == 0 or bit == 1

        _rank = 0
        for i in range(self.length):
            if self.bits[i] == bit:
                _rank += 1
            if _rank == index+1:
                return i
        raise Exception(f"Bit Vector out of bounds.")
    
    def access(self, index):
        assert index < self.length
        
        return self.bits[index]


class WaveletNode():
    def __init__(self, bits, parent, left, right, sign, label=None) -> None:
        self.BV = BitVector(bits)
        self.parent = parent
        self.left = left
        self.right = right
        self.sign = sign
        self.label = label
    
    def is_leaf(self):
        return self.label != None
    
    def is_root(self):
        return self.parent == None


class WaveletTree():
    def __init__(self, text:str) -> None:
        self.text = text.strip()
        self.root = None
        self.symbol_code = {}

    def rank(self, symbol, index):
        assert self.root != None
        
        node = self.root
        _k = 0
        while not node.is_leaf():
            _B = node.BV
            _b = self.symbol_code[symbol][_k]
            if _b == 0:
                node = node.left
            else:
                node = node.right
            index = _B.rank(_b,index)
            _k += 1
        return index

    
    def select(self, symbol, index):
        assert self.root != None
        
        node = self.root
        for d in self.symbol_code[symbol]:
            if d == 0:
                node = node.left
            else:
                node = node.right
        assert node.is_leaf()

        _k = len(self.symbol_code[symbol]) - 1
        while not node.is_root():
            node = node.parent
            _B = node.BV
            _b = self.symbol_code[symbol][_k]
            index = _B.select(_b, index)
            _k -= 1
        return index

    def access(self, index):
        assert self.root != None
        node = self.root

        while not node.is_leaf():
            _B = node.BV
            _b = _B.access(index)
            if _b == 0:
                node = node.left
            else:
                node = node.right
            index = _B.rank(_b,index)
        return node.label

    def __get_symbols(self,text:str):
        symbols = []
        for _c in text:
            if _c not in symbols:
                symbols.append(_c)
        return symbols
    
    def __build_recursive(self, text:str, parent:WaveletNode, sign):        
        symbols = self.__get_symbols(text)

        if len(symbols) < 1:
            return None
        if len(symbols) == 1:
            if DEBUG: print(f"-> Leaf: sign={sign}, label='{symbols[0]}'")
            _p = parent
            _code = [sign]
            while _p.parent != None:
                _code.insert(0,_p.sign)
                _p = _p.parent
            self.symbol_code[symbols[0]] = _code
            return WaveletNode([],parent,None,None,sign,symbols[0])

        symbols_left = symbols[:math.floor(len(symbols)/2)]
        symbols_right = symbols[math.floor(len(symbols)/2):]

        text_left = ""
        text_right = ""
        bits = []

        for _c in text:
            if _c in symbols_left:
                bits.append(0)
                text_left += _c
            if _c in symbols_right:
                bits.append(1)
                text_right += _c
        
        node = WaveletNode(bits, parent,None,None,sign)
        if DEBUG: print(f"> Node: bits={bits}, symbols={symbols}, sign={sign}")
        if DEBUG: print(">> Left:")
        node.left = self.__build_recursive(text_left,node,0)
        if DEBUG: print(">> Right:")
        node.right = self.__build_recursive(text_right,node,1)
        return node

    def build_tree(self):
        assert self.root == None
        assert len(self.text) > 0

        self.root = self.__build_recursive(self.text,None,-1)