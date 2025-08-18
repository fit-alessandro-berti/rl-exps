import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structural Check': Transition(label='Structural Check'),
    'Resource Sourcing': Transition(label='Resource Sourcing'),
    'System Install': Transition(label='System Install'),
    'Lighting Setup': Transition(label='Lighting Setup'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Stakeholder Meet': Transition(label='Stakeholder Meet'),
    'Volunteer Train': Transition(label='Volunteer Train'),
    'Regulation Review': Transition(label='Regulation Review'),
    'Crop Selection': Transition(label='Crop Selection'),
    'Planting Phase': Transition(label='Planting Phase'),
    'Climate Control': Transition(label='Climate Control'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Data Logging': Transition(label='Data Logging'),
    'Harvest Event': Transition(label='Harvest Event'),
    'Waste Manage': Transition(label='Waste Manage'),
    'Feedback Collect': Transition(label='Feedback Collect')
}

# Define the partial order
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the dependencies
root.order.add_edge(activities['Site Survey'], activities['Structural Check'])
root.order.add_edge(activities['Site Survey'], activities['Resource Sourcing'])
root.order.add_edge(activities['Structural Check'], activities['System Install'])
root.order.add_edge(activities['Resource Sourcing'], activities['System Install'])
root.order.add_edge(activities['System Install'], activities['Lighting Setup'])
root.order.add_edge(activities['System Install'], activities['Irrigation Setup'])
root.order.add_edge(activities['Lighting Setup'], activities['Stakeholder Meet'])
root.order.add_edge(activities['Irrigation Setup'], activities['Stakeholder Meet'])
root.order.add_edge(activities['Stakeholder Meet'], activities['Volunteer Train'])
root.order.add_edge(activities['Stakeholder Meet'], activities['Regulation Review'])
root.order.add_edge(activities['Volunteer Train'], activities['Crop Selection'])
root.order.add_edge(activities['Volunteer Train'], activities['Planting Phase'])
root.order.add_edge(activities['Regulation Review'], activities['Crop Selection'])
root.order.add_edge(activities['Crop Selection'], activities['Planting Phase'])
root.order.add_edge(activities['Planting Phase'], activities['Climate Control'])
root.order.add_edge(activities['Climate Control'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Data Logging'])
root.order.add_edge(activities['Data Logging'], activities['Harvest Event'])
root.order.add_edge(activities['Harvest Event'], activities['Waste Manage'])
root.order.add_edge(activities['Harvest Event'], activities['Feedback Collect'])