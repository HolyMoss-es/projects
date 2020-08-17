
import unittest
import bowling


class BowlingTest(unittest.TestCase):

    def test_normal(self):
        x = bowling.ScoreGetter(res='Х4/34-4')
        result = x.run()
        self.assertEqual(result, 46)

    def test_x(self):
        x = bowling.ScoreGetter(res='xXхХxXхХхХ')
        result = x.run()
        self.assertEqual(result, 200)

    def test_symbols(self):
        x = bowling.ScoreGetter(res='1/2--3')
        result = x.run()
        self.assertEqual(result, 20)

    def test_last_x(self):
        x = bowling.ScoreGetter(res='121212x')
        result = x.run()
        self.assertEqual(result, 29)

    def test_xs(self):
        with self.assertRaises(bowling.TooManyXs):
            x = bowling.ScoreGetter(res='xxxxxxxxxx12')
            x.run()

    def test_len(self):
        with self.assertRaises(bowling.LenError):
            x = bowling.ScoreGetter(res='1212121212121212121212')
            x.run()

    def test_invalid_frame_size(self):
        with self.assertRaises(bowling.InputError):
            x = bowling.ScoreGetter(res='1')
            x.run()

    def test_type(self):
        with self.assertRaises(TypeError):
            x = bowling.ScoreGetter(res=True)
            x.run()

    def test_frame_score(self):
        with self.assertRaises(bowling.InvalidFrame):
            x = bowling.ScoreGetter(res='99')
            x.run()
