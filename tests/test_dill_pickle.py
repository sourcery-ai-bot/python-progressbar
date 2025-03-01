import dill

import progressbar


def test_dill():
    bar = progressbar.ProgressBar()
    assert bar._started is False
    assert bar._finished is False

    assert dill.pickles(bar) is False

    assert bar._started is False
    # Should be false because it never should have started/initialized
    assert bar._finished is False
