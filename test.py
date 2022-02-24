from trie import Trie, Node

def test_trie():
    root = Node()
    trie = Trie(root)
    trie.insert(root, ["D", "O", "G"], "1")
    trie.insert(root, ["C", "A", "T"], "2")
    trie.insert(root, ["D", "O", "G", "E"], "3")
    trie.insert(root, ["C", "A", "N", "A", "P", "E"], "4")
    assert trie.look_up(root, ["D", "O", "G"]) == "1"
    assert trie.look_up(root, ["C", "A", "T"]) == "2"
    assert trie.look_up(root, ["D", "O", "G", "E"]) == "3"
    assert trie.look_up(root, ["C", "A", "N", "A", "P", "E"]) == "4"
    print("passed all tests")

if __name__ == "__main__":
    test_trie()