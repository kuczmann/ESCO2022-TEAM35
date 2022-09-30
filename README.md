## Additional Data and Calculations for the Paper presented on ESCO22 conference

## Performance Analysis of a Robust Design Optimization of a Solenoid with Different Sensitivity Metrics

The paper contains the performance analysis of the well-known TEAM-35 benchmark
problem (https://www.compumag.org/wp/wp-content/uploads/2021/07/problem-35.pdf), where
the goal is to design a solenoid, which can generate homogenous magnetic field at the given,
squared region. The provided code contains a numerical analysis to resolve this problem,
for this task, a digital-twin-distiller based model was built, which can perform the calculations with
the following open-source solvers: FEMM (https://www.femm.info/wiki/HomePage) and Agros
Suite (https://github.com/karban/agros2d).

The optimization of the Design problem was resolved by Ārtap (https://github.com/artap-framework/artap).
The webpage of the conference is available at: https://www.esco2022.femhub.com/
The proposed paper is still under the review process, after the acceptance it will be downloaded from the ESCO22
conference section of JCAM.

## Installation

The project used a poetry environment with Python3.8, after installing the poetry environment under the correct version
numbered python package, you should download the repository and you can install the necessary requirements by:

> poetry install

## Project structure

- Running the FEM model of the solenoid:
  You can run separately an arbitrary FEM simulation by running the model.py.

- Running the DOE-based calculations on a selected layout:
  you can run them by the selection of the appropriate script at the optimization.py

- Running a quasi-monte carlo or latin-hypercube sampling-based simulation: quasi_mc_methods.py

- Running the originally described simulations with the selected metric: optimization_total.py 



