from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A1 = Transition(label='Site Survey')
A2 = Transition(label='Load Test')
A3 = Transition(label='Climate Study')
A4 = Transition(label='Permit Check')
A5 = Transition(label='System Design')
A6 = Transition(label='Equipment Buy')
A7 = Transition(label='Sensor Setup')
A8 = Transition(label='Irrigation Fit')
A9 = Transition(label='Solar Install')
A10 = Transition(label='Staff Train')
A11 = Transition(label='Pilot Plant')
A12 = Transition(label='Data Monitor')
A13 = Transition(label='Crop Harvest')
A14 = Transition(label='Maintenance Plan')
A15 = Transition(label='Community Meet')

# Define silent activities
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[A4, A5])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[A12, A13])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[A14, A15])

# Define choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[A1, A2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[A3, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[A6, A7])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[A8, A9])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[A10, A11])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, loop1, xor3, xor4, xor5, loop2, loop3])

# Define the partial order dependencies
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop1)
root.order.add_edge(loop1, xor3)
root.order.add_edge(xor3, loop2)
root.order.add_edge(loop2, xor4)
root.order.add_edge(xor4, loop3)
root.order.add_edge(loop3, xor5)
root.order.add_edge(xor5, loop2)

# Print the root POWL model
print(root)