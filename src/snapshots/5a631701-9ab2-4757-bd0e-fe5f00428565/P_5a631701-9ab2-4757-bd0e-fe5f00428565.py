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
geometry.add_edge(0.0, 0.025, 0.0, 0.0, boundaries={'magnetic': 'a0'})
geometry.add_edge(0.04, 0.025, 0.0, 0.025, boundaries={'magnetic': 'a0'})
geometry.add_edge(0.04, 0.0, 0.04, 0.025, boundaries={'magnetic': 'a0'})
geometry.add_edge(0.0, 0.0, 0.04, 0.0, boundaries={'magnetic': 'symmetry'})
geometry.add_edge(0.007803167468254901, 1e-05, 0.0088031674682549, 1e-05)
geometry.add_edge(0.0088031674682549, 1e-05, 0.0088031674682549, 0.00151)
geometry.add_edge(0.0088031674682549, 0.00151, 0.007803167468254901, 0.00151)
geometry.add_edge(0.007803167468254901, 0.00151, 0.007803167468254901, 1e-05)
geometry.add_edge(0.007022258667733729, 0.00151, 0.00802225866773373, 0.00151)
geometry.add_edge(0.00802225866773373, 0.00151, 0.00802225866773373, 0.00301)
geometry.add_edge(0.00802225866773373, 0.00301, 0.007022258667733729, 0.00301)
geometry.add_edge(0.007022258667733729, 0.00301, 0.007022258667733729, 0.00151)
geometry.add_edge(0.012806266625535287, 0.00301, 0.013806266625535288, 0.00301)
geometry.add_edge(0.013806266625535288, 0.00301, 0.013806266625535288, 0.00451)
geometry.add_edge(0.013806266625535288, 0.00451, 0.012806266625535287, 0.00451)
geometry.add_edge(0.012806266625535287, 0.00451, 0.012806266625535287, 0.00301)
geometry.add_edge(0.019291930956379127, 0.00451, 0.02029193095637913, 0.00451)
geometry.add_edge(0.02029193095637913, 0.00451, 0.02029193095637913, 0.00601)
geometry.add_edge(0.02029193095637913, 0.00601, 0.019291930956379127, 0.00601)
geometry.add_edge(0.019291930956379127, 0.00601, 0.019291930956379127, 0.00451)
geometry.add_edge(0.019360611240481804, 0.00601, 0.020360611240481805, 0.00601)
geometry.add_edge(0.020360611240481805, 0.00601, 0.020360611240481805, 0.007509999999999999)
geometry.add_edge(0.020360611240481805, 0.007509999999999999, 0.019360611240481804, 0.007509999999999999)
geometry.add_edge(0.019360611240481804, 0.007509999999999999, 0.019360611240481804, 0.00601)
geometry.add_edge(0.010702311290759143, 0.007509999999999999, 0.011702311290759142, 0.007509999999999999)
geometry.add_edge(0.011702311290759142, 0.007509999999999999, 0.011702311290759142, 0.009009999999999999)
geometry.add_edge(0.011702311290759142, 0.009009999999999999, 0.010702311290759143, 0.009009999999999999)
geometry.add_edge(0.010702311290759143, 0.009009999999999999, 0.010702311290759143, 0.007509999999999999)
geometry.add_edge(0.012291702904834006, 0.00901, 0.013291702904834005, 0.00901)
geometry.add_edge(0.013291702904834005, 0.00901, 0.013291702904834005, 0.01051)
geometry.add_edge(0.013291702904834005, 0.01051, 0.012291702904834006, 0.01051)
geometry.add_edge(0.012291702904834006, 0.01051, 0.012291702904834006, 0.00901)
geometry.add_edge(0.010895704224092107, 0.01051, 0.011895704224092106, 0.01051)
geometry.add_edge(0.011895704224092106, 0.01051, 0.011895704224092106, 0.01201)
geometry.add_edge(0.011895704224092106, 0.01201, 0.010895704224092107, 0.01201)
geometry.add_edge(0.010895704224092107, 0.01201, 0.010895704224092107, 0.01051)
geometry.add_edge(0.019400548390422587, 0.01201, 0.020400548390422588, 0.01201)
geometry.add_edge(0.020400548390422588, 0.01201, 0.020400548390422588, 0.01351)
geometry.add_edge(0.020400548390422588, 0.01351, 0.019400548390422587, 0.01351)
geometry.add_edge(0.019400548390422587, 0.01351, 0.019400548390422587, 0.01201)
geometry.add_edge(0.013035447017530531, 0.01351, 0.014035447017530532, 0.01351)
geometry.add_edge(0.014035447017530532, 0.01351, 0.014035447017530532, 0.015009999999999999)
geometry.add_edge(0.014035447017530532, 0.015009999999999999, 0.013035447017530531, 0.015009999999999999)
geometry.add_edge(0.013035447017530531, 0.015009999999999999, 0.013035447017530531, 0.01351)

# BLOCK LABELS
geometry.add_label(0.0083031674682549, 0.00076, materials = {'magnetic' : 'turn_0'})
labels.append((0.0083031674682549, 0.00076))
geometry.add_label(0.00752225866773373, 0.0022600000000000003, materials = {'magnetic' : 'turn_1'})
labels.append((0.00752225866773373, 0.0022600000000000003))
geometry.add_label(0.013306266625535287, 0.0037600000000000003, materials = {'magnetic' : 'turn_2'})
labels.append((0.013306266625535287, 0.0037600000000000003))
geometry.add_label(0.019791930956379128, 0.00526, materials = {'magnetic' : 'turn_3'})
labels.append((0.019791930956379128, 0.00526))
geometry.add_label(0.019860611240481805, 0.0067599999999999995, materials = {'magnetic' : 'turn_4'})
labels.append((0.019860611240481805, 0.0067599999999999995))
geometry.add_label(0.011202311290759142, 0.008259999999999998, materials = {'magnetic' : 'turn_5'})
labels.append((0.011202311290759142, 0.008259999999999998))
geometry.add_label(0.012791702904834007, 0.00976, materials = {'magnetic' : 'turn_6'})
labels.append((0.012791702904834007, 0.00976))
geometry.add_label(0.011395704224092106, 0.011260000000000001, materials = {'magnetic' : 'turn_7'})
labels.append((0.011395704224092106, 0.011260000000000001))
geometry.add_label(0.019900548390422587, 0.01276, materials = {'magnetic' : 'turn_8'})
labels.append((0.019900548390422587, 0.01276))
geometry.add_label(0.013535447017530532, 0.014259999999999998, materials = {'magnetic' : 'turn_9'})
labels.append((0.013535447017530532, 0.014259999999999998))
geometry.add_label(0.001, 0.001, materials = {'magnetic' : 'air'})
labels.append((0.001, 0.001))

# SOLVE
problem.solve()
a2d.view.zoom_best_fit()
f = open(r"/home/kuczmann/ESCO2022-TEAM35/src/snapshots/5a631701-9ab2-4757-bd0e-fe5f00428565/S_5a631701-9ab2-4757-bd0e-fe5f00428565.csv", "w")

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
