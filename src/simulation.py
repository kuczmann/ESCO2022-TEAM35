from src.model import TEAM35Model

from digital_twin_distiller.encapsulator import Encapsulator
from digital_twin_distiller.modelpaths import ModelDir
from digital_twin_distiller.simulationproject import sim
from math import inf


def execute_model(model: TEAM35Model):
    result = model(timeout=2000, cleanup=True)
    return result


@sim.register("default")
def default_simulation(model, modelparams, simparams, miscparams):
    x = simparams["r"]  # the r params can define
    B0 = simparams["B0"]

    model = TEAM35Model(rads=x)
    Bz = execute_model(model)

    if Bz is not None:
        f1 = max(map(lambda Bz_i: abs(Bz_i - B0), Bz))
        return {"f1": f1}
    else:
        return {"f1": inf}


if __name__ == "__main__":
    ModelDir.set_base(__file__)

    # set the model for the simulation
    sim.set_model(TEAM35Model)

    model = Encapsulator(sim)
    model.build_docs()
    model.host = "0.0.0.0"
    model.port = 5000
    model.run()
