import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_analysis = Transition(label='Site Analysis')
structural_check = Transition(label='Structural Check')
rack_install = Transition(label='Rack Install')
system_setup = Transition(label='System Setup')
hydroponics_config = Transition(label='Hydroponics Config')
aeroponics_tune = Transition(label='Aeroponics Tune')
lighting_setup = Transition(label='Lighting Setup')
enviro_control = Transition(label='Enviro Control')
sensor_deploy = Transition(label='Sensor Deploy')
waste_recycle = Transition(label='Waste Recycle')
water_reuse = Transition(label='Water Reuse')
staff_training = Transition(label='Staff Training')
test_grow = Transition(label='Test Grow')
data_analytics = Transition(label='Data Analytics')
yield_optimize = Transition(label='Yield Optimize')

# Define silent activities (tau labels)
skip = SilentTransition()

# Define the loop node for waste recycle and water reuse
loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, water_reuse])

# Define the exclusive choice node for sensor deploy and staff training
xor = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, staff_training])

# Define the exclusive choice node for test grow and data analytics
xor2 = OperatorPOWL(operator=Operator.XOR, children=[test_grow, data_analytics])

# Define the loop node for hydroponics and aeroponics
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[hydroponics_config, aeroponics_tune])

# Define the loop node for lighting setup and enviro control
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[lighting_setup, enviro_control])

# Define the loop node for site analysis and structural check
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, structural_check])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor, xor2, loop2, loop3, loop4, system_setup])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, system_setup)
root.order.add_edge(system_setup, loop2)
root.order.add_edge(system_setup, loop3)
root.order.add_edge(system_setup, loop4)

# Print the root POWL model
print(root)