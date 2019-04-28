import unittest
from trie import TrieNode

class TestTrieNode(unittest.TestCase):

    def test_init(self):
        mynode = TrieNode()
        self.assertFalse(mynode.isend)

        othernode = TrieNode(True)
        self.assertTrue(othernode.isend)

    def test_set_isend(self):
        mynode = TrieNode()
        self.assertFalse(mynode.isend)
        mynode.set_isend()
        self.assertTrue(mynode.isend)
        mynode.set_isend(False)
        self.assertFalse(mynode.isend)
        mynode.set_isend(True)
        self.assertTrue(mynode.isend)
        mynode.set_isend()
        self.assertTrue(mynode.isend)

    def test_add_child(self):
        mynode = TrieNode()
        mynode.add_child(0)
        mynode.add_child('C')
        mynode.add_child('e')

        self.assertTrue(isinstance(mynode.children[0], TrieNode))
        self.assertTrue(isinstance(mynode.children[2], TrieNode))
        self.assertTrue(isinstance(mynode.children[4], TrieNode))
        self.assertEqual(mynode.children[1], None)
        self.assertEqual(mynode.children[3], None)

        savenode = mynode.children[2]
        mynode.add_child(2)
        self.assertEqual(savenode, mynode.children[2])

        with self.assertRaises(ValueError):
            mynode.add_child('ben')

if __name__ == "__main__":
    unittest.main()
