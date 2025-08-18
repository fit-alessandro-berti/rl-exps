import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permits_check = Transition(label='Permits Check')
foundation_prep = Transition(label='Foundation Prep')
frame_assembly = Transition(label='Frame Assembly')
hydro_setup = Transition(label='Hydro Setup')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
system_calibration = Transition(label='System Calibration')
pest_control = Transition(label='Pest Control')
automation_link = Transition(label='Automation Link')
staff_training = Transition(label='Staff Training')
yield_tracking = Transition(label='Yield Tracking')
distribution_plan = Transition(label='Distribution Plan')

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[foundation_prep, frame_assembly, hydro_setup, climate_setup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, nutrient_mix, system_calibration])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, automation_link])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[staff_training, yield_tracking])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, skip])

# Define the root partial order
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3])

# Add edges for dependencies
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)

# Print the root POWL model
print(root)