from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Load Test': Transition(label='Load Test'),
    'Permit Review': Transition(label='Permit Review'),
    'Design Layout': Transition(label='Design Layout'),
    'Material Sourcing': Transition(label='Material Sourcing'),
    'Soil Prep': Transition(label='Soil Prep'),
    'Hydroponic Setup': Transition(label='Hydroponic Setup'),
    'Community Meet': Transition(label='Community Meet'),
    'Crop Select': Transition(label='Crop Select'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Water Testing': Transition(label='Water Testing'),
    'Pest Control': Transition(label='Pest Control'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Harvest Plan': Transition(label='Harvest Plan'),
    'Market Launch': Transition(label='Market Launch'),
    'Feedback Collect': Transition(label='Feedback Collect')
}

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[activities['Site Survey'], activities['Load Test']])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[activities['Permit Review'], xor1])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[activities['Design Layout'], activities['Material Sourcing']])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[activities['Soil Prep'], activities['Hydroponic Setup']])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[activities['Community Meet'], activities['Crop Select']])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[activities['Sensor Install'], activities['Water Testing']])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[activities['Pest Control'], activities['Growth Monitor']])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[activities['Harvest Plan'], activities['Market Launch']])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[activities['Feedback Collect'], xor4])

# Define the root node with the control-flow operators
root = StrictPartialOrder(nodes=[xor2, loop1, loop2, xor3, loop3, loop4, xor5])
root.order.add_edge(xor2, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(xor3, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, xor5)

# Print the root node
print(root)