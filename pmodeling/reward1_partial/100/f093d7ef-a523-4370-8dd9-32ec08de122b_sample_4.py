from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'Module Build': Transition(label='Module Build'),
    'System Install': Transition(label='System Install'),
    'Water Prep': Transition(label='Water Prep'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Sensor Deploy': Transition(label='Sensor Deploy'),
    'Pest Scan': Transition(label='Pest Scan'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Data Sync': Transition(label='Data Sync'),
    'Energy Manage': Transition(label='Energy Manage'),
    'Harvest Plan': Transition(label='Harvest Plan'),
    'Community Link': Transition(label='Community Link')
}

# Define the POWL model
root = StrictPartialOrder(nodes=activities.values())

# Define dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['Module Build'])
root.order.add_edge(activities['Module Build'], activities['System Install'])
root.order.add_edge(activities['System Install'], activities['Water Prep'])
root.order.add_edge(activities['Water Prep'], activities['Seed Selection'])
root.order.add_edge(activities['Seed Selection'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Climate Setup'])
root.order.add_edge(activities['Climate Setup'], activities['Sensor Deploy'])
root.order.add_edge(activities['Sensor Deploy'], activities['Pest Scan'])
root.order.add_edge(activities['Pest Scan'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Data Sync'])
root.order.add_edge(activities['Data Sync'], activities['Energy Manage'])
root.order.add_edge(activities['Energy Manage'], activities['Harvest Plan'])
root.order.add_edge(activities['Harvest Plan'], activities['Community Link'])

# Print the POWL model
print(root)