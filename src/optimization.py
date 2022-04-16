from math import inf
from operator import itemgetter

from artap.algorithm_genetic import NSGAII
from artap.problem import Problem
from model import TEAM35Model, Turn

from metrics import f1_score, f2_score


class CoilOptimizationProblem(Problem):
    def set(self):
        self.name = "Team35 Test Problem"

        self.parameters = [
            {"name": "r0", "bounds": [5.0, 20.0]},
            {"name": "r1", "bounds": [5.0, 20.0]},
            {"name": "r2", "bounds": [5.0, 20.0]},
            {"name": "r3", "bounds": [5.0, 20.0]},
            {"name": "r4", "bounds": [5.0, 20.0]},
            {"name": "r5", "bounds": [5.0, 20.0]},
            {"name": "r6", "bounds": [5.0, 20.0]},
            {"name": "r7", "bounds": [5.0, 20.0]},
            {"name": "r8", "bounds": [5.0, 20.0]},
            {"name": "r9", "bounds": [5.0, 20.0]},
        ]

        self.costs = [{"name": "f_1", "criteria": "minimize"}]

    def b_absolute(self, res):
        Br = map(itemgetter(2), res["Br"])
        Bz = map(itemgetter(2), res["Bz"])

        return list(map(lambda Bz_i, Br_i: (Bz_i ** 2. + Br_i ** 2.) ** 0.5, Bz, Br))

    # def f1(self, b, b_0=2e-3):
    #     f1 = max(map(lambda Babsi: abs(Babsi - B0), self.b_absolute(res)))
    #     return

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
                Turn(current=3.0, r_0=xi * 1e-3 + 6.0 * 1e-3, z_0=i * 1.5 * 1e-3, width=1.0 * 1e-3, height=1.5 * 1e-3))

        try:
            model = TEAM35Model(turns=coil_turns)
            res = model(devmode=False, timeout=30, cleanup=True)

            bab = self.b_absolute(res)
            f1 = f1_score(b=bab)[0]
            print("f1:",f1)
            print("DONE")
            return [f1, f2(coil_turns)]
        except:
            print("FAILED")
            return [inf]


if __name__ == "__main__":

    # Perform the optimization iterating over 100 times on 100 individuals.
    problem = CoilOptimizationProblem()
    algorithm = NSGAII(problem)
    algorithm.options["max_population_number"] = 2
    algorithm.options["max_population_size"] = 2
    try:
        algorithm.run()
        res = problem.individuals[-1]
        print(res.vector)
        print(res.costs)
    except KeyboardInterrupt:
        pass
