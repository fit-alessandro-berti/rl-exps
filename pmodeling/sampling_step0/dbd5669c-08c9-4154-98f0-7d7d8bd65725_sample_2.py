import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
unit_assembly = Transition(label='Unit Assembly')
system_wiring = Transition(label='System Wiring')
sensor_install = Transition(label='Sensor Install')
water_testing = Transition(label='Water Testing')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_setup = Transition(label='Planting Setup')
climate_control = Transition(label='Climate Control')
pest_management = Transition(label='Pest Management')
data_calibration = Transition(label='Data Calibration')
yield_analysis = Transition(label='Yield Analysis')
community_meet = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
expansion_plan = Transition(label='Expansion Plan')

# Define silent transitions
skip = SilentTransition()

# Define loop and XOR operations
site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout])
material_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, unit_assembly])
system_wiring_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_wiring, sensor_install])
water_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_testing, nutrient_mix])
seed_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, planting_setup])
climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, pest_management])
data_calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_calibration, yield_analysis])
community_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, compliance_check])
expansion_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[expansion_plan])

# Define XOR operations for concurrent activities
site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, material_sourcing])
material_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[unit_assembly, system_wiring])
system_wiring_xor = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])
water_testing_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_selection])
seed_selection_xor = OperatorPOWL(operator=Operator.XOR, children=[planting_setup, climate_control])
climate_control_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_management, data_calibration])
data_calibration_xor = OperatorPOWL(operator=Operator.XOR, children=[yield_analysis, community_meet])
community_meet_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, expansion_plan])

# Define root POWL model
root = StrictPartialOrder(nodes=[site_survey_loop, material_sourcing_loop, system_wiring_loop, water_testing_loop, seed_selection_loop, climate_control_loop, data_calibration_loop, community_meet_loop, expansion_plan_loop, site_survey_xor, material_sourcing_xor, system_wiring_xor, water_testing_xor, seed_selection_xor, climate_control_xor, data_calibration_xor, community_meet_xor])
root.order.add_edge(site_survey_loop, material_sourcing_loop)
root.order.add_edge(material_sourcing_loop, unit_assembly)
root.order.add_edge(unit_assembly, system_wiring)
root.order.add_edge(system_wiring, sensor_install)
root.order.add_edge(sensor_install, water_testing)
root.order.add_edge(water_testing, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, planting_setup)
root.order.add_edge(planting_setup, climate_control)
root.order.add_edge(climate_control, pest_management)
root.order.add_edge(pest_management, data_calibration)
root.order.add_edge(data_calibration, yield_analysis)
root.order.add_edge(yield_analysis, community_meet)
root.order.add_edge(community_meet, compliance_check)
root.order.add_edge(compliance_check, expansion_plan)

# Print the root POWL model
print(root)