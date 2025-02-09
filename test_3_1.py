from testbook import testbook

@testbook("Assignment_3_1.ipynb", execute=True)
def test_notebook(tb):
    func = tb.ref("sum_positives")
    assert func([2, -1, 3]) == 5
    assert func([1, 2, 3]) == 6
    assert func([-1, -2, -3]) == 0

