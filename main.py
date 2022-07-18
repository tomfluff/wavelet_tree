import wavelet_tree

if __name__ == "__main__":
    text = "mississippi"
    wv_tree = wavelet_tree.WaveletTree(text)
    wv_tree.build_tree()
    print(wv_tree.access(3))
    print(wv_tree.symbol_code)
    print(wv_tree.rank('m',8))
    print(wv_tree.select('s',2))