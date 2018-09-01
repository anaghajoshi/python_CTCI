"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2blc5a3.
If the "compressed"string would not become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).
"""

import unittest


def string_compression(in_string):
    char_counter = 0
    comp_str = ''
    for i in range(len(in_string)):
        char_counter += 1
        if i+1 >= len(in_string) or in_string[i] != in_string[i+1]:
            comp_str = comp_str + in_string[i]
            comp_str = comp_str + str(char_counter)
            char_counter = 0
    print(comp_str)
    if len(comp_str) < len(in_string):
        return comp_str
    else:
        return comp_str

class MyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(string_compression("aaabb"), "a3b2")

    def test_1(self):
        self.assertEqual(string_compression("ab"), "a1b1")
