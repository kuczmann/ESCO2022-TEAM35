from copy import copy
import math
import ghalton
import sobol_seq
from joblib.numpy_pickle_utils import xrange
from pyDOE import lhs
from scipy.stats import norm
from numpy import random, full, nan, average, std, subtract, add, multiply
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from artap.individual import Individual
from src.optimization import CoilOptimizationProblem

EXAMINED_CASE = [13.5, 12.5, 10.5, 6.5, 8.5, 7.5, 6.5, 6.5, 6.5, 6.5]
TRUE_F1 = 0.432 * 1e-3


def box_muller_transform(U1, U2):
    random.seed(521)
    # U1 = np.random.uniform(size=1000)
    # U2 = np.random.uniform(size=1000)
    R = np.sqrt(-2 * np.log(U1))
    # Theta = 2 * np.pi * U2
    Theta = multiply(2 * np.pi, U2)
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    temp = ax1.hist(X)
    ax1.set_title("X")
    temp = ax2.hist(Y)
    ax2.set_title("Y")
    plt.show()


def original_tolerances(radii_list, uniform_tolerance=0.5):
    maximum_design = []
    minimum_design = []

    for item in radii_vector:
        maximum_design.append(item + uniform_tolerance)
        minimum_design.append(item - uniform_tolerance)

    return [maximum_design, minimum_design]


# uniform distribution of the errors
def uniform_distribution_of_errors_simple_mc(radii_list, n=16, uniform_tolerance=0.5):
    """creates design in 16 points """
    designs = []
    for j in range(n):
        temp = copy(radii_vector)
        for i in xrange(10):
            temp[i] += random.uniform(-uniform_tolerance, uniform_tolerance)
        designs.append(temp)

    return designs


def single_design_with_tolerances(tolerance_list, true_f1=TRUE_F1):
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


def repeat_tolerance_calculations(tolerance_vector, N: int = 10):
    """
    :param N: represents the number of the repetitions
    """
    overall_minima = []
    overall_maxima = []
    overall_avg = []

    for i in range(N):
        minima, maxima, avg, f1_distance = single_design_with_tolerances(tolerance_vector)
        overall_minima.append(minima)
        overall_maxima.append(maxima)
        overall_avg.append(avg)

    print("Minima (global)", min(overall_minima))
    print("Average of the minimas", average(overall_minima))
    print("Std of the minimas: ", std(overall_minima))
    print("-----------------------------------------")
    print("Maxima (global)", min(overall_maxima))
    print("Average of the minimas", average(overall_minima))
    print("Std of the minimas: ", std(overall_minima))


def normalized_lhs_design(nr_dim=10, samples=128):
    design = lhs(nr_dim, samples=samples)
    # means = [0.0, 0.0]
    means = EXAMINED_CASE
    stdvs = nr_dim * [0.5 / 3]

    for i in xrange(nr_dim):
        design[:, i] = norm(loc=means[i], scale=stdvs[i]).ppf(design[:, i])

    # fig, ax = plt.subplots(1, 1)
    # ax.hist(design, density=True, alpha=0.5)
    # ax.legend(loc='best', frameon=False)
    # plt.show()
    return design


if __name__ == '__main__':
    # print("Original MIN and MAX postion calculations:")
    # tolerance_cases = original_tolerances(radii_vector=EXAMINED_CASE)  # selects from the maximum and the minimum points
    # single_design_with_tolerances(tolerance_cases)

    # print("UNIFORM distribution with MC:")
    # tolerance_cases = uniform_distribution_of_errors_simple_mc(radii_vector=EXAMINED_CASE)
    # single_design_with_tolerances(tolerance_cases)
    # repeat_tolerance_calculations(tolerance_cases)

    # print("UNIFORM DISTRIBUTION WITH HALTON SEQUENCE")
    # sequencer = ghalton.Halton(16)
    # halton_points = sequencer.get(3)  # -> numbers between 0 - 1
    # offseted_points = add(halton_points, EXAMINED_CASE)
    # offseted_points = subtract(offseted_points, 0.5)
    # single_design_with_tolerances(offseted_points)

    # print("UNIFORM DISTRIBUTION WITH SOBOL SEQUENCE")
    # seq = sobol_seq.i4_sobol_generate(10, 16)
    # offseted_points = add(seq, EXAMINED_CASE)
    # offseted_points = subtract(offseted_points, 0.5)

    # single_design_with_tolerances(offseted_points)

    # print("UNIFORM DISTRIBUTION WITH LATIN HYPERCUBE SAMPLING")
    # seq = lhs(10, samples=5)
    # offseted_points = add(seq, EXAMINED_CASE)
    # offseted_points = subtract(offseted_points, 0.5)

    # single_design_with_tolerances(offseted_points)

    # Box Muller transform
    # sequencer = ghalton.Halton(100)
    # halton_points = sequencer.get(2)
    # pts = sobol_seq.i4_sobol_generate(2,10)
    # box_muller_transform(pts[0], pts[1])
    # print - lhs design with gauss distribution
    #print(offseted_points)
    offseted_points = normalized_lhs_design()
    single_design_with_tolerances(offseted_points)
