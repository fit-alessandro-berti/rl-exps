import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
sensor_deploy = Transition(label='Sensor Deploy')
crop_select = Transition(label='Crop Select')
system_install = Transition(label='System Install')
energy_setup = Transition(label='Energy Setup')
water_cycle = Transition(label='Water Cycle')
pest_control = Transition(label='Pest Control')
regulatory_check = Transition(label='Regulatory Check')
staff_training = Transition(label='Staff Training')
data_configure = Transition(label='Data Configure')
supply_plan = Transition(label='Supply Plan')
harvest_schedule = Transition(label='Harvest Schedule')
quality_audit = Transition(label='Quality Audit')
market_launch = Transition(label='Market Launch')
feedback_loop = Transition(label='Feedback Loop')

# Define the silent transition for exiting a loop
skip = SilentTransition()

# Define the partial order model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy, crop_select])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[system_install, energy_setup])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle, pest_control])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_check, staff_training])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[data_configure, supply_plan])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_schedule, quality_audit])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[market_launch, feedback_loop])

# Define the exclusive choice for the regulatory check and staff training
xor1 = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, staff_training])

# Define the exclusive choice for the data configure and supply plan
xor2 = OperatorPOWL(operator=Operator.XOR, children=[data_configure, supply_plan])

# Define the exclusive choice for the harvest schedule and quality audit
xor3 = OperatorPOWL(operator=Operator.XOR, children=[harvest_schedule, quality_audit])

# Define the exclusive choice for the market launch and feedback loop
xor4 = OperatorPOWL(operator=Operator.XOR, children=[market_launch, feedback_loop])

# Define the root partial order model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, xor1, loop5, xor2, loop6, xor3, loop7, xor4])

# Add the dependencies between the partial orders
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, xor1)
root.order.add_edge(xor1, loop5)
root.order.add_edge(loop5, xor2)
root.order.add_edge(xor2, loop6)
root.order.add_edge(loop6, xor3)
root.order.add_edge(xor3, loop7)
root.order.add_edge(loop7, xor4)
root.order.add_edge(xor4, root)

# Print the root partial order model
print(root)