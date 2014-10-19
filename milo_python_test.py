import unittest
from milo_python_task import parse_date
import sys 


class ParseDateTest(unittest.TestCase):
    def test_parse_date(self):
        #only year check
        self.assertEqual(parse_date('2001'), '2001 is illegal')
        #only year and month check
        self.assertEqual(parse_date('2001/01'), '2001/01 is illegal')
        #standard date check
        self.assertEqual(parse_date('2001/02/03'), '2001-02-03')
        #short date check
        self.assertEqual(parse_date('01/02/03'), '2001-02-03')
        #reverse date check
        self.assertEqual(parse_date('03/02/2101'), '2101-02-03')
        #US standard date check
        self.assertEqual(parse_date('18/02/2010'), '2010-02-18')
        #illegal date check
        self.assertEqual(parse_date('35/02/2010'), '35/02/2010 is illegal')
        #leap year date check
        self.assertEqual(parse_date('2000/02/29'), ' 2000-02-29')
        #illegal leap year date check
        self.assertEqual(parse_date('2001/02/29'), '2001/02/29 is illegal')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ParseDateTest))
    unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite) 