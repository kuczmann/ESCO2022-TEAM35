from copy import copy

import ghalton
import sobol_seq
from joblib.numpy_pickle_utils import xrange
from pyDOE import lhs
from scipy.stats import norm
from numpy import random
import matplotlib.pyplot as plt

from artap.individual import Individual
from src.optimization import CoilOptimizationProblem

EXAMINED_CASE = [13.5, 12.5, 10.5, 6.5, 8.5, 7.5, 6.5, 6.5, 6.5, 6.5]


def original_tolerances(radii_vector: list, uniform_tolerance=0.5):
    maximum_design = []
    minimum_design = []

    for item in radii_vector:
        maximum_design.append(item + uniform_tolerance)
        minimum_design.append(item - uniform_tolerance)

    return [maximum_design, minimum_design]


def single_design_with_tolerances(tolerance_vector: list):
    """ Calculates the robustnees of a single design, for different tolerance vectors. """
    errors = []
    individual = Individual()
    for case in tolerance_vector:
        individual.vector = copy(case)
        dummy = CoilOptimizationProblem()
        result = dummy.evaluate(individual, only_f1=True)
        errors.append(result[0])
    print(errors)
    print("average of the errors: ", sum(errors) / len(errors))
    print("minimum:", min(errors))
    print("maximum:", max(errors))


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
    tolerance_cases = original_tolerances(radii_vector=EXAMINED_CASE)  # selects from the maximum and the minimum points
    single_design_with_tolerances(tolerance_cases)
