from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the workflow
loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_management, climate_control])
xor = OperatorPOWL(operator=Operator.XOR, children=[yield_analysis, community_meet, compliance_check, expansion_plan])

root = StrictPartialOrder(nodes=[site_survey, design_layout, material_sourcing, unit_assembly, system_wiring, sensor_install, water_testing, nutrient_mix, seed_selection, planting_setup, loop, xor])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, material_sourcing)
root.order.add_edge(material_sourcing, unit_assembly)
root.order.add_edge(unit_assembly, system_wiring)
root.order.add_edge(system_wiring, sensor_install)
root.order.add_edge(sensor_install, water_testing)
root.order.add_edge(water_testing, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, planting_setup)
root.order.add_edge(planting_setup, loop)
root.order.add_edge(loop, xor)