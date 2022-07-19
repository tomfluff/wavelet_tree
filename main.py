import wavelet_tree

if __name__ == "__main__":
    text = "mississippi"

    wv_tree = wavelet_tree.WaveletTree(text)
    wv_tree.build_tree()

    print(f"Access: i=3 -> \'{wv_tree.access(3)}\' [should be: \'s\']")
    print(f"Rank: s=s, i=5 -> {wv_tree.rank('s',5)} [should be: 2]")
    print(f"Select: s=s, i=2 -> {wv_tree.select('s',2)} [should be: 5]")

    print("---")

    text = "when you want to be a friend it is time to hold your hands"

    wv_tree = wavelet_tree.WaveletTree(text)
    wv_tree.build_tree()

    print(f"Access: i=3 -> \'{wv_tree.access(3)}\' [should be: \'n\']")
    print(f"Rank: s=w, i=9 -> {wv_tree.rank('w',9)} [should be: 1]")
    print(f"Select: s=h, i=1 -> {wv_tree.select('h',1)} [should be: 43]")