from math import inf
from operator import itemgetter

from artap.algorithm_genetic import NSGAII
from artap.problem import Problem
from artap.individual import Individual
from model import TEAM35Model, Turn

from metrics import f1_score, f2_losses
from src.metrics import f2_masses
from copy import copy, deepcopy
from sklearn.metrics import max_error

"""This file is not part of this paper. """


class CoilOptimizationProblem(Problem):
    def set(self):
        self.name = "Team35 Test Problem"

        self.parameters = [
            {"name": "r0", "bounds": [13.0, 14.0]},
            {"name": "r1", "bounds": [12.0, 13.0]},
            {"name": "r2", "bounds": [10.0, 11.0]},
            {"name": "r3", "bounds": [6.0, 7.0]},
            {"name": "r4", "bounds": [8.0, 9.0]},
            {"name": "r5", "bounds": [7.0, 8.0]},
            {"name": "r6", "bounds": [6.0, 7.0]},
            {"name": "r7", "bounds": [6.0, 7.0]},
            {"name": "r8", "bounds": [6.0, 7.0]},
            {"name": "r9", "bounds": [6.0, 7.0]},
            {"name": "i0", "bounds": [2.95, 3.05]}
        ]

        self.costs = [{"name": "f_1", "criteria": "maximize"}]

    def b_absolute(self, res):
        Br = map(itemgetter(2), res["Br"])
        Bz = map(itemgetter(2), res["Bz"])

        return list(map(lambda Bz_i, Br_i: (Bz_i ** 2. + Br_i ** 2.) ** 0.5, Bz, Br))

    def calc(self, coil_turns):
        model = TEAM35Model(turns=coil_turns)
        res = model(devmode=False, timeout=30, cleanup=True)
        return res

    def evaluate(self, individual, only_f1=True):
        x = individual.vector

        x1 = [round(xi, 2) for xi in x]
        print("called with", x1, end=" ")
        assert len(x) == 11

        # in the original team problem, only the radii of the turns varied
        # every other parameters coming from the team benchmark problem
        coil_turns = []
        for i in range(len(x1) - 1):
            coil_turns.append(
                Turn(current=x1[-1], r_0=x1[i] * 1e-3, z_0=i * 1.5 * 1e-3, width=1.0 * 1e-3, height=1.5 * 1e-3))

        try:
            # f1 and the modified f2 and f3 measures needs only one evaluation
            res = self.calc(coil_turns=coil_turns)

            # - f1 - #
            ba0 = self.b_absolute(res)  # the absolute values at the expected geometry
            f1 = f1_score(b=ba0)[0]

            if not only_f1:

                f21 = f2_losses(coil_turns)
                f22 = f2_masses(coil_turns)
                print("f1:", f1, "f21:", f21, f22)

                # - f3 -  overestimates the manufacturing error?
                # calculating the tolerance
                # evalution of the f3 metric needs other calculations
                pos_turns = deepcopy(coil_turns)
                neg_turns = deepcopy(coil_turns)

                for i in range(len(pos_turns)):
                    pos_turns[i].r_0 = pos_turns[i].r_0 + 0.5 * 1e-3
                    neg_turns[i].r_0 = neg_turns[i].r_0 - 0.5 * 1e-3

                res_pos = self.calc(coil_turns=pos_turns)
                ba_pos = self.b_absolute(res_pos)
                f3_plus = max_error(ba0, ba_pos)

                res_neg = self.calc(coil_turns=neg_turns)
                ba_neg = self.b_absolute(res_neg)
                f3_minus = max_error(ba0, ba_neg)

            print("DONE")

            if only_f1:
                return [f1]

            else:
                return [f1, f21, f22, f3_minus + f3_plus]

        except:
            print("FAILED")
            return [inf]


if __name__ == "__main__":
    def coil_optimization():
        problem = CoilOptimizationProblem()
        algorithm = NSGAII(problem)
        algorithm.options["max_population_number"] = 30
        algorithm.options["max_population_size"] = 30
        try:
            algorithm.run()
            res = problem.individuals[-1]
            print(res.vector)
            print(res.costs)
        except KeyboardInterrupt:
            pass


    coil_optimization()
