from copy import copy
import math
import ghalton
import sobol_seq
from joblib.numpy_pickle_utils import xrange
from pyDOE import lhs
from scipy.stats import norm
from numpy import random, full, nan
import matplotlib.pyplot as plt

from artap.individual import Individual
from src.optimization import CoilOptimizationProblem

EXAMINED_CASE = [13.5, 12.5, 10.5, 6.5, 8.5, 7.5, 6.5, 6.5, 6.5, 6.5]
TRUE_F1 = 0.432 * 1e-3


def halton(dim: int, nbpts: int):
    h = full(nbpts * dim, nan)
    p = full(nbpts, nan)
    P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    lognbpts = math.log(nbpts + 1)
    for i in range(dim):
        b = P[i]
        n = int(math.ceil(lognbpts / math.log(b)))
        for t in range(n):
            p[t] = pow(b, -(t + 1))
        for j in range(nbpts):
            d = j + 1
            sum_ = math.fmod(d, b) * p[0]
            for t in range(1, n):
                d = math.floor(d / b)
                sum_ += math.fmod(d, b) * p[t]

            h[j * dim + i] = sum_
    return h.reshape(nbpts, dim)


def original_tolerances(radii_vector: list, uniform_tolerance=0.5):
    maximum_design = []
    minimum_design = []

    for item in radii_vector:
        maximum_design.append(item + uniform_tolerance)
        minimum_design.append(item - uniform_tolerance)

    return [maximum_design, minimum_design]


# uniform distribution of the errors
def uniform_distribution_of_errors_simple_mc(radii_vector: list, n=16, uniform_tolerance=0.5):
    """creates design in 16 points """
    designs = []
    for j in range(n):
        temp = copy(radii_vector)
        for i in xrange(10):
            temp[i] += random.uniform(-uniform_tolerance, uniform_tolerance)
        designs.append(temp)

    return designs


def single_design_with_tolerances(tolerance_vector: list, true_f1=TRUE_F1):
    """ Calculates the robustnees of a single design, for different tolerance vectors. """
    errors = []
    sum_diff = 0.0
    individual = Individual()
    for case in tolerance_vector:
        individual.vector = copy(case)
        dummy = CoilOptimizationProblem()
        result = dummy.evaluate(individual, only_f1=True)
        errors.append(result[0])
        sum_diff += abs(result[0] - true_f1)
    print(errors)
    print("Length of the tolerance calculations:", len(tolerance_vector))
    print("average difference from the TRUE F1 score is:", sum_diff / len(tolerance_vector))
    print("average of the errors (F1*): ", sum(errors) / len(errors))
    print("minimum:", min(errors))
    print("maximum:", max(errors))

    return min(errors), max(errors), sum(errors) / len(errors), sum_diff / len(tolerance_vector)


#
# def lhs_design():
#     design = lhs(2, samples=100000)
#     means = [6.5, 9.5]
#     stdvs = [0.5 / 3, 0.5 / 3]
#     for i in xrange(2):
#         design[:, i] = norm(loc=means[i], scale=stdvs[i]).ppf(design[:, i])
#     print(design)
#
#     fig, ax = plt.subplots(1, 1)
#     ax.hist(design, density=True, histtype='stepfilled', alpha=0.5)
#     ax.legend(loc='best', frameon=False)
#     plt.show()


if __name__ == '__main__':
    # print("Original MIN and MAX postion calculations:")
    # tolerance_cases = original_tolerances(radii_vector=EXAMINED_CASE)  # selects from the maximum and the minimum points
    # single_design_with_tolerances(tolerance_cases)

    print("UNIFORM distribution with MC:")
    tolerance_cases = uniform_distribution_of_errors_simple_mc(radii_vector=EXAMINED_CASE)
    single_design_with_tolerances(tolerance_cases)
