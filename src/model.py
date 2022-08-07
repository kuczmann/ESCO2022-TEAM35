from digital_twin_distiller.boundaries import DirichletBoundaryCondition, NeumannBoundaryCondition
from digital_twin_distiller.material import Material
from digital_twin_distiller.metadata import FemmMetadata, Agros2DMetadata
from digital_twin_distiller.model import BaseModel
from digital_twin_distiller.modelpaths import ModelDir
from digital_twin_distiller.platforms.femm import Femm
from digital_twin_distiller.platforms.agros2d import Agros2D
from digital_twin_distiller.snapshot import Snapshot
from digital_twin_distiller.objects import Rectangle

from dataclasses import dataclass
from copy import copy

ModelDir.set_base(__file__)
from numpy import linspace, meshgrid


@dataclass
class Turn:
    current: float  # Amps
    r_0: float  # m
    z_0: float  # m
    width: float  # m
    height: float  # m

    def get_current_density(self):
        return self.current / (self.width * self.height)


class TEAM35Model(BaseModel):
    """
    This class waits a generalized version of the original TEAM-35 problem.

    Differences
    -----------
       - Here the number of the turns can be defined separately.
       - The symmetry assumption is not used, but it can be defined
       - The number of the turns can be optimized
       - The position of the windings can be defined one by one.
       - The current in the turns can be changed from [-i .. +i].
    """

    def default_turns(self):
        default_turns = []
        for i in range(10):
            default_turns.append(
                Turn(current=3.0, r_0=i * 1e-3 + 6.0 * 1e-3, z_0=i * 1.5 * 1e-3, width=1. * 1e-3, height=1.5 * 1e-3))

        return default_turns

    def __init__(self, **kwargs):
        super(TEAM35Model, self).__init__(**kwargs)

        self._init_directories()

        # The default values of the example script are coming from the original team problem

        # turn definition: it should be a list of dictionaries with the given information
        self.turn_data = kwargs.get('turns', self.default_turns)
        self.symmetrical_problem = kwargs.get('symmetry', True)

    def setup_solver(self):
        # a 2-dimensional, axisymmetric FEMM model is used for the basic simulations
        femm_metadata = FemmMetadata()
        femm_metadata.problem_type = "magnetic"
        femm_metadata.coordinate_type = "axisymmetric"
        femm_metadata.file_script_name = self.file_solver_script
        femm_metadata.file_metrics_name = self.file_solution
        femm_metadata.unit = "meters"
        femm_metadata.smartmesh = True

        agros_metadata = Agros2DMetadata()
        agros_metadata.file_script_name = self.file_solver_script
        agros_metadata.file_metrics_name = self.file_solution
        agros_metadata.problem_type = "magnetic"
        agros_metadata.coordinate_type = "axisymmetric"
        agros_metadata.analysis_type = "steadystate"
        agros_metadata.unit = 1e-3
        agros_metadata.nb_refinements = 0
        agros_metadata.adaptivity = "hp-adaptivity"
        agros_metadata.polyorder = 2
        agros_metadata.adaptivity_tol = 0.001

        self.platform = Femm(femm_metadata)
        # self.platform = Agros2D(agros_metadata)
        self.snapshot = Snapshot(self.platform)

    def define_boundary_conditions(self):
        a0 = DirichletBoundaryCondition("a0", field_type="magnetic", magnetic_potential=0.0)
        n0 = NeumannBoundaryCondition("symmetry", field_type="magnetic")
        # Adding boundary conditions to the snapshot
        self.snapshot.add_boundary_condition(a0)
        self.snapshot.add_boundary_condition(n0)

    def define_materials(self):
        air = Material('air')
        turn = Material('coil')

        for i, elem in enumerate(self.turn_data):
            turn.name = 'turn_{}'.format(i)
            turn.Je = elem.get_current_density()
            self.snapshot.add_material(turn)

        self.snapshot.add_material(air)

    def add_postprocessing(self, Nx=10, Ny=10):

        x = linspace(1e-6, 5e-3, Nx)
        y = linspace(1e-6, 5e-3, Ny)

        xx, yy = meshgrid(x, y, sparse=False, indexing="xy")

        for i in range(Nx):
            for j in range(Ny):
                eval_point = (xx[j, i], yy[j, i])
                self.snapshot.add_postprocessing("point_value", eval_point, "Bz")
                self.snapshot.add_postprocessing("point_value", eval_point, "Br")

        self.snapshot.add_postprocessing("mesh_info", None, None)

    def build_geometry(self):
        """
        The goemetry represents the inner window of the calculated power transformer, which contains three
        rectangles:
         - the inner side of the core window
         - the inner winding
         - the outer winding
        """

        # symmetrycal
        out_rect = Rectangle(0, 0, width=60 * 1e-3, height=20 * 1e-3)

        self.geom.add_rectangle(out_rect)

        self.assign_material(1e-3, 1e-3, 'air')

        self.assign_boundary(*out_rect.a.mean(out_rect.b), 'symmetry')

        self.assign_boundary(*out_rect.b.mean(out_rect.c), 'a0')
        self.assign_boundary(*out_rect.c.mean(out_rect.d), 'a0')
        self.assign_boundary(*out_rect.d.mean(out_rect.a), 'a0')

        for i, turn in enumerate(self.turn_data):
            rect = Rectangle(turn.r_0, turn.z_0, width=turn.width, height=turn.height)
            self.geom.add_rectangle(rect)
            self.assign_material(*rect.cp, 'turn_{}'.format(i))

        self.snapshot.add_geometry(self.geom)


if __name__ == "__main__":

    x = [13.5, 12.5, 10.5, 6.5, 8.5, 7.5, 6.5, 6.5, 6.5, 6.5]

    coil_turns = []
    for i, xi in enumerate(x):
        coil_turns.append(
            Turn(current=3.0, r_0=xi * 1e-3, z_0=i * 1.5 * 1e-3, width=1.0 * 1e-3, height=1.5 * 1e-3))

    m = TEAM35Model(turns=coil_turns)
    m(cleanup=False, devmode=True)
