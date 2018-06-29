#!/usr/bin/python3

import unittest
import hamming

class TestHamming(unittest.TestCase):
    
    def test_matches(self):
        self.assertEqual(hamming.hammingDistance("GTAC", "GGAC"), 1)
        self.assertEqual(hamming.hammingDistance("GGACGAACAGTCTAGCG", "GTACGATCAGCCTGGCG"), 4)
        self.assertEqual(hamming.hammingDistance("GGGGATCCCGGGTATAGACC", "GCGGAACTCGGTCGTAAGCA"), 9)
        
    def test_no_matches(self):
        self.assertEqual(hamming.hammingDistance("GGGGATCCCGGGTATAGACC", "GGGGATCCCGGGTATAGACC"), 0)
    
    def test_length_mismatch(self):
        self.assertEqual(hamming.hammingDistance("GGATCATAG", "GATCTG"), -1)
        
        
        
        
if __name__ == "__main__":
    unittest.main()
