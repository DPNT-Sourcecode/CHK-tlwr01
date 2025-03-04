from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.computer(1, 2) == 3
        assert sum_solution.computer(0,0) == 0
        assert sum_solution.computer(10,20) == 0
        assert sum_solution.computer(50,50) == 0
        assert sum_solution.computer(99,1) == 0
        print("All tests passed for SUM challenege!")


