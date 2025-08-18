import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as Transition objects
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Plan': Transition(label='Design Plan'),
    'Permit Acquire': Transition(label='Permit Acquire'),
    'Structural Retrofit': Transition(label='Structural Retrofit'),
    'System Install': Transition(label='System Install'),
    'Lighting Setup': Transition(label='Lighting Setup'),
    'Sensor Deploy': Transition(label='Sensor Deploy'),
    'Seed Sourcing': Transition(label='Seed Sourcing'),
    'Nutrient Prep': Transition(label='Nutrient Prep'),
    'Staff Training': Transition(label='Staff Training'),
    'Data Monitor': Transition(label='Data Monitor'),
    'Yield Analyze': Transition(label='Yield Analyze'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Community Meet': Transition(label='Community Meet'),
    'Market Launch': Transition(label='Market Launch'),
    'Logistics Plan': Transition(label='Logistics Plan')
}

# Create the POWL model
root = StrictPartialOrder()
root.nodes.extend(activities.values())

# Define the dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Design Plan'])
root.order.add_edge(activities['Design Plan'], activities['Permit Acquire'])
root.order.add_edge(activities['Permit Acquire'], activities['Structural Retrofit'])
root.order.add_edge(activities['Structural Retrofit'], activities['System Install'])
root.order.add_edge(activities['System Install'], activities['Lighting Setup'])
root.order.add_edge(activities['Lighting Setup'], activities['Sensor Deploy'])
root.order.add_edge(activities['Sensor Deploy'], activities['Seed Sourcing'])
root.order.add_edge(activities['Seed Sourcing'], activities['Nutrient Prep'])
root.order.add_edge(activities['Nutrient Prep'], activities['Staff Training'])
root.order.add_edge(activities['Staff Training'], activities['Data Monitor'])
root.order.add_edge(activities['Data Monitor'], activities['Yield Analyze'])
root.order.add_edge(activities['Yield Analyze'], activities['Compliance Check'])
root.order.add_edge(activities['Compliance Check'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Market Launch'])
root.order.add_edge(activities['Market Launch'], activities['Logistics Plan'])

# Print the POWL model
print(root)