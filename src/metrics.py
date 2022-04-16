from sklearn.metrics import mean_squared_error, max_error, mean_absolute_error, r2_score


def f1_score(b, b_0=2e-3):
    """ idea: check the results with different regression metrics
    :return: the first one gives back the origirnal problem
    """
    b0 = [b_0] * len(b)
    # f1 = max(map(lambda Babsi: abs(Babsi - b_0), b))

    return max_error(b0, b), mean_absolute_error(b0, b), mean_squared_error(b0, b), r2_score(b0, b)
