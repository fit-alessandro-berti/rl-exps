import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[])
root.order = set()

# Add activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structural Audit': Transition(label='Structural Audit'),
    'Modular Design': Transition(label='Modular Design'),
    'Hydroponic Setup': Transition(label='Hydroponic Setup'),
    'Climate Config': Transition(label='Climate Config'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Pest Detect': Transition(label='Pest Detect'),
    'Lighting Setup': Transition(label='Lighting Setup'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Automation Install': Transition(label='Automation Install'),
    'Staff Training': Transition(label='Staff Training'),
    'Market Analysis': Transition(label='Market Analysis'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Yield Monitor': Transition(label='Yield Monitor'),
    'Waste Manage': Transition(label='Waste Manage'),
    'Data Analytics': Transition(label='Data Analytics')
}

# Add the activities to the root model
for activity in activities.values():
    root.nodes.append(activity)

# Define the partial order
root.order.add_edge(activities['Site Survey'], activities['Structural Audit'])
root.order.add_edge(activities['Structural Audit'], activities['Modular Design'])
root.order.add_edge(activities['Modular Design'], activities['Hydroponic Setup'])
root.order.add_edge(activities['Hydroponic Setup'], activities['Climate Config'])
root.order.add_edge(activities['Climate Config'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Pest Detect'])
root.order.add_edge(activities['Pest Detect'], activities['Lighting Setup'])
root.order.add_edge(activities['Lighting Setup'], activities['Energy Audit'])
root.order.add_edge(activities['Energy Audit'], activities['Automation Install'])
root.order.add_edge(activities['Automation Install'], activities['Staff Training'])
root.order.add_edge(activities['Staff Training'], activities['Market Analysis'])
root.order.add_edge(activities['Market Analysis'], activities['Regulation Check'])
root.order.add_edge(activities['Regulation Check'], activities['Yield Monitor'])
root.order.add_edge(activities['Yield Monitor'], activities['Waste Manage'])
root.order.add_edge(activities['Waste Manage'], activities['Data Analytics'])

# Print the root model
print(root)