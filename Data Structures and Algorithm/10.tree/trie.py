class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        print("successfully inserted")

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if currentNode.endOfString == True:
            return True
        else:
            return False


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False
    # case 1 - some other prefix of strings is same as the\
    # one that we wnt to delete
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    # case 2  - the string is a prefix of some other string
    if index == len(word)-1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    # case 3 - other string is prefix of this string
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    # case 4 - not any node depends on this string
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
newTrie.insertString("Box")
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))
