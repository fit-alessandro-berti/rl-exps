import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define transitions with no label (silent transitions)
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()

# Define exclusive choice operators
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[structural_check, skip1])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[building_retrofit, skip2])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, skip3])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[climate_control, skip4])
exclusive_choice5 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_design, skip5])

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[staff_hiring, staff_training])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[software_install, system_testing])

# Define partial order
root = StrictPartialOrder(nodes=[site_analysis, zoning_approval, exclusive_choice1, exclusive_choice2, exclusive_choice3, exclusive_choice4, exclusive_choice5, loop1, loop2, crop_planting, growth_monitor, pest_control, harvest_plan])
root.order.add_edge(site_analysis, zoning_approval)
root.order.add_edge(zoning_approval, exclusive_choice1)
root.order.add_edge(exclusive_choice1, exclusive_choice2)
root.order.add_edge(exclusive_choice2, exclusive_choice3)
root.order.add_edge(exclusive_choice3, exclusive_choice4)
root.order.add_edge(exclusive_choice4, exclusive_choice5)
root.order.add_edge(exclusive_choice5, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, crop_planting)
root.order.add_edge(crop_planting, growth_monitor)
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(pest_control, harvest_plan)