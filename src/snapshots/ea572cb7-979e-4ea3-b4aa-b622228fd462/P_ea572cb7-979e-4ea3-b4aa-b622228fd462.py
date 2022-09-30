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
geometry.add_edge(0.04, 0.025, 0.0, 0.025, boundaries={'magnetic': 'a0'})
geometry.add_edge(0.0, 0.025, 0.0, 0.0, boundaries={'magnetic': 'a0'})
geometry.add_edge(0.04, 0.0, 0.04, 0.025, boundaries={'magnetic': 'a0'})
geometry.add_edge(0.0, 0.0, 0.04, 0.0, boundaries={'magnetic': 'symmetry'})
geometry.add_edge(0.008707358689181627, 1e-05, 0.009707358689181628, 1e-05)
geometry.add_edge(0.009707358689181628, 1e-05, 0.009707358689181628, 0.00151)
geometry.add_edge(0.009707358689181628, 0.00151, 0.008707358689181627, 0.00151)
geometry.add_edge(0.008707358689181627, 0.00151, 0.008707358689181627, 1e-05)
geometry.add_edge(0.006399201967535477, 0.00151, 0.007399201967535477, 0.00151)
geometry.add_edge(0.007399201967535477, 0.00151, 0.007399201967535477, 0.00301)
geometry.add_edge(0.007399201967535477, 0.00301, 0.006399201967535477, 0.00301)
geometry.add_edge(0.006399201967535477, 0.00301, 0.006399201967535477, 0.00151)
geometry.add_edge(0.01367650431448231, 0.00301, 0.014676504314482312, 0.00301)
geometry.add_edge(0.014676504314482312, 0.00301, 0.014676504314482312, 0.00451)
geometry.add_edge(0.014676504314482312, 0.00451, 0.01367650431448231, 0.00451)
geometry.add_edge(0.01367650431448231, 0.00451, 0.01367650431448231, 0.00301)
geometry.add_edge(0.01879671084063169, 0.00451, 0.01979671084063169, 0.00451)
geometry.add_edge(0.01979671084063169, 0.00451, 0.01979671084063169, 0.00601)
geometry.add_edge(0.01979671084063169, 0.00601, 0.01879671084063169, 0.00601)
geometry.add_edge(0.01879671084063169, 0.00601, 0.01879671084063169, 0.00451)
geometry.add_edge(0.01861433530536668, 0.00601, 0.01961433530536668, 0.00601)
geometry.add_edge(0.01961433530536668, 0.00601, 0.01961433530536668, 0.007509999999999999)
geometry.add_edge(0.01961433530536668, 0.007509999999999999, 0.01861433530536668, 0.007509999999999999)
geometry.add_edge(0.01861433530536668, 0.007509999999999999, 0.01861433530536668, 0.00601)
geometry.add_edge(0.006529964441887843, 0.007509999999999999, 0.007529964441887843, 0.007509999999999999)
geometry.add_edge(0.007529964441887843, 0.007509999999999999, 0.007529964441887843, 0.009009999999999999)
geometry.add_edge(0.007529964441887843, 0.009009999999999999, 0.006529964441887843, 0.009009999999999999)
geometry.add_edge(0.006529964441887843, 0.009009999999999999, 0.006529964441887843, 0.007509999999999999)
geometry.add_edge(0.011588700401435316, 0.00901, 0.012588700401435317, 0.00901)
geometry.add_edge(0.012588700401435317, 0.00901, 0.012588700401435317, 0.01051)
geometry.add_edge(0.012588700401435317, 0.01051, 0.011588700401435316, 0.01051)
geometry.add_edge(0.011588700401435316, 0.01051, 0.011588700401435316, 0.00901)
geometry.add_edge(0.012894164381258181, 0.01051, 0.013894164381258182, 0.01051)
geometry.add_edge(0.013894164381258182, 0.01051, 0.013894164381258182, 0.01201)
geometry.add_edge(0.013894164381258182, 0.01201, 0.012894164381258181, 0.01201)
geometry.add_edge(0.012894164381258181, 0.01201, 0.012894164381258181, 0.01051)
geometry.add_edge(0.01659969781047582, 0.01201, 0.01759969781047582, 0.01201)
geometry.add_edge(0.01759969781047582, 0.01201, 0.01759969781047582, 0.01351)
geometry.add_edge(0.01759969781047582, 0.01351, 0.01659969781047582, 0.01351)
geometry.add_edge(0.01659969781047582, 0.01351, 0.01659969781047582, 0.01201)
geometry.add_edge(0.011687033463972228, 0.01351, 0.012687033463972229, 0.01351)
geometry.add_edge(0.012687033463972229, 0.01351, 0.012687033463972229, 0.015009999999999999)
geometry.add_edge(0.012687033463972229, 0.015009999999999999, 0.011687033463972228, 0.015009999999999999)
geometry.add_edge(0.011687033463972228, 0.015009999999999999, 0.011687033463972228, 0.01351)

# BLOCK LABELS
geometry.add_label(0.009207358689181627, 0.00076, materials = {'magnetic' : 'turn_0'})
labels.append((0.009207358689181627, 0.00076))
geometry.add_label(0.006899201967535478, 0.0022600000000000003, materials = {'magnetic' : 'turn_1'})
labels.append((0.006899201967535478, 0.0022600000000000003))
geometry.add_label(0.014176504314482311, 0.0037600000000000003, materials = {'magnetic' : 'turn_2'})
labels.append((0.014176504314482311, 0.0037600000000000003))
geometry.add_label(0.01929671084063169, 0.00526, materials = {'magnetic' : 'turn_3'})
labels.append((0.01929671084063169, 0.00526))
geometry.add_label(0.01911433530536668, 0.0067599999999999995, materials = {'magnetic' : 'turn_4'})
labels.append((0.01911433530536668, 0.0067599999999999995))
geometry.add_label(0.007029964441887844, 0.008259999999999998, materials = {'magnetic' : 'turn_5'})
labels.append((0.007029964441887844, 0.008259999999999998))
geometry.add_label(0.012088700401435316, 0.00976, materials = {'magnetic' : 'turn_6'})
labels.append((0.012088700401435316, 0.00976))
geometry.add_label(0.013394164381258181, 0.011260000000000001, materials = {'magnetic' : 'turn_7'})
labels.append((0.013394164381258181, 0.011260000000000001))
geometry.add_label(0.01709969781047582, 0.01276, materials = {'magnetic' : 'turn_8'})
labels.append((0.01709969781047582, 0.01276))
geometry.add_label(0.012187033463972229, 0.014259999999999998, materials = {'magnetic' : 'turn_9'})
labels.append((0.012187033463972229, 0.014259999999999998))
geometry.add_label(0.001, 0.001, materials = {'magnetic' : 'air'})
labels.append((0.001, 0.001))

# SOLVE
problem.solve()
a2d.view.zoom_best_fit()
f = open(r"/home/kuczmann/ESCO2022-TEAM35/src/snapshots/ea572cb7-979e-4ea3-b4aa-b622228fd462/S_ea572cb7-979e-4ea3-b4aa-b622228fd462.csv", "w")

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
