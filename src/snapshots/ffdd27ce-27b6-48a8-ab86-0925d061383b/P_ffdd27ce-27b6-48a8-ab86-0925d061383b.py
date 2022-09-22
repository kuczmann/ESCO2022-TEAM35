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
geometry.add_edge(0.009957628346892455, 1e-05, 0.010957628346892456, 1e-05)
geometry.add_edge(0.010957628346892456, 1e-05, 0.010957628346892456, 0.00151)
geometry.add_edge(0.010957628346892456, 0.00151, 0.009957628346892455, 0.00151)
geometry.add_edge(0.009957628346892455, 0.00151, 0.009957628346892455, 1e-05)
geometry.add_edge(0.007122600276996442, 0.00151, 0.008122600276996442, 0.00151)
geometry.add_edge(0.008122600276996442, 0.00151, 0.008122600276996442, 0.00301)
geometry.add_edge(0.008122600276996442, 0.00301, 0.007122600276996442, 0.00301)
geometry.add_edge(0.007122600276996442, 0.00301, 0.007122600276996442, 0.00151)
geometry.add_edge(0.012598404813831034, 0.00301, 0.013598404813831035, 0.00301)
geometry.add_edge(0.013598404813831035, 0.00301, 0.013598404813831035, 0.00451)
geometry.add_edge(0.013598404813831035, 0.00451, 0.012598404813831034, 0.00451)
geometry.add_edge(0.012598404813831034, 0.00451, 0.012598404813831034, 0.00301)
geometry.add_edge(0.00789388600983803, 0.00451, 0.00889388600983803, 0.00451)
geometry.add_edge(0.00889388600983803, 0.00451, 0.00889388600983803, 0.00601)
geometry.add_edge(0.00889388600983803, 0.00601, 0.00789388600983803, 0.00601)
geometry.add_edge(0.00789388600983803, 0.00601, 0.00789388600983803, 0.00451)
geometry.add_edge(0.005008617929673261, 0.00601, 0.006008617929673261, 0.00601)
geometry.add_edge(0.006008617929673261, 0.00601, 0.006008617929673261, 0.007509999999999999)
geometry.add_edge(0.006008617929673261, 0.007509999999999999, 0.005008617929673261, 0.007509999999999999)
geometry.add_edge(0.005008617929673261, 0.007509999999999999, 0.005008617929673261, 0.00601)
geometry.add_edge(0.0074025015589529505, 0.007509999999999999, 0.00840250155895295, 0.007509999999999999)
geometry.add_edge(0.00840250155895295, 0.007509999999999999, 0.00840250155895295, 0.009009999999999999)
geometry.add_edge(0.00840250155895295, 0.009009999999999999, 0.0074025015589529505, 0.009009999999999999)
geometry.add_edge(0.0074025015589529505, 0.009009999999999999, 0.0074025015589529505, 0.007509999999999999)
geometry.add_edge(0.012078473883920271, 0.00901, 0.01307847388392027, 0.00901)
geometry.add_edge(0.01307847388392027, 0.00901, 0.01307847388392027, 0.01051)
geometry.add_edge(0.01307847388392027, 0.01051, 0.012078473883920271, 0.01051)
geometry.add_edge(0.012078473883920271, 0.01051, 0.012078473883920271, 0.00901)
geometry.add_edge(0.008671104511185352, 0.01051, 0.00967110451118535, 0.01051)
geometry.add_edge(0.00967110451118535, 0.01051, 0.00967110451118535, 0.01201)
geometry.add_edge(0.00967110451118535, 0.01201, 0.008671104511185352, 0.01201)
geometry.add_edge(0.008671104511185352, 0.01201, 0.008671104511185352, 0.01051)
geometry.add_edge(0.015494575926938942, 0.01201, 0.016494575926938943, 0.01201)
geometry.add_edge(0.016494575926938943, 0.01201, 0.016494575926938943, 0.01351)
geometry.add_edge(0.016494575926938943, 0.01351, 0.015494575926938942, 0.01351)
geometry.add_edge(0.015494575926938942, 0.01351, 0.015494575926938942, 0.01201)
geometry.add_edge(0.009565487199551458, 0.01351, 0.010565487199551457, 0.01351)
geometry.add_edge(0.010565487199551457, 0.01351, 0.010565487199551457, 0.015009999999999999)
geometry.add_edge(0.010565487199551457, 0.015009999999999999, 0.009565487199551458, 0.015009999999999999)
geometry.add_edge(0.009565487199551458, 0.015009999999999999, 0.009565487199551458, 0.01351)

# BLOCK LABELS
geometry.add_label(0.010457628346892456, 0.00076, materials = {'magnetic' : 'turn_0'})
labels.append((0.010457628346892456, 0.00076))
geometry.add_label(0.0076226002769964425, 0.0022600000000000003, materials = {'magnetic' : 'turn_1'})
labels.append((0.0076226002769964425, 0.0022600000000000003))
geometry.add_label(0.013098404813831035, 0.0037600000000000003, materials = {'magnetic' : 'turn_2'})
labels.append((0.013098404813831035, 0.0037600000000000003))
geometry.add_label(0.00839388600983803, 0.00526, materials = {'magnetic' : 'turn_3'})
labels.append((0.00839388600983803, 0.00526))
geometry.add_label(0.005508617929673261, 0.0067599999999999995, materials = {'magnetic' : 'turn_4'})
labels.append((0.005508617929673261, 0.0067599999999999995))
geometry.add_label(0.00790250155895295, 0.008259999999999998, materials = {'magnetic' : 'turn_5'})
labels.append((0.00790250155895295, 0.008259999999999998))
geometry.add_label(0.01257847388392027, 0.00976, materials = {'magnetic' : 'turn_6'})
labels.append((0.01257847388392027, 0.00976))
geometry.add_label(0.00917110451118535, 0.011260000000000001, materials = {'magnetic' : 'turn_7'})
labels.append((0.00917110451118535, 0.011260000000000001))
geometry.add_label(0.015994575926938943, 0.01276, materials = {'magnetic' : 'turn_8'})
labels.append((0.015994575926938943, 0.01276))
geometry.add_label(0.010065487199551457, 0.014259999999999998, materials = {'magnetic' : 'turn_9'})
labels.append((0.010065487199551457, 0.014259999999999998))
geometry.add_label(0.001, 0.001, materials = {'magnetic' : 'air'})
labels.append((0.001, 0.001))

# SOLVE
problem.solve()
a2d.view.zoom_best_fit()
f = open(r"/home/kuczmann/ESCO2022-TEAM35/src/snapshots/ffdd27ce-27b6-48a8-ab86-0925d061383b/S_ffdd27ce-27b6-48a8-ab86-0925d061383b.csv", "w")

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
