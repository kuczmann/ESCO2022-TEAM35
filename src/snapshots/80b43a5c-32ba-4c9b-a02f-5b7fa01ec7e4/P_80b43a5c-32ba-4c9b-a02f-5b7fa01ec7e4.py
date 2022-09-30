import agros2d as a2d

# PROBLEM
problem = a2d.problem(clear=True)
problem.coordinate_type = "axisymmetric"
problem.mesh_type = "triangle"

magnetic = a2d.field("magnetic")
magnetic.analysis_type = "steadystate"
magnetic.number_of_refinements = 2
magnetic.polynomial_order = 3
magnetic.solver = "linear"

geometry = a2d.geometry

magnetic.adaptivity_type = "h-adaptivity"
magnetic.adaptivity_parameters["tolerance"] = 0.001
magnetic.adaptivity_parameters["steps"] = 10
labels = []

# MATERIAL DEFINITIONS
magnetic.add_material("turn_0", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 2000000.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})
magnetic.add_material("turn_1", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 2000000.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})
magnetic.add_material("turn_2", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 2000000.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})
magnetic.add_material("turn_3", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 2000000.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})
magnetic.add_material("turn_4", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 2000000.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})
magnetic.add_material("turn_5", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 2000000.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})
magnetic.add_material("turn_6", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 2000000.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})
magnetic.add_material("turn_7", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 2000000.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})
magnetic.add_material("turn_8", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 2000000.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})
magnetic.add_material("turn_9", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 2000000.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})
magnetic.add_material("air", {'magnetic_remanence_angle': 0.0, 'magnetic_velocity_y': 0.0, 'magnetic_current_density_external_real': 0.0, 'magnetic_permeability': 1.0, 'magnetic_conductivity': 0.0, 'magnetic_remanence': 0.0, 'magnetic_velocity_angular': 0.0, 'magnetic_velocity_x': 0.0})

# BOUNDARY DEFINITIONS
magnetic.add_boundary("a0", "magnetic_potential", {'magnetic_potential_real': 0.0})
magnetic.add_boundary("symmetry", "magnetic_surface_current", {'magnetic_surface_current_real': 0.0})

# GEOMETRY
geometry.add_edge(0.04, 0.0, 0.04, 0.025, boundaries={'magnetic': 'a0'})
geometry.add_edge(0.0, 0.025, 0.0, 0.0, boundaries={'magnetic': 'a0'})
geometry.add_edge(0.04, 0.025, 0.0, 0.025, boundaries={'magnetic': 'a0'})
geometry.add_edge(0.0, 0.0, 0.04, 0.0, boundaries={'magnetic': 'symmetry'})
geometry.add_edge(0.012178369727947405, 1e-05, 0.013178369727947406, 1e-05)
geometry.add_edge(0.013178369727947406, 1e-05, 0.013178369727947406, 0.00151)
geometry.add_edge(0.013178369727947406, 0.00151, 0.012178369727947405, 0.00151)
geometry.add_edge(0.012178369727947405, 0.00151, 0.012178369727947405, 1e-05)
geometry.add_edge(0.023634808520091227, 0.00151, 0.024634808520091228, 0.00151)
geometry.add_edge(0.024634808520091228, 0.00151, 0.024634808520091228, 0.00301)
geometry.add_edge(0.024634808520091228, 0.00301, 0.023634808520091227, 0.00301)
geometry.add_edge(0.023634808520091227, 0.00301, 0.023634808520091227, 0.00151)
geometry.add_edge(0.01248499087655658, 0.00301, 0.01348499087655658, 0.00301)
geometry.add_edge(0.01348499087655658, 0.00301, 0.01348499087655658, 0.00451)
geometry.add_edge(0.01348499087655658, 0.00451, 0.01248499087655658, 0.00451)
geometry.add_edge(0.01248499087655658, 0.00451, 0.01248499087655658, 0.00301)
geometry.add_edge(0.027040851577884405, 0.00451, 0.028040851577884406, 0.00451)
geometry.add_edge(0.028040851577884406, 0.00451, 0.028040851577884406, 0.00601)
geometry.add_edge(0.028040851577884406, 0.00601, 0.027040851577884405, 0.00601)
geometry.add_edge(0.027040851577884405, 0.00601, 0.027040851577884405, 0.00451)
geometry.add_edge(0.019009932824226396, 0.00601, 0.020009932824226397, 0.00601)
geometry.add_edge(0.020009932824226397, 0.00601, 0.020009932824226397, 0.007509999999999999)
geometry.add_edge(0.020009932824226397, 0.007509999999999999, 0.019009932824226396, 0.007509999999999999)
geometry.add_edge(0.019009932824226396, 0.007509999999999999, 0.019009932824226396, 0.00601)
geometry.add_edge(0.01595847964624622, 0.007509999999999999, 0.01695847964624622, 0.007509999999999999)
geometry.add_edge(0.01695847964624622, 0.007509999999999999, 0.01695847964624622, 0.009009999999999999)
geometry.add_edge(0.01695847964624622, 0.009009999999999999, 0.01595847964624622, 0.009009999999999999)
geometry.add_edge(0.01595847964624622, 0.009009999999999999, 0.01595847964624622, 0.007509999999999999)
geometry.add_edge(0.015410796143620143, 0.00901, 0.016410796143620142, 0.00901)
geometry.add_edge(0.016410796143620142, 0.00901, 0.016410796143620142, 0.01051)
geometry.add_edge(0.016410796143620142, 0.01051, 0.015410796143620143, 0.01051)
geometry.add_edge(0.015410796143620143, 0.01051, 0.015410796143620143, 0.00901)
geometry.add_edge(0.008002092466356891, 0.01051, 0.00900209246635689, 0.01051)
geometry.add_edge(0.00900209246635689, 0.01051, 0.00900209246635689, 0.01201)
geometry.add_edge(0.00900209246635689, 0.01201, 0.008002092466356891, 0.01201)
geometry.add_edge(0.008002092466356891, 0.01201, 0.008002092466356891, 0.01051)
geometry.add_edge(0.016263450863763424, 0.01201, 0.017263450863763425, 0.01201)
geometry.add_edge(0.017263450863763425, 0.01201, 0.017263450863763425, 0.01351)
geometry.add_edge(0.017263450863763425, 0.01351, 0.016263450863763424, 0.01351)
geometry.add_edge(0.016263450863763424, 0.01351, 0.016263450863763424, 0.01201)
geometry.add_edge(0.008634870681720447, 0.01351, 0.009634870681720448, 0.01351)
geometry.add_edge(0.009634870681720448, 0.01351, 0.009634870681720448, 0.015009999999999999)
geometry.add_edge(0.009634870681720448, 0.015009999999999999, 0.008634870681720447, 0.015009999999999999)
geometry.add_edge(0.008634870681720447, 0.015009999999999999, 0.008634870681720447, 0.01351)

# BLOCK LABELS
geometry.add_label(0.012678369727947406, 0.00076, materials = {'magnetic' : 'turn_0'})
labels.append((0.012678369727947406, 0.00076))
geometry.add_label(0.024134808520091228, 0.0022600000000000003, materials = {'magnetic' : 'turn_1'})
labels.append((0.024134808520091228, 0.0022600000000000003))
geometry.add_label(0.012984990876556579, 0.0037600000000000003, materials = {'magnetic' : 'turn_2'})
labels.append((0.012984990876556579, 0.0037600000000000003))
geometry.add_label(0.027540851577884405, 0.00526, materials = {'magnetic' : 'turn_3'})
labels.append((0.027540851577884405, 0.00526))
geometry.add_label(0.019509932824226396, 0.0067599999999999995, materials = {'magnetic' : 'turn_4'})
labels.append((0.019509932824226396, 0.0067599999999999995))
geometry.add_label(0.01645847964624622, 0.008259999999999998, materials = {'magnetic' : 'turn_5'})
labels.append((0.01645847964624622, 0.008259999999999998))
geometry.add_label(0.01591079614362014, 0.00976, materials = {'magnetic' : 'turn_6'})
labels.append((0.01591079614362014, 0.00976))
geometry.add_label(0.00850209246635689, 0.011260000000000001, materials = {'magnetic' : 'turn_7'})
labels.append((0.00850209246635689, 0.011260000000000001))
geometry.add_label(0.016763450863763425, 0.01276, materials = {'magnetic' : 'turn_8'})
labels.append((0.016763450863763425, 0.01276))
geometry.add_label(0.009134870681720447, 0.014259999999999998, materials = {'magnetic' : 'turn_9'})
labels.append((0.009134870681720447, 0.014259999999999998))
geometry.add_label(0.001, 0.001, materials = {'magnetic' : 'air'})
labels.append((0.001, 0.001))

# SOLVE
problem.solve()
a2d.view.zoom_best_fit()
f = open(r"/home/kuczmann/ESCO2022-TEAM35/src/snapshots/80b43a5c-32ba-4c9b-a02f-5b7fa01ec7e4/S_80b43a5c-32ba-4c9b-a02f-5b7fa01ec7e4.csv", "w")

# POSTPROCESSING AND EXPORTING
point = magnetic.local_values(1e-06, 1e-06)["Brz"]
f.write("{}, 1e-06, 1e-06, {}\n".format("Bz", point))

point = magnetic.local_values(1e-06, 1e-06)["Brr"]
f.write("{}, 1e-06, 1e-06, {}\n".format("Br", point))

point = magnetic.local_values(1e-06, 0.0005564444444444445)["Brz"]
f.write("{}, 1e-06, 0.0005564444444444445, {}\n".format("Bz", point))

point = magnetic.local_values(1e-06, 0.0005564444444444445)["Brr"]
f.write("{}, 1e-06, 0.0005564444444444445, {}\n".format("Br", point))

point = magnetic.local_values(1e-06, 0.0011118888888888888)["Brz"]
f.write("{}, 1e-06, 0.0011118888888888888, {}\n".format("Bz", point))

point = magnetic.local_values(1e-06, 0.0011118888888888888)["Brr"]
f.write("{}, 1e-06, 0.0011118888888888888, {}\n".format("Br", point))

point = magnetic.local_values(1e-06, 0.0016673333333333334)["Brz"]
f.write("{}, 1e-06, 0.0016673333333333334, {}\n".format("Bz", point))

point = magnetic.local_values(1e-06, 0.0016673333333333334)["Brr"]
f.write("{}, 1e-06, 0.0016673333333333334, {}\n".format("Br", point))

point = magnetic.local_values(1e-06, 0.002222777777777778)["Brz"]
f.write("{}, 1e-06, 0.002222777777777778, {}\n".format("Bz", point))

point = magnetic.local_values(1e-06, 0.002222777777777778)["Brr"]
f.write("{}, 1e-06, 0.002222777777777778, {}\n".format("Br", point))

point = magnetic.local_values(1e-06, 0.0027782222222222223)["Brz"]
f.write("{}, 1e-06, 0.0027782222222222223, {}\n".format("Bz", point))

point = magnetic.local_values(1e-06, 0.0027782222222222223)["Brr"]
f.write("{}, 1e-06, 0.0027782222222222223, {}\n".format("Br", point))

point = magnetic.local_values(1e-06, 0.003333666666666667)["Brz"]
f.write("{}, 1e-06, 0.003333666666666667, {}\n".format("Bz", point))

point = magnetic.local_values(1e-06, 0.003333666666666667)["Brr"]
f.write("{}, 1e-06, 0.003333666666666667, {}\n".format("Br", point))

point = magnetic.local_values(1e-06, 0.0038891111111111114)["Brz"]
f.write("{}, 1e-06, 0.0038891111111111114, {}\n".format("Bz", point))

point = magnetic.local_values(1e-06, 0.0038891111111111114)["Brr"]
f.write("{}, 1e-06, 0.0038891111111111114, {}\n".format("Br", point))

point = magnetic.local_values(1e-06, 0.004444555555555556)["Brz"]
f.write("{}, 1e-06, 0.004444555555555556, {}\n".format("Bz", point))

point = magnetic.local_values(1e-06, 0.004444555555555556)["Brr"]
f.write("{}, 1e-06, 0.004444555555555556, {}\n".format("Br", point))

point = magnetic.local_values(1e-06, 0.005)["Brz"]
f.write("{}, 1e-06, 0.005, {}\n".format("Bz", point))

point = magnetic.local_values(1e-06, 0.005)["Brr"]
f.write("{}, 1e-06, 0.005, {}\n".format("Br", point))

point = magnetic.local_values(0.0005564444444444445, 1e-06)["Brz"]
f.write("{}, 0.0005564444444444445, 1e-06, {}\n".format("Bz", point))

point = magnetic.local_values(0.0005564444444444445, 1e-06)["Brr"]
f.write("{}, 0.0005564444444444445, 1e-06, {}\n".format("Br", point))

point = magnetic.local_values(0.0005564444444444445, 0.0005564444444444445)["Brz"]
f.write("{}, 0.0005564444444444445, 0.0005564444444444445, {}\n".format("Bz", point))

point = magnetic.local_values(0.0005564444444444445, 0.0005564444444444445)["Brr"]
f.write("{}, 0.0005564444444444445, 0.0005564444444444445, {}\n".format("Br", point))

point = magnetic.local_values(0.0005564444444444445, 0.0011118888888888888)["Brz"]
f.write("{}, 0.0005564444444444445, 0.0011118888888888888, {}\n".format("Bz", point))

point = magnetic.local_values(0.0005564444444444445, 0.0011118888888888888)["Brr"]
f.write("{}, 0.0005564444444444445, 0.0011118888888888888, {}\n".format("Br", point))

point = magnetic.local_values(0.0005564444444444445, 0.0016673333333333334)["Brz"]
f.write("{}, 0.0005564444444444445, 0.0016673333333333334, {}\n".format("Bz", point))

point = magnetic.local_values(0.0005564444444444445, 0.0016673333333333334)["Brr"]
f.write("{}, 0.0005564444444444445, 0.0016673333333333334, {}\n".format("Br", point))

point = magnetic.local_values(0.0005564444444444445, 0.002222777777777778)["Brz"]
f.write("{}, 0.0005564444444444445, 0.002222777777777778, {}\n".format("Bz", point))

point = magnetic.local_values(0.0005564444444444445, 0.002222777777777778)["Brr"]
f.write("{}, 0.0005564444444444445, 0.002222777777777778, {}\n".format("Br", point))

point = magnetic.local_values(0.0005564444444444445, 0.0027782222222222223)["Brz"]
f.write("{}, 0.0005564444444444445, 0.0027782222222222223, {}\n".format("Bz", point))

point = magnetic.local_values(0.0005564444444444445, 0.0027782222222222223)["Brr"]
f.write("{}, 0.0005564444444444445, 0.0027782222222222223, {}\n".format("Br", point))

point = magnetic.local_values(0.0005564444444444445, 0.003333666666666667)["Brz"]
f.write("{}, 0.0005564444444444445, 0.003333666666666667, {}\n".format("Bz", point))

point = magnetic.local_values(0.0005564444444444445, 0.003333666666666667)["Brr"]
f.write("{}, 0.0005564444444444445, 0.003333666666666667, {}\n".format("Br", point))

point = magnetic.local_values(0.0005564444444444445, 0.0038891111111111114)["Brz"]
f.write("{}, 0.0005564444444444445, 0.0038891111111111114, {}\n".format("Bz", point))

point = magnetic.local_values(0.0005564444444444445, 0.0038891111111111114)["Brr"]
f.write("{}, 0.0005564444444444445, 0.0038891111111111114, {}\n".format("Br", point))

point = magnetic.local_values(0.0005564444444444445, 0.004444555555555556)["Brz"]
f.write("{}, 0.0005564444444444445, 0.004444555555555556, {}\n".format("Bz", point))

point = magnetic.local_values(0.0005564444444444445, 0.004444555555555556)["Brr"]
f.write("{}, 0.0005564444444444445, 0.004444555555555556, {}\n".format("Br", point))

point = magnetic.local_values(0.0005564444444444445, 0.005)["Brz"]
f.write("{}, 0.0005564444444444445, 0.005, {}\n".format("Bz", point))

point = magnetic.local_values(0.0005564444444444445, 0.005)["Brr"]
f.write("{}, 0.0005564444444444445, 0.005, {}\n".format("Br", point))

point = magnetic.local_values(0.0011118888888888888, 1e-06)["Brz"]
f.write("{}, 0.0011118888888888888, 1e-06, {}\n".format("Bz", point))

point = magnetic.local_values(0.0011118888888888888, 1e-06)["Brr"]
f.write("{}, 0.0011118888888888888, 1e-06, {}\n".format("Br", point))

point = magnetic.local_values(0.0011118888888888888, 0.0005564444444444445)["Brz"]
f.write("{}, 0.0011118888888888888, 0.0005564444444444445, {}\n".format("Bz", point))

point = magnetic.local_values(0.0011118888888888888, 0.0005564444444444445)["Brr"]
f.write("{}, 0.0011118888888888888, 0.0005564444444444445, {}\n".format("Br", point))

point = magnetic.local_values(0.0011118888888888888, 0.0011118888888888888)["Brz"]
f.write("{}, 0.0011118888888888888, 0.0011118888888888888, {}\n".format("Bz", point))

point = magnetic.local_values(0.0011118888888888888, 0.0011118888888888888)["Brr"]
f.write("{}, 0.0011118888888888888, 0.0011118888888888888, {}\n".format("Br", point))

point = magnetic.local_values(0.0011118888888888888, 0.0016673333333333334)["Brz"]
f.write("{}, 0.0011118888888888888, 0.0016673333333333334, {}\n".format("Bz", point))

point = magnetic.local_values(0.0011118888888888888, 0.0016673333333333334)["Brr"]
f.write("{}, 0.0011118888888888888, 0.0016673333333333334, {}\n".format("Br", point))

point = magnetic.local_values(0.0011118888888888888, 0.002222777777777778)["Brz"]
f.write("{}, 0.0011118888888888888, 0.002222777777777778, {}\n".format("Bz", point))

point = magnetic.local_values(0.0011118888888888888, 0.002222777777777778)["Brr"]
f.write("{}, 0.0011118888888888888, 0.002222777777777778, {}\n".format("Br", point))

point = magnetic.local_values(0.0011118888888888888, 0.0027782222222222223)["Brz"]
f.write("{}, 0.0011118888888888888, 0.0027782222222222223, {}\n".format("Bz", point))

point = magnetic.local_values(0.0011118888888888888, 0.0027782222222222223)["Brr"]
f.write("{}, 0.0011118888888888888, 0.0027782222222222223, {}\n".format("Br", point))

point = magnetic.local_values(0.0011118888888888888, 0.003333666666666667)["Brz"]
f.write("{}, 0.0011118888888888888, 0.003333666666666667, {}\n".format("Bz", point))

point = magnetic.local_values(0.0011118888888888888, 0.003333666666666667)["Brr"]
f.write("{}, 0.0011118888888888888, 0.003333666666666667, {}\n".format("Br", point))

point = magnetic.local_values(0.0011118888888888888, 0.0038891111111111114)["Brz"]
f.write("{}, 0.0011118888888888888, 0.0038891111111111114, {}\n".format("Bz", point))

point = magnetic.local_values(0.0011118888888888888, 0.0038891111111111114)["Brr"]
f.write("{}, 0.0011118888888888888, 0.0038891111111111114, {}\n".format("Br", point))

point = magnetic.local_values(0.0011118888888888888, 0.004444555555555556)["Brz"]
f.write("{}, 0.0011118888888888888, 0.004444555555555556, {}\n".format("Bz", point))

point = magnetic.local_values(0.0011118888888888888, 0.004444555555555556)["Brr"]
f.write("{}, 0.0011118888888888888, 0.004444555555555556, {}\n".format("Br", point))

point = magnetic.local_values(0.0011118888888888888, 0.005)["Brz"]
f.write("{}, 0.0011118888888888888, 0.005, {}\n".format("Bz", point))

point = magnetic.local_values(0.0011118888888888888, 0.005)["Brr"]
f.write("{}, 0.0011118888888888888, 0.005, {}\n".format("Br", point))

point = magnetic.local_values(0.0016673333333333334, 1e-06)["Brz"]
f.write("{}, 0.0016673333333333334, 1e-06, {}\n".format("Bz", point))

point = magnetic.local_values(0.0016673333333333334, 1e-06)["Brr"]
f.write("{}, 0.0016673333333333334, 1e-06, {}\n".format("Br", point))

point = magnetic.local_values(0.0016673333333333334, 0.0005564444444444445)["Brz"]
f.write("{}, 0.0016673333333333334, 0.0005564444444444445, {}\n".format("Bz", point))

point = magnetic.local_values(0.0016673333333333334, 0.0005564444444444445)["Brr"]
f.write("{}, 0.0016673333333333334, 0.0005564444444444445, {}\n".format("Br", point))

point = magnetic.local_values(0.0016673333333333334, 0.0011118888888888888)["Brz"]
f.write("{}, 0.0016673333333333334, 0.0011118888888888888, {}\n".format("Bz", point))

point = magnetic.local_values(0.0016673333333333334, 0.0011118888888888888)["Brr"]
f.write("{}, 0.0016673333333333334, 0.0011118888888888888, {}\n".format("Br", point))

point = magnetic.local_values(0.0016673333333333334, 0.0016673333333333334)["Brz"]
f.write("{}, 0.0016673333333333334, 0.0016673333333333334, {}\n".format("Bz", point))

point = magnetic.local_values(0.0016673333333333334, 0.0016673333333333334)["Brr"]
f.write("{}, 0.0016673333333333334, 0.0016673333333333334, {}\n".format("Br", point))

point = magnetic.local_values(0.0016673333333333334, 0.002222777777777778)["Brz"]
f.write("{}, 0.0016673333333333334, 0.002222777777777778, {}\n".format("Bz", point))

point = magnetic.local_values(0.0016673333333333334, 0.002222777777777778)["Brr"]
f.write("{}, 0.0016673333333333334, 0.002222777777777778, {}\n".format("Br", point))

point = magnetic.local_values(0.0016673333333333334, 0.0027782222222222223)["Brz"]
f.write("{}, 0.0016673333333333334, 0.0027782222222222223, {}\n".format("Bz", point))

point = magnetic.local_values(0.0016673333333333334, 0.0027782222222222223)["Brr"]
f.write("{}, 0.0016673333333333334, 0.0027782222222222223, {}\n".format("Br", point))

point = magnetic.local_values(0.0016673333333333334, 0.003333666666666667)["Brz"]
f.write("{}, 0.0016673333333333334, 0.003333666666666667, {}\n".format("Bz", point))

point = magnetic.local_values(0.0016673333333333334, 0.003333666666666667)["Brr"]
f.write("{}, 0.0016673333333333334, 0.003333666666666667, {}\n".format("Br", point))

point = magnetic.local_values(0.0016673333333333334, 0.0038891111111111114)["Brz"]
f.write("{}, 0.0016673333333333334, 0.0038891111111111114, {}\n".format("Bz", point))

point = magnetic.local_values(0.0016673333333333334, 0.0038891111111111114)["Brr"]
f.write("{}, 0.0016673333333333334, 0.0038891111111111114, {}\n".format("Br", point))

point = magnetic.local_values(0.0016673333333333334, 0.004444555555555556)["Brz"]
f.write("{}, 0.0016673333333333334, 0.004444555555555556, {}\n".format("Bz", point))

point = magnetic.local_values(0.0016673333333333334, 0.004444555555555556)["Brr"]
f.write("{}, 0.0016673333333333334, 0.004444555555555556, {}\n".format("Br", point))

point = magnetic.local_values(0.0016673333333333334, 0.005)["Brz"]
f.write("{}, 0.0016673333333333334, 0.005, {}\n".format("Bz", point))

point = magnetic.local_values(0.0016673333333333334, 0.005)["Brr"]
f.write("{}, 0.0016673333333333334, 0.005, {}\n".format("Br", point))

point = magnetic.local_values(0.002222777777777778, 1e-06)["Brz"]
f.write("{}, 0.002222777777777778, 1e-06, {}\n".format("Bz", point))

point = magnetic.local_values(0.002222777777777778, 1e-06)["Brr"]
f.write("{}, 0.002222777777777778, 1e-06, {}\n".format("Br", point))

point = magnetic.local_values(0.002222777777777778, 0.0005564444444444445)["Brz"]
f.write("{}, 0.002222777777777778, 0.0005564444444444445, {}\n".format("Bz", point))

point = magnetic.local_values(0.002222777777777778, 0.0005564444444444445)["Brr"]
f.write("{}, 0.002222777777777778, 0.0005564444444444445, {}\n".format("Br", point))

point = magnetic.local_values(0.002222777777777778, 0.0011118888888888888)["Brz"]
f.write("{}, 0.002222777777777778, 0.0011118888888888888, {}\n".format("Bz", point))

point = magnetic.local_values(0.002222777777777778, 0.0011118888888888888)["Brr"]
f.write("{}, 0.002222777777777778, 0.0011118888888888888, {}\n".format("Br", point))

point = magnetic.local_values(0.002222777777777778, 0.0016673333333333334)["Brz"]
f.write("{}, 0.002222777777777778, 0.0016673333333333334, {}\n".format("Bz", point))

point = magnetic.local_values(0.002222777777777778, 0.0016673333333333334)["Brr"]
f.write("{}, 0.002222777777777778, 0.0016673333333333334, {}\n".format("Br", point))

point = magnetic.local_values(0.002222777777777778, 0.002222777777777778)["Brz"]
f.write("{}, 0.002222777777777778, 0.002222777777777778, {}\n".format("Bz", point))

point = magnetic.local_values(0.002222777777777778, 0.002222777777777778)["Brr"]
f.write("{}, 0.002222777777777778, 0.002222777777777778, {}\n".format("Br", point))

point = magnetic.local_values(0.002222777777777778, 0.0027782222222222223)["Brz"]
f.write("{}, 0.002222777777777778, 0.0027782222222222223, {}\n".format("Bz", point))

point = magnetic.local_values(0.002222777777777778, 0.0027782222222222223)["Brr"]
f.write("{}, 0.002222777777777778, 0.0027782222222222223, {}\n".format("Br", point))

point = magnetic.local_values(0.002222777777777778, 0.003333666666666667)["Brz"]
f.write("{}, 0.002222777777777778, 0.003333666666666667, {}\n".format("Bz", point))

point = magnetic.local_values(0.002222777777777778, 0.003333666666666667)["Brr"]
f.write("{}, 0.002222777777777778, 0.003333666666666667, {}\n".format("Br", point))

point = magnetic.local_values(0.002222777777777778, 0.0038891111111111114)["Brz"]
f.write("{}, 0.002222777777777778, 0.0038891111111111114, {}\n".format("Bz", point))

point = magnetic.local_values(0.002222777777777778, 0.0038891111111111114)["Brr"]
f.write("{}, 0.002222777777777778, 0.0038891111111111114, {}\n".format("Br", point))

point = magnetic.local_values(0.002222777777777778, 0.004444555555555556)["Brz"]
f.write("{}, 0.002222777777777778, 0.004444555555555556, {}\n".format("Bz", point))

point = magnetic.local_values(0.002222777777777778, 0.004444555555555556)["Brr"]
f.write("{}, 0.002222777777777778, 0.004444555555555556, {}\n".format("Br", point))

point = magnetic.local_values(0.002222777777777778, 0.005)["Brz"]
f.write("{}, 0.002222777777777778, 0.005, {}\n".format("Bz", point))

point = magnetic.local_values(0.002222777777777778, 0.005)["Brr"]
f.write("{}, 0.002222777777777778, 0.005, {}\n".format("Br", point))

point = magnetic.local_values(0.0027782222222222223, 1e-06)["Brz"]
f.write("{}, 0.0027782222222222223, 1e-06, {}\n".format("Bz", point))

point = magnetic.local_values(0.0027782222222222223, 1e-06)["Brr"]
f.write("{}, 0.0027782222222222223, 1e-06, {}\n".format("Br", point))

point = magnetic.local_values(0.0027782222222222223, 0.0005564444444444445)["Brz"]
f.write("{}, 0.0027782222222222223, 0.0005564444444444445, {}\n".format("Bz", point))

point = magnetic.local_values(0.0027782222222222223, 0.0005564444444444445)["Brr"]
f.write("{}, 0.0027782222222222223, 0.0005564444444444445, {}\n".format("Br", point))

point = magnetic.local_values(0.0027782222222222223, 0.0011118888888888888)["Brz"]
f.write("{}, 0.0027782222222222223, 0.0011118888888888888, {}\n".format("Bz", point))

point = magnetic.local_values(0.0027782222222222223, 0.0011118888888888888)["Brr"]
f.write("{}, 0.0027782222222222223, 0.0011118888888888888, {}\n".format("Br", point))

point = magnetic.local_values(0.0027782222222222223, 0.0016673333333333334)["Brz"]
f.write("{}, 0.0027782222222222223, 0.0016673333333333334, {}\n".format("Bz", point))

point = magnetic.local_values(0.0027782222222222223, 0.0016673333333333334)["Brr"]
f.write("{}, 0.0027782222222222223, 0.0016673333333333334, {}\n".format("Br", point))

point = magnetic.local_values(0.0027782222222222223, 0.002222777777777778)["Brz"]
f.write("{}, 0.0027782222222222223, 0.002222777777777778, {}\n".format("Bz", point))

point = magnetic.local_values(0.0027782222222222223, 0.002222777777777778)["Brr"]
f.write("{}, 0.0027782222222222223, 0.002222777777777778, {}\n".format("Br", point))

point = magnetic.local_values(0.0027782222222222223, 0.0027782222222222223)["Brz"]
f.write("{}, 0.0027782222222222223, 0.0027782222222222223, {}\n".format("Bz", point))

point = magnetic.local_values(0.0027782222222222223, 0.0027782222222222223)["Brr"]
f.write("{}, 0.0027782222222222223, 0.0027782222222222223, {}\n".format("Br", point))

point = magnetic.local_values(0.0027782222222222223, 0.003333666666666667)["Brz"]
f.write("{}, 0.0027782222222222223, 0.003333666666666667, {}\n".format("Bz", point))

point = magnetic.local_values(0.0027782222222222223, 0.003333666666666667)["Brr"]
f.write("{}, 0.0027782222222222223, 0.003333666666666667, {}\n".format("Br", point))

point = magnetic.local_values(0.0027782222222222223, 0.0038891111111111114)["Brz"]
f.write("{}, 0.0027782222222222223, 0.0038891111111111114, {}\n".format("Bz", point))

point = magnetic.local_values(0.0027782222222222223, 0.0038891111111111114)["Brr"]
f.write("{}, 0.0027782222222222223, 0.0038891111111111114, {}\n".format("Br", point))

point = magnetic.local_values(0.0027782222222222223, 0.004444555555555556)["Brz"]
f.write("{}, 0.0027782222222222223, 0.004444555555555556, {}\n".format("Bz", point))

point = magnetic.local_values(0.0027782222222222223, 0.004444555555555556)["Brr"]
f.write("{}, 0.0027782222222222223, 0.004444555555555556, {}\n".format("Br", point))

point = magnetic.local_values(0.0027782222222222223, 0.005)["Brz"]
f.write("{}, 0.0027782222222222223, 0.005, {}\n".format("Bz", point))

point = magnetic.local_values(0.0027782222222222223, 0.005)["Brr"]
f.write("{}, 0.0027782222222222223, 0.005, {}\n".format("Br", point))

point = magnetic.local_values(0.003333666666666667, 1e-06)["Brz"]
f.write("{}, 0.003333666666666667, 1e-06, {}\n".format("Bz", point))

point = magnetic.local_values(0.003333666666666667, 1e-06)["Brr"]
f.write("{}, 0.003333666666666667, 1e-06, {}\n".format("Br", point))

point = magnetic.local_values(0.003333666666666667, 0.0005564444444444445)["Brz"]
f.write("{}, 0.003333666666666667, 0.0005564444444444445, {}\n".format("Bz", point))

point = magnetic.local_values(0.003333666666666667, 0.0005564444444444445)["Brr"]
f.write("{}, 0.003333666666666667, 0.0005564444444444445, {}\n".format("Br", point))

point = magnetic.local_values(0.003333666666666667, 0.0011118888888888888)["Brz"]
f.write("{}, 0.003333666666666667, 0.0011118888888888888, {}\n".format("Bz", point))

point = magnetic.local_values(0.003333666666666667, 0.0011118888888888888)["Brr"]
f.write("{}, 0.003333666666666667, 0.0011118888888888888, {}\n".format("Br", point))

point = magnetic.local_values(0.003333666666666667, 0.0016673333333333334)["Brz"]
f.write("{}, 0.003333666666666667, 0.0016673333333333334, {}\n".format("Bz", point))

point = magnetic.local_values(0.003333666666666667, 0.0016673333333333334)["Brr"]
f.write("{}, 0.003333666666666667, 0.0016673333333333334, {}\n".format("Br", point))

point = magnetic.local_values(0.003333666666666667, 0.002222777777777778)["Brz"]
f.write("{}, 0.003333666666666667, 0.002222777777777778, {}\n".format("Bz", point))

point = magnetic.local_values(0.003333666666666667, 0.002222777777777778)["Brr"]
f.write("{}, 0.003333666666666667, 0.002222777777777778, {}\n".format("Br", point))

point = magnetic.local_values(0.003333666666666667, 0.0027782222222222223)["Brz"]
f.write("{}, 0.003333666666666667, 0.0027782222222222223, {}\n".format("Bz", point))

point = magnetic.local_values(0.003333666666666667, 0.0027782222222222223)["Brr"]
f.write("{}, 0.003333666666666667, 0.0027782222222222223, {}\n".format("Br", point))

point = magnetic.local_values(0.003333666666666667, 0.003333666666666667)["Brz"]
f.write("{}, 0.003333666666666667, 0.003333666666666667, {}\n".format("Bz", point))

point = magnetic.local_values(0.003333666666666667, 0.003333666666666667)["Brr"]
f.write("{}, 0.003333666666666667, 0.003333666666666667, {}\n".format("Br", point))

point = magnetic.local_values(0.003333666666666667, 0.0038891111111111114)["Brz"]
f.write("{}, 0.003333666666666667, 0.0038891111111111114, {}\n".format("Bz", point))

point = magnetic.local_values(0.003333666666666667, 0.0038891111111111114)["Brr"]
f.write("{}, 0.003333666666666667, 0.0038891111111111114, {}\n".format("Br", point))

point = magnetic.local_values(0.003333666666666667, 0.004444555555555556)["Brz"]
f.write("{}, 0.003333666666666667, 0.004444555555555556, {}\n".format("Bz", point))

point = magnetic.local_values(0.003333666666666667, 0.004444555555555556)["Brr"]
f.write("{}, 0.003333666666666667, 0.004444555555555556, {}\n".format("Br", point))

point = magnetic.local_values(0.003333666666666667, 0.005)["Brz"]
f.write("{}, 0.003333666666666667, 0.005, {}\n".format("Bz", point))

point = magnetic.local_values(0.003333666666666667, 0.005)["Brr"]
f.write("{}, 0.003333666666666667, 0.005, {}\n".format("Br", point))

point = magnetic.local_values(0.0038891111111111114, 1e-06)["Brz"]
f.write("{}, 0.0038891111111111114, 1e-06, {}\n".format("Bz", point))

point = magnetic.local_values(0.0038891111111111114, 1e-06)["Brr"]
f.write("{}, 0.0038891111111111114, 1e-06, {}\n".format("Br", point))

point = magnetic.local_values(0.0038891111111111114, 0.0005564444444444445)["Brz"]
f.write("{}, 0.0038891111111111114, 0.0005564444444444445, {}\n".format("Bz", point))

point = magnetic.local_values(0.0038891111111111114, 0.0005564444444444445)["Brr"]
f.write("{}, 0.0038891111111111114, 0.0005564444444444445, {}\n".format("Br", point))

point = magnetic.local_values(0.0038891111111111114, 0.0011118888888888888)["Brz"]
f.write("{}, 0.0038891111111111114, 0.0011118888888888888, {}\n".format("Bz", point))

point = magnetic.local_values(0.0038891111111111114, 0.0011118888888888888)["Brr"]
f.write("{}, 0.0038891111111111114, 0.0011118888888888888, {}\n".format("Br", point))

point = magnetic.local_values(0.0038891111111111114, 0.0016673333333333334)["Brz"]
f.write("{}, 0.0038891111111111114, 0.0016673333333333334, {}\n".format("Bz", point))

point = magnetic.local_values(0.0038891111111111114, 0.0016673333333333334)["Brr"]
f.write("{}, 0.0038891111111111114, 0.0016673333333333334, {}\n".format("Br", point))

point = magnetic.local_values(0.0038891111111111114, 0.002222777777777778)["Brz"]
f.write("{}, 0.0038891111111111114, 0.002222777777777778, {}\n".format("Bz", point))

point = magnetic.local_values(0.0038891111111111114, 0.002222777777777778)["Brr"]
f.write("{}, 0.0038891111111111114, 0.002222777777777778, {}\n".format("Br", point))

point = magnetic.local_values(0.0038891111111111114, 0.0027782222222222223)["Brz"]
f.write("{}, 0.0038891111111111114, 0.0027782222222222223, {}\n".format("Bz", point))

point = magnetic.local_values(0.0038891111111111114, 0.0027782222222222223)["Brr"]
f.write("{}, 0.0038891111111111114, 0.0027782222222222223, {}\n".format("Br", point))

point = magnetic.local_values(0.0038891111111111114, 0.003333666666666667)["Brz"]
f.write("{}, 0.0038891111111111114, 0.003333666666666667, {}\n".format("Bz", point))

point = magnetic.local_values(0.0038891111111111114, 0.003333666666666667)["Brr"]
f.write("{}, 0.0038891111111111114, 0.003333666666666667, {}\n".format("Br", point))

point = magnetic.local_values(0.0038891111111111114, 0.0038891111111111114)["Brz"]
f.write("{}, 0.0038891111111111114, 0.0038891111111111114, {}\n".format("Bz", point))

point = magnetic.local_values(0.0038891111111111114, 0.0038891111111111114)["Brr"]
f.write("{}, 0.0038891111111111114, 0.0038891111111111114, {}\n".format("Br", point))

point = magnetic.local_values(0.0038891111111111114, 0.004444555555555556)["Brz"]
f.write("{}, 0.0038891111111111114, 0.004444555555555556, {}\n".format("Bz", point))

point = magnetic.local_values(0.0038891111111111114, 0.004444555555555556)["Brr"]
f.write("{}, 0.0038891111111111114, 0.004444555555555556, {}\n".format("Br", point))

point = magnetic.local_values(0.0038891111111111114, 0.005)["Brz"]
f.write("{}, 0.0038891111111111114, 0.005, {}\n".format("Bz", point))

point = magnetic.local_values(0.0038891111111111114, 0.005)["Brr"]
f.write("{}, 0.0038891111111111114, 0.005, {}\n".format("Br", point))

point = magnetic.local_values(0.004444555555555556, 1e-06)["Brz"]
f.write("{}, 0.004444555555555556, 1e-06, {}\n".format("Bz", point))

point = magnetic.local_values(0.004444555555555556, 1e-06)["Brr"]
f.write("{}, 0.004444555555555556, 1e-06, {}\n".format("Br", point))

point = magnetic.local_values(0.004444555555555556, 0.0005564444444444445)["Brz"]
f.write("{}, 0.004444555555555556, 0.0005564444444444445, {}\n".format("Bz", point))

point = magnetic.local_values(0.004444555555555556, 0.0005564444444444445)["Brr"]
f.write("{}, 0.004444555555555556, 0.0005564444444444445, {}\n".format("Br", point))

point = magnetic.local_values(0.004444555555555556, 0.0011118888888888888)["Brz"]
f.write("{}, 0.004444555555555556, 0.0011118888888888888, {}\n".format("Bz", point))

point = magnetic.local_values(0.004444555555555556, 0.0011118888888888888)["Brr"]
f.write("{}, 0.004444555555555556, 0.0011118888888888888, {}\n".format("Br", point))

point = magnetic.local_values(0.004444555555555556, 0.0016673333333333334)["Brz"]
f.write("{}, 0.004444555555555556, 0.0016673333333333334, {}\n".format("Bz", point))

point = magnetic.local_values(0.004444555555555556, 0.0016673333333333334)["Brr"]
f.write("{}, 0.004444555555555556, 0.0016673333333333334, {}\n".format("Br", point))

point = magnetic.local_values(0.004444555555555556, 0.002222777777777778)["Brz"]
f.write("{}, 0.004444555555555556, 0.002222777777777778, {}\n".format("Bz", point))

point = magnetic.local_values(0.004444555555555556, 0.002222777777777778)["Brr"]
f.write("{}, 0.004444555555555556, 0.002222777777777778, {}\n".format("Br", point))

point = magnetic.local_values(0.004444555555555556, 0.0027782222222222223)["Brz"]
f.write("{}, 0.004444555555555556, 0.0027782222222222223, {}\n".format("Bz", point))

point = magnetic.local_values(0.004444555555555556, 0.0027782222222222223)["Brr"]
f.write("{}, 0.004444555555555556, 0.0027782222222222223, {}\n".format("Br", point))

point = magnetic.local_values(0.004444555555555556, 0.003333666666666667)["Brz"]
f.write("{}, 0.004444555555555556, 0.003333666666666667, {}\n".format("Bz", point))

point = magnetic.local_values(0.004444555555555556, 0.003333666666666667)["Brr"]
f.write("{}, 0.004444555555555556, 0.003333666666666667, {}\n".format("Br", point))

point = magnetic.local_values(0.004444555555555556, 0.0038891111111111114)["Brz"]
f.write("{}, 0.004444555555555556, 0.0038891111111111114, {}\n".format("Bz", point))

point = magnetic.local_values(0.004444555555555556, 0.0038891111111111114)["Brr"]
f.write("{}, 0.004444555555555556, 0.0038891111111111114, {}\n".format("Br", point))

point = magnetic.local_values(0.004444555555555556, 0.004444555555555556)["Brz"]
f.write("{}, 0.004444555555555556, 0.004444555555555556, {}\n".format("Bz", point))

point = magnetic.local_values(0.004444555555555556, 0.004444555555555556)["Brr"]
f.write("{}, 0.004444555555555556, 0.004444555555555556, {}\n".format("Br", point))

point = magnetic.local_values(0.004444555555555556, 0.005)["Brz"]
f.write("{}, 0.004444555555555556, 0.005, {}\n".format("Bz", point))

point = magnetic.local_values(0.004444555555555556, 0.005)["Brr"]
f.write("{}, 0.004444555555555556, 0.005, {}\n".format("Br", point))

point = magnetic.local_values(0.005, 1e-06)["Brz"]
f.write("{}, 0.005, 1e-06, {}\n".format("Bz", point))

point = magnetic.local_values(0.005, 1e-06)["Brr"]
f.write("{}, 0.005, 1e-06, {}\n".format("Br", point))

point = magnetic.local_values(0.005, 0.0005564444444444445)["Brz"]
f.write("{}, 0.005, 0.0005564444444444445, {}\n".format("Bz", point))

point = magnetic.local_values(0.005, 0.0005564444444444445)["Brr"]
f.write("{}, 0.005, 0.0005564444444444445, {}\n".format("Br", point))

point = magnetic.local_values(0.005, 0.0011118888888888888)["Brz"]
f.write("{}, 0.005, 0.0011118888888888888, {}\n".format("Bz", point))

point = magnetic.local_values(0.005, 0.0011118888888888888)["Brr"]
f.write("{}, 0.005, 0.0011118888888888888, {}\n".format("Br", point))

point = magnetic.local_values(0.005, 0.0016673333333333334)["Brz"]
f.write("{}, 0.005, 0.0016673333333333334, {}\n".format("Bz", point))

point = magnetic.local_values(0.005, 0.0016673333333333334)["Brr"]
f.write("{}, 0.005, 0.0016673333333333334, {}\n".format("Br", point))

point = magnetic.local_values(0.005, 0.002222777777777778)["Brz"]
f.write("{}, 0.005, 0.002222777777777778, {}\n".format("Bz", point))

point = magnetic.local_values(0.005, 0.002222777777777778)["Brr"]
f.write("{}, 0.005, 0.002222777777777778, {}\n".format("Br", point))

point = magnetic.local_values(0.005, 0.0027782222222222223)["Brz"]
f.write("{}, 0.005, 0.0027782222222222223, {}\n".format("Bz", point))

point = magnetic.local_values(0.005, 0.0027782222222222223)["Brr"]
f.write("{}, 0.005, 0.0027782222222222223, {}\n".format("Br", point))

point = magnetic.local_values(0.005, 0.003333666666666667)["Brz"]
f.write("{}, 0.005, 0.003333666666666667, {}\n".format("Bz", point))

point = magnetic.local_values(0.005, 0.003333666666666667)["Brr"]
f.write("{}, 0.005, 0.003333666666666667, {}\n".format("Br", point))

point = magnetic.local_values(0.005, 0.0038891111111111114)["Brz"]
f.write("{}, 0.005, 0.0038891111111111114, {}\n".format("Bz", point))

point = magnetic.local_values(0.005, 0.0038891111111111114)["Brr"]
f.write("{}, 0.005, 0.0038891111111111114, {}\n".format("Br", point))

point = magnetic.local_values(0.005, 0.004444555555555556)["Brz"]
f.write("{}, 0.005, 0.004444555555555556, {}\n".format("Bz", point))

point = magnetic.local_values(0.005, 0.004444555555555556)["Brr"]
f.write("{}, 0.005, 0.004444555555555556, {}\n".format("Br", point))

point = magnetic.local_values(0.005, 0.005)["Brz"]
f.write("{}, 0.005, 0.005, {}\n".format("Bz", point))

point = magnetic.local_values(0.005, 0.005)["Brr"]
f.write("{}, 0.005, 0.005, {}\n".format("Br", point))

info = magnetic.solution_mesh_info()
f.write("{}, {}\n".format("dofs", info["dofs"]))
f.write("{}, {}\n".format("nodes", info["nodes"]))
f.write("{}, {}\n".format("elements", info["elements"]))

# CLOSING STEPS
f.close()
