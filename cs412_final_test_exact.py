import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.files import check_submitted_files
from io import StringIO
from unittest.mock import patch

from cs412_hw0_a import main as hw0_a_main
from cs412_hw0_b import main as hw0_b_main

class TestHW1(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.file_a_ok = False
        cls.file_b_ok = False
        cls.t0_in = """toot woof wa ow ow ow pa blub blub pa toot pa blub pa pa ow pow toot
5
dog goes woof
fish goes blub
elephant goes toot
seal goes ow
horse goes neigh
what does the fox say?"""
        cls.t0_exp = 'what the fox says: wa pa pa pa pa pa pow \nalso heard: elephant dog seal fish \n'
        
        cls.t1_in = """fox makes sounds
0
what does the fox say?"""
        cls.t1_exp = 'what the fox says: fox makes sounds \nalso heard: \n'


        cls.t2_in = """baba whoof fox makes baba sounds whoof night baba
3
dog goes whoof
sheep goes baba
lion goes roor
what does the fox say?"""
        cls.t2_exp = 'what the fox says: fox makes sounds night \nalso heard: sheep dog \n'

    @weight(0)
    @number("1.2")
    def test_01(self):
        """Check file cs412_hw0_a does not contain a dictionary"""

        dict_char = False
        with open('cs412_hw0_a.py') as f:
            if '{' in f.read():
                dict_char = True

        with open('cs412_hw0_a.py') as f:
            if 'dict()' in f.read():
                dict_char = True

        self.assertEqual(False, dict_char, 
                          'Appears that a dictionary is used in cs412_hw0_a.py')
        
        # test OK, set status to good/true
        TestHW1.file_a_ok = True

    @weight(0)
    @number("1.3")
    def test_02(self):
        """Check file cs412_hw0_b does contain a dictionary"""

        dict_char = False
        with open('cs412_hw0_b.py') as f:
            if '{' in f.read():
                dict_char = True
                
        with open('cs412_hw0_b.py') as f:                
            if 'dict()' in f.read():
                dict_char = True

        self.assertEqual(True, dict_char, 
                          'Appears that a dictionary is NOT used in cs412_hw0_b.py')
        
        # test OK, set status to good                  
        TestHW1.file_b_ok = True

    
    @weight(1)
    @number("1.4")
    @patch('sys.stdout', new_callable=StringIO)
    def test_03(self, mock_out):
        """Case 0 from write up on hw0_a"""
        self.assertEqual(True, TestHW1.file_a_ok, "File A test skipped because of dictionary detected")

        with patch('sys.stdin', new = StringIO(self.t0_in)):
            hw0_a_main()
        self.assertEqual(mock_out.getvalue(), self.t0_exp)

    
    
    @weight(1)
    @number("1.5")
    @patch('sys.stdout', new_callable=StringIO)
    def test_04(self, mock_out):
        """Case 0 from write up on hw0_b"""
        self.assertEqual(True, TestHW1.file_b_ok,  "File B test skipped because no dictionary detected")

        with patch('sys.stdin', new = StringIO(self.t0_in)):
            hw0_b_main()
        self.assertEqual(mock_out.getvalue(), self.t0_exp)
