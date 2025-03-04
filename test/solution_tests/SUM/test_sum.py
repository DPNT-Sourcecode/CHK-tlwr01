from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        assert sum_solution.compute(0,0) == 0
        assert sum_solution.compute(10,20) == 30
        assert sum_solution.compute(50,50) == 100
        assert sum_solution.compute(99,1) == 100
        print("All tests passed for SUM challenege!")



