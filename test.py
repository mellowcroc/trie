from trie import Trie, Node

def test_trie():
    root = Node()
    trie = Trie(root)
    trie.insert(root, ["D", "O", "G"], "1")
    trie.insert(root, ["C", "A", "T"], "2")
    trie.insert(root, ["D", "O", "G", "E"], "3")
    trie.insert(root, ["C", "A", "N", "A", "P", "E"], "4")
    trie.print(root)
    print("look up")
    print(trie.look_up(root, ["D", "O", "G"]))
    print(trie.look_up(root, ["C", "A", "T"]))
    print(trie.look_up(root, ["D", "O", "G", "E"]))
    print(trie.look_up(root, ["C", "A", "N", "A", "P", "E"]))

if __name__ == "__main__":
    test_trie()