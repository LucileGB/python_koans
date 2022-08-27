#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    """
    First, we check that the triangle is valid (all sides are over 0 and
    the sum of any two sides is superior to the remaining one).
    Then, we return an adjective qualifying the triangle's nature.
    """
    sides = [a, b, c]

    for side in sides:
        if side < 1:
            raise TriangleError

        if (sum(sides) - side) <= side:
            raise TriangleError

    unique_sides = len(set(sides))

    if unique_sides == 1:
        return 'equilateral'
    
    if unique_sides == 2:
        return 'isosceles'

    else:
        return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
