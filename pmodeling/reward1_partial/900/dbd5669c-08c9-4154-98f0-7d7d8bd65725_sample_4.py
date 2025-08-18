import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'Material Sourcing': Transition(label='Material Sourcing'),
    'Unit Assembly': Transition(label='Unit Assembly'),
    'System Wiring': Transition(label='System Wiring'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Water Testing': Transition(label='Water Testing'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Planting Setup': Transition(label='Planting Setup'),
    'Climate Control': Transition(label='Climate Control'),
    'Pest Management': Transition(label='Pest Management'),
    'Data Calibration': Transition(label='Data Calibration'),
    'Yield Analysis': Transition(label='Yield Analysis'),
    'Community Meet': Transition(label='Community Meet'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Expansion Plan': Transition(label='Expansion Plan')
}

# Define the transitions
root = StrictPartialOrder(nodes=[activities['Site Survey'], activities['Design Layout'], activities['Material Sourcing'], activities['Unit Assembly'], activities['System Wiring'], activities['Sensor Install'], activities['Water Testing'], activities['Nutrient Mix'], activities['Seed Selection'], activities['Planting Setup'], activities['Climate Control'], activities['Pest Management'], activities['Data Calibration'], activities['Yield Analysis'], activities['Community Meet'], activities['Compliance Check'], activities['Expansion Plan']])

# Define the dependencies
root.order.add_edge(activities['Site Survey'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['Material Sourcing'])
root.order.add_edge(activities['Material Sourcing'], activities['Unit Assembly'])
root.order.add_edge(activities['Unit Assembly'], activities['System Wiring'])
root.order.add_edge(activities['System Wiring'], activities['Sensor Install'])
root.order.add_edge(activities['Sensor Install'], activities['Water Testing'])
root.order.add_edge(activities['Water Testing'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Seed Selection'])
root.order.add_edge(activities['Seed Selection'], activities['Planting Setup'])
root.order.add_edge(activities['Planting Setup'], activities['Climate Control'])
root.order.add_edge(activities['Climate Control'], activities['Pest Management'])
root.order.add_edge(activities['Pest Management'], activities['Data Calibration'])
root.order.add_edge(activities['Data Calibration'], activities['Yield Analysis'])
root.order.add_edge(activities['Yield Analysis'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Compliance Check'])
root.order.add_edge(activities['Compliance Check'], activities['Expansion Plan'])

# Print the POWL model
print(root)