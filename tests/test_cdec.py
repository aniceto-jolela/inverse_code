import unittest
from .test_convert_dec import TestConvertDecimal


def suite():
    """@NOTE: return all tests"""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestConvertDecimal("cdec_octal"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
