"""
Author: Andrew Solomon
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.rightangle1 = Triangle(3, 4, 5)
        self.rightangle2 = Triangle(5, 3, 4)
        self.equilateral = Triangle(4, 4, 4)
        self.isoceles1 = Triangle(5, 5, 8)
        self.isoceles2 = Triangle(1, 1, 1.6)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.rightangle1.area(), 6, msg="rightangle area")
        self.assertEqual(
            self.rightangle2.area(), 6, msg="reordered rightangle area"
        )
        self.assertEqual(self.isoceles1.area(), 12, msg="integer isocles area")
        self.assertAlmostEqual(
            self.isoceles2.area(),
            0.48,
            places=6,
            msg="floating point isoceles area",
        )

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(
            self.rightangle1.perimeter(), 12, msg="rightangle perimeter"
        )
        self.assertEqual(
            self.rightangle2.perimeter(),
            12,
            msg="reordered rightangle perimeter",
        )
        self.assertEqual(
            self.equilateral.perimeter(), 12, msg="equilateral perimeter"
        )
        self.assertEqual(
            self.isoceles1.perimeter(), 18, msg="integer isoceles perimeter"
        )
        self.assertEqual(
            self.isoceles2.perimeter(), 3.6, msg="floating point isoceles area"
        )

    def test_equilateral(self):
        """
        Compare the test equilateral with the actual values
        """
        self.assertTrue(
            self.equilateral.is_equilateral(), msg="equilateral triangle"
        )
        self.assertFalse(
            self.rightangle1.is_equilateral(), msg="non-equilateral triangle"
        )

    def test_exceptions(self):
        """
        Ensure that exceptions are raised on invalid parameters
        """
        # fmt: off
        with self.assertRaises(TypeError, msg="triangle should not have more than 3 edges"):
            Triangle(3, 4, 5, 6)  # pylint: disable=too-many-function-args

        # fmt: off
        with self.assertRaises(TypeError, msg="triangle should not have fewer than 3 edges"):
            Triangle(3, 4)  # pylint: disable=no-value-for-parameter

        # fmt: off
        with self.assertRaises(ValueError, msg="edge lengths must fit the triangle inequality"):
            Triangle(3, 4, 100)
