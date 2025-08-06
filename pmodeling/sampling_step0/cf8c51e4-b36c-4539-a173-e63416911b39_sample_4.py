import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis = Transition(label='Site Analysis')
zoning_approval = Transition(label='Zoning Approval')
structural_check = Transition(label='Structural Check')
building_retrofit = Transition(label='Building Retrofit')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_control = Transition(label='Climate Control')
nutrient_design = Transition(label='Nutrient Design')
staff_hiring = Transition(label='Staff Hiring')
staff_training = Transition(label='Staff Training')
software_install = Transition(label='Software Install')
system_testing = Transition(label='System Testing')
crop_planting = Transition(label='Crop Planting')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[structural_check, building_retrofit])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, climate_control, nutrient_design])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[staff_hiring, staff_training])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[software_install, system_testing])

# Define exclusive choice nodes
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[skip, crop_planting])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[skip, harvest_plan])

# Define root
root = StrictPartialOrder(nodes=[site_analysis, zoning_approval, loop_1, loop_2, loop_3, loop_4, xor_1, xor_2, xor_3])
root.order.add_edge(site_analysis, zoning_approval)
root.order.add_edge(zoning_approval, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, loop_4)
root.order.add_edge(loop_4, xor_1)
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, root)