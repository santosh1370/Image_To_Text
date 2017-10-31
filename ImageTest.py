import unittest
from image import getimage,nonblank_lines

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'vinRead2.jpg')

class TestImage(unittest.TestCase):
    """
    Our basic test class
    """

    def test_image(self):
        """
        Check if the file exist or not
        """
        self.testdata = open(TESTDATA_FILENAME).read()



if __name__ == '__main__':
    unittest.main()