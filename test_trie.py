import unittest
from trie import Trie, TrieNode

class TestModule(unittest.TestCase):

    def test_init(self):
        t1 = Trie()
        base1 = t1.get_base_node()
        self.assertFalse(base1.isend)

        t2 = Trie('testfile1.txt')
        # contains python, javascript, java
        base2 = t2.get_base_node()
        self.assertFalse(base2.isend)
        self.assertEqual(base2.children[3], None)
        self.assertTrue(isinstance(base2.children[ord('j')-ord('a')], TrieNode))
        self.assertTrue(isinstance(base2.children[ord('p')-ord('a')], TrieNode))
    
    def test_add_word(self):
        t1 = Trie()
        t1.add_word('bennett')
        t1.add_word('levine')
        t1.add_word('ben')
        t1.add_word('')

        self.assertTrue(t1.get_base_node().isend)
        self.assertTrue(isinstance(t1.get_base_node().children[ord('b')-ord('a')], TrieNode))
        self.assertTrue(isinstance(t1.get_base_node().children[ord('l')-ord('a')], TrieNode))

    def test_check_for_word(self):
        t1 = Trie('testfile1.txt')
        self.assertTrue(t1.check_for_word('python'))
        self.assertTrue(t1.check_for_word('java'))
        self.assertTrue(t1.check_for_word('javascript'))
        self.assertFalse(t1.check_for_word('apple'))
        t1.add_word('apple')
        self.assertTrue(t1.check_for_word('apple'))
        self.assertFalse(t1.check_for_word(''))
        t1.add_word('')
        self.assertTrue(t1.check_for_word(''))

if __name__ == "__main__":
    unittest.main()
