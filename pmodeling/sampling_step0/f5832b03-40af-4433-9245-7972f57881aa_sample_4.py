import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'Legal Review': Transition(label='Legal Review'),
    'Tech Sourcing': Transition(label='Tech Sourcing'),
    'Structural Build': Transition(label='Structural Build'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Irrigation Install': Transition(label='Irrigation Install'),
    'Sensor Deploy': Transition(label='Sensor Deploy'),
    'Crop Select': Transition(label='Crop Select'),
    'Nutrient Prep': Transition(label='Nutrient Prep'),
    'Waste System': Transition(label='Waste System'),
    'Automation Config': Transition(label='Automation Config'),
    'Trial Growth': Transition(label='Trial Growth'),
    'Data Analysis': Transition(label='Data Analysis'),
    'Quality Audit': Transition(label='Quality Audit'),
    'Stakeholder Meet': Transition(label='Stakeholder Meet'),
    'Compliance Check': Transition(label='Compliance Check')
}

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(nodes=[
    activities['Site Survey'],
    activities['Design Layout'],
    activities['Legal Review'],
    activities['Tech Sourcing'],
    activities['Structural Build'],
    activities['Climate Setup'],
    activities['Irrigation Install'],
    activities['Sensor Deploy'],
    activities['Crop Select'],
    activities['Nutrient Prep'],
    activities['Waste System'],
    activities['Automation Config'],
    activities['Trial Growth'],
    activities['Data Analysis'],
    activities['Quality Audit'],
    activities['Stakeholder Meet'],
    activities['Compliance Check']
])

# Define the partial order dependencies
root.order.add_edge(activities['Site Survey'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['Legal Review'])
root.order.add_edge(activities['Legal Review'], activities['Tech Sourcing'])
root.order.add_edge(activities['Tech Sourcing'], activities['Structural Build'])
root.order.add_edge(activities['Structural Build'], activities['Climate Setup'])
root.order.add_edge(activities['Climate Setup'], activities['Irrigation Install'])
root.order.add_edge(activities['Irrigation Install'], activities['Sensor Deploy'])
root.order.add_edge(activities['Sensor Deploy'], activities['Crop Select'])
root.order.add_edge(activities['Crop Select'], activities['Nutrient Prep'])
root.order.add_edge(activities['Nutrient Prep'], activities['Waste System'])
root.order.add_edge(activities['Waste System'], activities['Automation Config'])
root.order.add_edge(activities['Automation Config'], activities['Trial Growth'])
root.order.add_edge(activities['Trial Growth'], activities['Data Analysis'])
root.order.add_edge(activities['Data Analysis'], activities['Quality Audit'])
root.order.add_edge(activities['Quality Audit'], activities['Stakeholder Meet'])
root.order.add_edge(activities['Stakeholder Meet'], activities['Compliance Check'])

# Return the final POWL model
return root