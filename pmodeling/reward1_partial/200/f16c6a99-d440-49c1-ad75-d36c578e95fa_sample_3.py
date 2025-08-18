from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the operators (control-flow)
xor1 = OperatorPOWL(operator=Operator.XOR, children=[crop_select, sensor_deploy])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[system_install, energy_setup])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, pest_control])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, staff_training])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_configure, supply_plan])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[harvest_schedule, quality_audit])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[market_launch, feedback_loop])

# Define the loop (repeated steps)
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, loop1, loop2, loop3, loop4])
root.order.add_edge(site_survey, loop1)
root.order.add_edge(site_survey, loop2)
root.order.add_edge(site_survey, loop3)
root.order.add_edge(site_survey, loop4)

# Print the root POWL model
print(root)