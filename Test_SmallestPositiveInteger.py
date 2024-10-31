import unittest
import P_TaskSmallestPositiveInteger as Solution


class Test_SmallestPositiveInteger(unittest.TestCase):

    def test_solution_Return5(self):
        lista = [1, 3, 6, 4, 1, 2]
        solution = Solution.solution(lista)
        self.assertEqual(solution, 5)

    def test_solution_Return1(self):
        lista = [-1, -3]
        solution = Solution.solution(lista)
        self.assertEqual(solution, 1)

    def test_solution_Return4(self):
        lista = [1, 2, 3]
        solution = Solution.solution(lista)
        self.assertEqual(solution, 4)

    def test_solution_Return2(self):
        lista = [-1, -3, 0, 1, 3, 4, 6]
        solution = Solution.solution(lista)
        self.assertEqual(solution, 2)


if __name__ == '__main__':
    unittest.main()
