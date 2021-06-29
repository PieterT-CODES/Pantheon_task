import unittest
import xmlrunner
import ugen
import argparse
import sys

class MyTest(unittest.TestCase): 
    def test_generate_username(self):   
        self.assertEqual(ugen.generate_list_of_usernames("input_file1.txt"), ['jmhurban','mrstefan','jmurgas'])
        self.assertEqual(ugen.generate_list_of_usernames("input_file2.txt"), ['phufnage','phufnage1'])
        self.assertEqual(ugen.generate_list_of_usernames("input_file3.txt"), [])

if __name__ == '__main__':  
    unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output='REPORT_XML'), #The output is an automatically generated report.
    failfast=False, buffer=False, catchbreak=False)    




              