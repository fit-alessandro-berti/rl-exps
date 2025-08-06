from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
A1 = Transition(label='Site Survey')
A2 = Transition(label='Permit Review')
A3 = Transition(label='Design Layout')
A4 = Transition(label='System Assembly')
A5 = Transition(label='Climate Setup')
A6 = Transition(label='Nutrient Prep')
A7 = Transition(label='Irrigation Test')
A8 = Transition(label='Lighting Config')
A9 = Transition(label='Energy Install')
A10 = Transition(label='Sensor Setup')
A11 = Transition(label='Automation Deploy')
A12 = Transition(label='Crop Seeding')
A13 = Transition(label='Waste Plan')
A14 = Transition(label='Staff Training')
A15 = Transition(label='Community Outreach')
A16 = Transition(label='Yield Monitor')
A17 = Transition(label='Maintenance Check')
skip = SilentTransition()

# Define the workflow
loop = OperatorPOWL(operator=Operator.LOOP, children=[A1, A2])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[A3, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[A4, A5])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[A6, A7])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[A8, A9])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[A10, A11])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[A12, A13])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[A14, A15])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[A16, A17])

# Define the root of the workflow
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

# Print the root of the workflow
print(root)