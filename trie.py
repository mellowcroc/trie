


class Node:
    def __init__(self):
        self.children = {}
        self.value = None

    def __str__(self):
        s = "\nnode value:" + str(self.value)
        for key in self.children.keys():
            s += ", key: " + key
        return s


class Trie:
    def __init__(self, root):
        self.root = root
    
    def insert(self, node, key, value):
        if node == None:
            return self.insert(Node(), key, value)

        if len(key) == 0:
            node.value = value
            return node

        if key[0] not in node.children:
            node.children[key[0]] = None
        node.children[key[0]] = self.insert(node.children[key[0]], key[1:], value)
        return node

    def look_up(self, node, key):
        if node == None:
            return None

        if len(key) == 0:
            return node.value

        return self.look_up(node.children[key[0]], key[1:])

    def traverse(self, node, s):
        s += str(node)
        for key in node.children.keys():
            s = self.traverse(node.children[key], s)
        return s

    def print(self, node):
        s = "children= ["
        s += self.traverse(node, s)
        s += "\n]. END"
        print(s)