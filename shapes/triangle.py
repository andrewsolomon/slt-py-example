#!/usr/bin/env python

"""
Author: Andrew Solomon
File: traingle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

import itertools
import math
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and is created with three edge length arguments
    """

    def __init__(self, a, b, c):
        self.edges = [a, b, c]

    @property
    def edges(self):
        """
        return the list of edge lengths
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """
        Check that the triangle inequality condition is satisfied.
        In detail, we're checking that
            a + b >= c, a + c >= b and b + c >= a
        and if p is the perimeter this is equivalent to:
            2(a + b) >= p, 2(a + c) >=p and 2(b + c) >= p

        NOTE: a + b == c are legitimate parameters for a
        degenerate triangle.
        """
        perimeter = sum(edges)
        for pair in itertools.combinations(edges, 2):
            if 2 * sum(pair) < perimeter:
                raise ValueError(
                    f"The edges {edges} fail the triangle inequality condition"
                )
        self._edges = edges  # pylint: disable=attribute-defined-outside-init

    def area(self):
        """
        Compute the area using Heron's formula:
            sqrt(s * (s - a) * (s - b) * (s - c))
        where s is half of the perimeter
        """
        semip = self.perimeter() / 2
        return math.sqrt(semip * math.prod(semip - x for x in self.edges))

    def perimeter(self):
        """
        Compute the perimeter using the formula (length + width) * 2
        """
        return sum(self.edges)

    def is_equilateral(self):
        """
        Return true if and only if all sides are of equal length
        """
        return max(self.edges) == min(self.edges)
