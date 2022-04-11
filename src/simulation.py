from src.model import TEAM35Model

from digital_twin_distiller.encapsulator import Encapsulator
from digital_twin_distiller.modelpaths import ModelDir
from digital_twin_distiller.simulationproject import sim


def execute_model(model: TEAM35Model):
    result = model(timeout=2000, cleanup=True)
    return result


@sim.register("short_circuit_impedance")
def short_circuit_impedance(model, modelparams, simparams, miscparams):
    """
    The FEM model gives back the stored magnetic energy in the transformer window, this quantity used to calculate the
    short-circuit impedance (sci) of the power transformer.
    The sci was normed on the impedance base, which calculated from the parameters of the LV terminal.
    """

    # these parameters should be used to inject the model geometry
    #js = simparams["js"]
    #jp = simparams["jp"]

    m = TEAM35Model()
    res = execute_model(m)
    # res = {"Energy": 256.5673046878133}
    Wm = res["Energy"]


    return res


if __name__ == "__main__":
    ModelDir.set_base(__file__)

    # set the model for the simulation
    sim.set_model(TEAM35Model)

    model = Encapsulator(sim)
    # model.build_docs()
    model.host = "0.0.0.0"
    model.port = 5000
    model.run()
