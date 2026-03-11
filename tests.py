"""
John Maynard
CSCI 332 Spring 2025
Programming Assignment #class18
I acknowledge that I have worked on this assignment independently, except where explicitly noted and referenced. Any collaboration or use of external resources has been properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by the university's academic integrity policy. I understand the importance the consequences of plagiarism.
"""

import unittest

from main import Point, convex_hull_jarvis


class TestMathFunctions(unittest.TestCase):

    # Base testing method
    def baseTestMethod(self, points: list[Point], validResults: list[Point]):
        hull: list[Point] = convex_hull_jarvis(points)

        for result in validResults:
            self.assertIn(result, hull)

        for point in points:
            if point not in validResults:
                self.assertNotIn(point, hull)

    # Basic tests
    def test_example_from_prompt(self):
        points: list[Point] = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
        resultValid: list[Point] = [(0, 3), (0, 0), (3, 0), (3, 3)]
        self.baseTestMethod(points, resultValid)

    def test_basic1(self):
        points: list[Point] = [
            (0, 3),
            (2, 2),
            (1, 1),
            (2, 1),
            (3, 0),
            (0, 0),
            (3, 3),
            (2, -1),
        ]
        resultValid: list[Point] = [(0, 3), (0, 0), (3, 0), (3, 3), (2, -1)]
        self.baseTestMethod(points, resultValid)

    def test_basic2(self):
        points: list[Point] = [
            (0, 3),
            (2, 2),
            (1, 1),
            (2, 1),
            (3, 0),
            (0, 0),
            (3, 3),
            (2, -1),
            (1, -0.5),
        ]
        resultValid: list[Point] = [(0, 3), (0, 0), (3, 0), (3, 3), (2, -1)]
        self.baseTestMethod(points, resultValid)

    def test_basic3(self):
        points: list[Point] = [
            (0, 3),
            (2, 2),
            (1, 1),
            (2, 1),
            (3, 0),
            (0, 0),
            (3, 3),
            (2, -1),
            (1, -0.5),
            (0, 2),
            (0, 1),
        ]
        resultValid: list[Point] = [
            (0, 3),
            (0, 0),
            (3, 0),
            (3, 3),
            (2, -1),
        ]
        self.baseTestMethod(points, resultValid)

    def test_basic4(self):
        points: list[Point] = [
            (0, 3),
            (2, 2),
            (1, 1),
            (2, 1),
            (3, 0),
            (0, 0),
            (3, 3),
            (2, -1),
            (1, -0.5),
            (0, 2),
            (0, 1),
            (-1, 1),
        ]
        resultValid: list[Point] = [
            (0, 3),
            (0, 0),
            (3, 0),
            (3, 3),
            (2, -1),
            (-1, 1),
        ]
        self.baseTestMethod(points, resultValid)

    def test_basic5(self):
        points: list[Point] = [
            (2, 0),
            (0, 2),
            (9, 5),
            (6, 4),
            (2, 1),
            (4, 5),
            (3, -2),
            (7, 0),
            (5, 1)
        ]
        resultValid: list[Point] = [
            (0, 2),
            (3, -2),
            (7, 0),
            (9, 5),
            (4, 5)
        ]
        self.baseTestMethod(points, resultValid)

    def test_basic6(self):
        points: list[Point] = [
            (0, 0),
            (1, 1),
            (0, 2)
        ]
        resultValid: list[Point] = [
            (0, 0),
            (1, 1),
            (0, 2)
        ]
        self.baseTestMethod(points, resultValid)

    # Edge cases
    def test_edge1(self):
        points: list[Point] = [
            (2, 0),
            (0, 2),
            (9, 5),
            (6, 4),
            (2, 1),
            (4, 5),
            (3, -2),
            (7, 0),
            (5, 1),
            (2, 0),
            (0, 2)
        ]
        resultValid: list[Point] = [
            (0, 2),
            (3, -2),
            (7, 0),
            (9, 5),
            (4, 5)
        ]
        self.baseTestMethod(points, resultValid)

    def test_edge2(self):
        points: list[Point] = [
            (2, 0),
            (1, 0),
            (0, 0),
            (3, 0),
            (4, 0)
        ]
        resultValid: list[Point] = [
            (4, 0),
            (0, 0)
        ]
        self.baseTestMethod(points, resultValid)

    def test_edge3(self):
        points: list[Point] = [
            (2, 1),
            (6, 2)
        ]
        resultValid: list[Point] = [
            (2, 1),
            (6, 2)
        ]
        self.baseTestMethod(points, resultValid)

    def test_edge4(self):
        points: list[Point] = [
            (2, 0),
            (6, 0)
        ]
        resultValid: list[Point] = [
            (2, 0),
            (6, 0)
        ]
        self.baseTestMethod(points, resultValid)

    def test_edge5(self):
        points: list[Point] = [
            (2, 0)
        ]
        resultValid: list[Point] = [
            (2, 0)
        ]
        self.baseTestMethod(points, resultValid)

    def test_edge6(self):
        points: list[Point] = [
            (2, 0),
            (2, 0),
            (2, 0),
            (2, 0),
            (2, 0),
            (2, 0)
        ]
        resultValid: list[Point] = [
            (2, 0)
        ]
        self.baseTestMethod(points, resultValid)

    def test_edge7(self):
        points: list[Point] = [
            (2, 2),
            (1, 1),
            (0, 0),
            (3, 3),
            (4, 4)
        ]
        resultValid: list[Point] = [
            (4, 4),
            (0, 0)
        ]
        self.baseTestMethod(points, resultValid)

if __name__ == "__main__":
    _ = unittest.main()
