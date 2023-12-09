#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_most_likely_ancestor_consensus(self):
        dna_string1 = 'GATATATGCATATACT'
        dna_string2 = 'ATAT'
        self.assertEqual(get_most_likely_ancestor_consensus(dna_string1, dna_string2), (2, 4, 10) )