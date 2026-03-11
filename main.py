"""
John Maynard
CSCI 332 Spring 2025
Programming Assignment #class18
I acknowledge that I have worked on this assignment independently, except where explicitly noted and referenced. Any collaboration or use of external resources has been properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by the university's academic integrity policy. I understand the importance the consequences of plagiarism.
"""
import sys
type Point = tuple[float, float]


def convex_hull_jarvis(points: list[Point]) -> list[Point]:
    hull: list[Point] = []
    lenPoints: int = len(points)

    # Get starting point (and test for errors)
    xIter: int = 1
    yIter: int = 1
    leftMostIndex: int = 0
    rightMostIndex: int = 0
    upMostIndex: int = 0
    downMostIndex: int = 0

    for i in range(1, lenPoints):  # Skip first point
        point: Point = points[i]

        # Convoluted mess. If all the points are collinear then the main loop breaks.
        # This is (theoretically) faster since it doesn't require looping through the points again to find the extremes.
        if point[0] < points[leftMostIndex][0]:
            leftMostIndex = i
        elif point[0] > points[rightMostIndex][0]:
            rightMostIndex = i

        if point[1] < points[upMostIndex][1]:
            upMostIndex = i
        elif point[1] > points[downMostIndex][1]:
            downMostIndex = i

        # Confirms that all points are not collinear.
        if point[0] == points[leftMostIndex][0]:
            yIter += 1
        if point[1] == points[leftMostIndex][1]:
            xIter += 1

    if xIter == lenPoints:
        hull.append(points[leftMostIndex])
        hull.append(points[rightMostIndex])
        return hull
    elif yIter == lenPoints:
        hull.append(points[upMostIndex])
        hull.append(points[downMostIndex])
        return hull

    # Default to leftmost.
    hull.append(points[leftMostIndex])

    # Create hull
    nextPoint: Point
    repeat: bool = True
    currentIndex: int
    while repeat:
        # Check to make sure nextPoint != hull[-1], since orientation will always be zero if it is
        currentIndex = points.index(hull[-1])
        if currentIndex == lenPoints - 1:
            nextPoint = points[currentIndex - 1]
        else:
            nextPoint = points[currentIndex + 1]

        for j in points:
            currentOrientation: float = getOrientation(hull[-1], nextPoint, j)
            if currentOrientation < 0:
                nextPoint = j

        if nextPoint == hull[0]:
            repeat = False
            break

        hull.append(nextPoint)

    # Remove collinear points
    removals: list[Point] = []
    for i in range(len(hull)):
        if getOrientation(hull[i - 1], hull[i], hull[(i + 1) % len(hull)]) == 0:
            removals.append(hull[i])

    if len(removals) < len(hull):
        for i in removals:
            _ = hull.remove(i)

    return hull


def getOrientation(point1: Point, point2: Point, point3: Point) -> float:
    orientation: float = ((point2[1] - point1[1]) * (point3[0] - point2[0])) - (
        (point3[1] - point2[1]) * (point2[0] - point1[0])
    )
    return orientation


if __name__ == "__main__":
    points: list[Point] = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    hull: list[Point] = convex_hull_jarvis(points)
    print("Convex Hull:", hull)

# Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]
