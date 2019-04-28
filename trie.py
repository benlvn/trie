class TrieNode:

    def __init__(self, isend=False):
        self.children = [None]*26
        self.isend = isend

    def set_isend(self, val=True):
        self.isend= val

    def add_child(self, nextnode, isend=False):
        ind = None
        if isinstance(nextnode, int) and 0 <= nextnode < 26:
            ind = nextnode
        elif isinstance(nextnode, str) and len(nextnode) == 1:
            if 'A' <= nextnode and nextnode <= 'Z':
                ind = ord(nextnode) - ord('A')
            elif 'a' <= nextnode and nextnode <= 'z':
                ind = ord(nextnode) - ord('a')
            else:
                raise ValueError('Child must be 0-25/A-z')
        else:
            raise ValueError('Child must be 0-25/A-z')
        if self.children[ind] == None:
            self.children[ind] = TrieNode(isend)
        

class Trie:

    def __init__(self, filename=None):
        self.base_node = TrieNode()
        if filename != None:
            with open(filename) as f:
                words = f.read().split('\n')[:-1] 
                for word in words:
                    self.add_word(word.strip())

    def add_word(self, word):
        tcrawl = self.base_node
        for c in word:
            if tcrawl.children[ord(c) - ord('a')] == None:
                tcrawl.add_child(c)
            tcrawl = tcrawl.children[ord(c) - ord('a')]
        tcrawl.set_isend()

    def check_for_word(self, word):
        tcrawl = self.base_node
        for c in word:
            if tcrawl.children[ord(c) - ord('a')] == None:
                return False
            tcrawl = tcrawl.children[ord(c) - ord('a')]
        return tcrawl.isend
        

    def get_base_node(self):
        return self.base_node

if __name__ == "__main__":
    print(help(Trie))
