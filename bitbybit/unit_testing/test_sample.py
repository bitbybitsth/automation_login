import unittest
from unit_testing.sample_funtion import get_data


class SampleTestCase(unittest.TestCase):

    def test_get_data(self):
        self.assertEqual(get_data("pankaj", "gosavi", "pankagosavi1029@gmail.com"),
                         ("pankaj","gosavi","pankajgosavi1029@gmail.com"))
        self.assertEqual(get_data("pankaj", "gosavi", "pankagosavi1029@gmail.com", bg="o+"),
                         ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "o+"))
        self.assertNotEqual(get_data("pankaj", "gosavi", "pankagosavi1029@gmail.com", bg="o+"),
                         ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "a+"))
        self.assertEqual(get_data("pankaj", "gosavi", "pankagosavi1029@gmail.com", ph="9766588937"),
                         ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "9766588937"))
        self.assertEqual(get_data("pankaj", "gosavi", "pankagosavi1029@gmail.com", add="solapur"),
                         ("pankaj","gosavi","pankajgosavi1029@gmail.com","solapur"))
        self.assertEqual(get_data("pankaj", "gosavi", "pankagosavi1029@gmail.com", ph="9766588937", add="solapur"),
                         ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "solapur", "9766588937"))
        self.assertEqual(get_data("pankaj", "gosavi", "pankagosavi1029@gmail.com", ph="9766588937", bg="o+"),
                         ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "o+", "9766588937"))
        self.assertEqual(get_data("pankaj", "gosavi", "pankagosavi1029@gmail.com", bg="o+", add="solapur"),
                         ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "solapur", "o+"))
        self.assertEqual(get_data("pankaj", "gosavi", "pankagosavi1029@gmail.com", ph="9766588937", add="solapur", bg="o+"),
                         ("pankaj", "gosavi", "pankajgosavi1029@gmail.com", "solapur", "o+", "9766588937"))



if __name__ == '__main__':
    unittest.main()
