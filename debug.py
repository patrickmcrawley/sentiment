import unittest
import pandas as pd
import data1 as d1

def test_dataframe():
    """Returns a pandas dataframe object to use in our tests. Our tests will compare dataframes to it to make sure
    that our functions return dataframe objects. """
    # initialize list of lists
    data = [['tom', 10], ['nick', 15], ['juli', 14]]
    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Name', 'Age'])
    return type(df)


class TestGetData(unittest.TestCase):
    """Test our functions from data1.py to ensure that they properly return pandas dataframes when called."""
    def test_get_cons(self):
        self.assertEqual(type(d1.get_cons()), test_dataframe())
    def test_get_sentiment(self):
        self.assertEqual(type(d1.get_sentiment()), test_dataframe())
    def test_get_unemployment(self):
        self.assertEqual(type(d1.get_unemployment()), test_dataframe())
if __name__ == '__main__':
    unittest.main()


