import unittest
from unit_testing.sample_funtion import get_data


class TestSample2(unittest.TestCase):

    def test_get_data(self):
        self.assertEqual(get_data(name="pankaj", last="goavi", email="jj@gmail.com"),
                         ("pankaj","gosavi","pankajgosavi1029@gmail.com"))
        self.assertEqual(get_data(name="pankaj", last="goavi", email="jj@gmail.com", bg="o+"),
                         ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "o+"))
        self.assertEqual(
            get_data(name="pankaj", last="goavi", email="jj@gmail.com",add="solapur"),
            ("pankaj", "gosavi", "pankajgosavi1029@gmail.com","solapur")
        )
        self.assertEqual(
            get_data(name="pankaj", last="goavi", email="jj@gmail.com", ph="solapur"),
            ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "9766588937")
        )
        self.assertEqual(
            get_data(name="pankaj", last="goavi", email="jj@gmail.com", add="solapur", ph="9766"),
            ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "solapur", "9766588937")
        )
        self.assertEqual(
            get_data(name="pankaj", last="goavi", email="jj@gmail.com", add="solapur", bg="o+"),
            ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "solapur","o+")
        )
        self.assertEqual(
            get_data(name="pankaj", last="goavi", email="jj@gmail.com", ph="9766588", bg="o"),
            ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "o+", "9766588937")
        )
        self.assertEqual(
            get_data(name="pankaj", last="goavi", email="jj@gmail.com", add="solapur", ph="9766", bg="o+"),
            ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "solapur", "o+", "9766588937")
        )




if __name__ == '__main__':
    unittest.main()
