from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Load Test': Transition(label='Load Test'),
    'Soil Sample': Transition(label='Soil Sample'),
    'Water Check': Transition(label='Water Check'),
    'Design Plan': Transition(label='Design Plan'),
    'Bed Setup': Transition(label='Bed Setup'),
    'Irrigation Install': Transition(label='Irrigation Install'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Planting Phase': Transition(label='Planting Phase'),
    'Pest Control': Transition(label='Pest Control'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Harvest Prep': Transition(label='Harvest Prep'),
    'Community Meet': Transition(label='Community Meet'),
    'Waste Manage': Transition(label='Waste Manage'),
    'Yield Report': Transition(label='Yield Report')
}

# Define the partial order structure
root = StrictPartialOrder()

# Add the activities to the root
root.add_transition(activities['Site Survey'])
root.add_transition(activities['Load Test'])
root.add_transition(activities['Soil Sample'])
root.add_transition(activities['Water Check'])
root.add_transition(activities['Design Plan'])
root.add_transition(activities['Bed Setup'])
root.add_transition(activities['Irrigation Install'])
root.add_transition(activities['Climate Setup'])
root.add_transition(activities['Seed Selection'])
root.add_transition(activities['Planting Phase'])
root.add_transition(activities['Pest Control'])
root.add_transition(activities['Growth Monitor'])
root.add_transition(activities['Harvest Prep'])
root.add_transition(activities['Community Meet'])
root.add_transition(activities['Waste Manage'])
root.add_transition(activities['Yield Report'])

# Define dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Load Test'])
root.order.add_edge(activities['Site Survey'], activities['Soil Sample'])
root.order.add_edge(activities['Site Survey'], activities['Water Check'])
root.order.add_edge(activities['Site Survey'], activities['Design Plan'])
root.order.add_edge(activities['Load Test'], activities['Bed Setup'])
root.order.add_edge(activities['Soil Sample'], activities['Bed Setup'])
root.order.add_edge(activities['Water Check'], activities['Bed Setup'])
root.order.add_edge(activities['Design Plan'], activities['Bed Setup'])
root.order.add_edge(activities['Bed Setup'], activities['Irrigation Install'])
root.order.add_edge(activities['Bed Setup'], activities['Climate Setup'])
root.order.add_edge(activities['Irrigation Install'], activities['Seed Selection'])
root.order.add_edge(activities['Climate Setup'], activities['Seed Selection'])
root.order.add_edge(activities['Seed Selection'], activities['Planting Phase'])
root.order.add_edge(activities['Planting Phase'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Harvest Prep'])
root.order.add_edge(activities['Harvest Prep'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Waste Manage'])
root.order.add_edge(activities['Waste Manage'], activities['Yield Report'])

print("POWL model generated successfully.")