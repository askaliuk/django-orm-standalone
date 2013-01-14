import unittest


class TestModelAccess(unittest.TestCase):

    def test_data_access(self):
        """Import data module and try to retrieve data from TestModel."""
        try:
            from data import TestModel
        except ImportError:
            self.fail("data module import failed")

        testObject = TestModel.objects.filter(id=1)
        self.assertEqual(0, len(testObject))


if __name__ == '__main__':
    unittest.main()
