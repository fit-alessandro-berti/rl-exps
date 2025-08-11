import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loops and XORs
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[pest_management, skip])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, skip])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[unit_assembly, system_wiring])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_selection])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[planting_setup, climate_control])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[site_survey, design_layout, material_sourcing, xor_1, xor_2, xor_3, xor_4, loop_1, loop_2, community_meet, compliance_check, expansion_plan])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, xor_1)
root.order.add_edge(material_sourcing, xor_2)
root.order.add_edge(material_sourcing, xor_3)
root.order.add_edge(material_sourcing, xor_4)
root.order.add_edge(xor_1, unit_assembly)
root.order.add_edge(xor_1, system_wiring)
root.order.add_edge(xor_2, sensor_install)
root.order.add_edge(xor_2, water_testing)
root.order.add_edge(xor_3, nutrient_mix)
root.order.add_edge(xor_3, seed_selection)
root.order.add_edge(xor_4, planting_setup)
root.order.add_edge(xor_4, climate_control)
root.order.add_edge(climate_control, loop_1)
root.order.add_edge(climate_control, loop_2)
root.order.add_edge(loop_1, pest_management)
root.order.add_edge(loop_1, skip)
root.order.add_edge(loop_2, community_meet)
root.order.add_edge(loop_2, compliance_check)
root.order.add_edge(loop_2, expansion_plan)

print(root)