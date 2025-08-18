from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities with exact names
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structural Audit': Transition(label='Structural Audit'),
    'System Design': Transition(label='System Design'),
    'Permit Filing': Transition(label='Permit Filing'),
    'Foundation Prep': Transition(label='Foundation Prep'),
    'Frame Build': Transition(label='Frame Build'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Lighting Install': Transition(label='Lighting Install'),
    'Climate Control': Transition(label='Climate Control'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Crop Planting': Transition(label='Crop Planting'),
    'Pest Scouting': Transition(label='Pest Scouting'),
    'Data Monitoring': Transition(label='Data Monitoring'),
    'Waste Sorting': Transition(label='Waste Sorting'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Community Meet': Transition(label='Community Meet'),
    'Yield Analysis': Transition(label='Yield Analysis')
}

# Define the POWL model
root = StrictPartialOrder()

# Define the dependencies
root.order.add_edge(activities['Site Survey'], activities['Structural Audit'])
root.order.add_edge(activities['Structural Audit'], activities['System Design'])
root.order.add_edge(activities['System Design'], activities['Permit Filing'])
root.order.add_edge(activities['Permit Filing'], activities['Foundation Prep'])
root.order.add_edge(activities['Foundation Prep'], activities['Frame Build'])
root.order.add_edge(activities['Frame Build'], activities['Irrigation Setup'])
root.order.add_edge(activities['Irrigation Setup'], activities['Lighting Install'])
root.order.add_edge(activities['Lighting Install'], activities['Climate Control'])
root.order.add_edge(activities['Climate Control'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Crop Planting'])
root.order.add_edge(activities['Crop Planting'], activities['Pest Scouting'])
root.order.add_edge(activities['Pest Scouting'], activities['Data Monitoring'])
root.order.add_edge(activities['Data Monitoring'], activities['Waste Sorting'])
root.order.add_edge(activities['Waste Sorting'], activities['Energy Audit'])
root.order.add_edge(activities['Energy Audit'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Yield Analysis'])

# Add the dependencies for the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[activities['Yield Analysis'], activities['Community Meet']])
root.order.add_edge(loop, activities['Yield Analysis'])

# Add the dependencies for the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[activities['Yield Analysis'], activities['Community Meet']])
root.order.add_edge(xor, activities['Yield Analysis'])

# Add the dependencies for the partial order
root.order.add_edge(root, xor)
root.order.add_edge(xor, loop)

# Print the result
print(root)