import unittest
from main import check_similarity

class TestCreateVocab(unittest.TestCase):
  def check_similarity_tests_correct(self):
    # Test check_similarity function when the answer is a full match to the correct answer
    self.assertEqual(check_similarity("hola", "hola"), "Correct!")
    self.assertEqual(check_similarity("hello", "hello"), "Correct!")
    self.assertEqual(check_similarity("adios", "Adiós."), "Correct!")
    self.assertEqual(check_similarity("acostarse (ue)", "acostarse"), "Correct!")
    pass

  def check_similarity_tests_incorrect(self):
    # Test case 2 code here
    pass

  def test_case3(self):
    # Test case 3 code here
    pass

if __name__ == '__main__':
  unittest.main()

