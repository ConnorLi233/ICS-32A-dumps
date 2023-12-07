# project4test.py
#
# ICS 32A Fall 2023
# Project 4: The Fall of the World's Own Optimist (Part 1)

import unittest
from faller import Faller

class TestFaller(unittest.TestCase):
    def setUp(self):
        self._game_state = [
            ['   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   '],
            ['   ', '   ', '   ', '   ']
        ]

    def test_new_drop(self):
        faller = Faller(self._game_state, 1, 'X', 'Y', 'Z')
        self.assertEqual(faller.new_drop(), [
            ['   ', '[X]', '   ', '   '],
            ['   ', '[Y]', '   ', '   '],
            ['   ', '[Z]', '   ', '   '],
            ['   ', '   ', '   ', '   ']
        ])


    def test_drop(self):
        faller = Faller(self._game_state, 1, 'X', 'Y', 'Z')
        self.assertEqual(faller.drop(2), [
            ['   ', '   ', '   ', '   '],
            ['   ', '|X|', '   ', '   '],
            ['   ', '|Y|', '   ', '   '],
            ['   ', '|Z|', '   ', '   ']
        ])

    def test_freeze(self):
        faller = Faller(self._game_state, 1, 'X', 'Y', 'Z')
        self.assertEqual(faller.freeze(2), [
            ['   ', '   ', '   ', '   '],
            ['   ', ' X ', '   ', '   '],
            ['   ', ' Y ', '   ', '   '],
            ['   ', ' Z ', '   ', '   ']
        ])

    def test_return_column(self):
        faller = Faller(self._game_state, 3, 'X', 'Y', 'Z')
        self.assertEqual(faller.return_column(), 3)

if __name__ == '__main__':
    unittest.main()