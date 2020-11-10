import unittest
import affine_cipher as ac

class TestStringMethods(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(ac.affine_cipher(19, 11), 'UTS')
        self.assertEqual(ac.affine_cipher(0, 0), 'ZZZ')

    def test_letters(self):
        with self.assertRaises(TypeError):
            ac.affine_cipher('ABC', 5)
        with self.assertRaises(TypeError):
            ac.affine_cipher(4, 'ABC')
        with self.assertRaises(TypeError):
            ac.affine_cipher(' ', 4)
        with self.assertRaises(TypeError):
            ac.affine_cipher(4, ' ')

if __name__ == '__main__':
    unittest.main()