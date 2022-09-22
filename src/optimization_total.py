from math import inf
from operator import itemgetter

from artap.algorithm_genetic import NSGAII
from artap.problem import Problem
from artap.individual import Individual
from model import TEAM35Model, Turn

from metrics import f1_score, f2_losses
from src.optimization import CoilOptimizationProblem
from src.metrics import f2_masses
from copy import copy, deepcopy
from sklearn.metrics import max_error

from doe import doe_ccf, doe_pbdesign, doe_bbdesign


def single_design_with_doe_tolerances(individual: Individual(), curr_f1):
    # the error metric should be rewritten for other type of designs
    tolerances = doe_pbdesign(10)
    errors = []

    for tol in tolerances:
        for i in range(10):
            individual.vector[i] = individual.vector[i] + tol[i] * 0.5

        dummy = CoilOptimizationProblem()
        result = dummy.evaluate(individual, only_f1=True)
        errors.append(result[0])

    min_error = min(errors)
    max_error = max(errors)
    print('min_error', min_error)
    print('max_error', max_error)
    print('current', curr_f1)

    return max(abs(curr_f1 - max_error), abs(curr_f1 - min_error))


class TotalOptimizationProblem(Problem):
    def set(self):
        self.name = "Team35 Test Problem"

        self.parameters = [
            {"name": "x0", "bounds": [5.05, 30.0]},
            {"name": "x1", "bounds": [5.05, 30.0]},
            {"name": "x2", "bounds": [5.05, 30.0]},
            {"name": "x3", "bounds": [5.05, 30.0]},
            {"name": "x4", "bounds": [5.05, 30.0]},
            {"name": "x5", "bounds": [5.05, 30.0]},
            {"name": "x6", "bounds": [5.05, 30.0]},
            {"name": "x7", "bounds": [5.05, 30.0]},
            {"name": "x8", "bounds": [5.05, 30.0]},
            {"name": "x9", "bounds": [5.05, 30.0]},
        ]

        self.costs = [{"name": "f_1", "criteria": "minimize"}, {"name": "f_2", "criteria": "minimize"}]

    def b_absolute(self, res):
        Br = map(itemgetter(2), res["Br"])
        Bz = map(itemgetter(2), res["Bz"])

        return list(map(lambda Bz_i, Br_i: (Bz_i ** 2. + Br_i ** 2.) ** 0.5, Bz, Br))

    def calc(self, coil_turns):
        model = TEAM35Model(turns=coil_turns)
        res = model(devmode=False, timeout=30, cleanup=True)
        return res

    def evaluate(self, individual):
        x = individual.vector

        x1 = [round(xi, 2) for xi in x]
        print("called with", x1, end=" ")
        assert len(x) == 10

        # in the original team problem, only the radii of the turns varied
        # every other parameters coming from the team benchmark problem
        coil_turns = []
        for i, xi in enumerate(x):
            coil_turns.append(
                Turn(current=3.0, r_0=xi * 1e-3, z_0=i * 1.5 * 1e-3, width=1.0 * 1e-3, height=1.5 * 1e-3))

        try:
            # f1 and f2
            res = self.calc(coil_turns=coil_turns)
            # - f1 - #
            ba0 = self.b_absolute(res)  # the absolute values at the expected geometry
            f1 = f1_score(b=ba0)[0]
            f2 = single_design_with_doe_tolerances(individual, f1)
            return [f1, f2]

        except:
            print("FAILED")
            return [inf, inf]


if __name__ == "__main__":
    import pylab as plt
    from artap.results import Results

    problem = TotalOptimizationProblem()
    algorithm = NSGAII(problem)
    algorithm.options["max_population_number"] = 50
    algorithm.options["max_population_size"] = 50
    algorithm.options['max_processes'] = 10
    algorithm.run()
    # res = problem.individuals[-1]
    # print(res.vector)
    # print(res.costs)
    results = Results(problem)

    list_of_inds = results.problem.individuals
    with open('individuals_pb.txt', 'w') as f:
        for elem in list_of_inds:
            f.write(str(elem))
            f.write('\n')

    table = results.pareto_values()

    with open('pareto_pb.txt', 'w') as f:
        for elem in table:
            f.write("{},{} \n".format(elem[0], elem[1]))
    print(table)
    plt.plot(table, 'o')
    plt.grid()
    plt.xlabel(r'$F_1$', fontsize=16)
    plt.ylabel(r'$F_2$', fontsize=16)
    plt.show()
