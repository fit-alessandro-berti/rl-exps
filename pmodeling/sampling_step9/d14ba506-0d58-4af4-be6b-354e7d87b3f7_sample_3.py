import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, structural_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[rack_install, system_setup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[hydroponics_config, aeroponics_tune])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[lighting_setup, enviro_control])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy, waste_recycle])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[water_reuse, staff_training])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[test_grow, data_analytics])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[yield_optimize])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[loop8, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop4)
root.order.add_edge(xor5, loop5)
root.order.add_edge(xor6, loop6)
root.order.add_edge(xor7, loop7)
root.order.add_edge(xor8, loop8)

print(root)