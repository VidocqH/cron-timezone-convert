import unittest
from crontzconvert import convert

class TestTransformer(unittest.TestCase):
    def test_no_time_difference(self):
        self.assertEqual(convert('1 17 * 4 *', 'Asia/Shanghai', 'Asia/Shanghai'), '1 17 * 4 *')

    def test_gmt8_gmt(self):
        self.assertEqual(convert('1 17 * 4 *', 'Asia/Shanghai', 'UTC'), '1 9 * 4 *')

    def test_all_star(self):
        self.assertEqual(convert('* * * * *', 'Asia/Shanghai', 'UTC'), '* * * * *')

    def test_range(self):
        self.assertEqual(convert('1 2-4 * * *', 'Asia/Shanghai', 'UTC'), '1 18-20 * * *')
    
    def test_overlap_range(self):
        self.assertEqual(convert('1 0-4,2-5 * 1 *', 'Asia/Shanghai', 'UTC'), '1 16-21 * 1 *')

    def test_gmt_gmt8(self):
        self.assertEqual(convert('* 20-22 * * *', 'UTC', 'Asia/Shanghai'), '* 4-6 * * *')

    def test_slash_unchange(self):
        self.assertEqual(convert('* 0-4,2-5/15 * * *', 'Asia/Shanghai', 'UTC'), '* 16-21/15 * * *')

    # TODO
    def test_gmt8_gmt_back_day(self):
        self.assertEqual(convert('* 0 2 * 2', 'Asia/Shanghai', 'UTC'), '* 16 1 * 1')

    def test_gmt_gmt8_next_day(self):
        self.assertEqual(convert('* 16 1 * 1', 'UTC', 'Asia/Shanghai'), '* 0 2 * 2')

    # TODO week case

if __name__ == '__main__':
    unittest.main()