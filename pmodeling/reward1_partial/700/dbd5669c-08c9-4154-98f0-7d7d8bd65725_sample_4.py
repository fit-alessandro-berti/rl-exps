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
transitions = {
    'Site Survey': [activities['Design Layout']],
    'Design Layout': [activities['Material Sourcing']],
    'Material Sourcing': [activities['Unit Assembly']],
    'Unit Assembly': [activities['System Wiring']],
    'System Wiring': [activities['Sensor Install']],
    'Sensor Install': [activities['Water Testing']],
    'Water Testing': [activities['Nutrient Mix']],
    'Nutrient Mix': [activities['Seed Selection']],
    'Seed Selection': [activities['Planting Setup']],
    'Planting Setup': [activities['Climate Control']],
    'Climate Control': [activities['Pest Management']],
    'Pest Management': [activities['Data Calibration']],
    'Data Calibration': [activities['Yield Analysis']],
    'Yield Analysis': [activities['Community Meet']],
    'Community Meet': [activities['Compliance Check']],
    'Compliance Check': [activities['Expansion Plan']]
}

# Create the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))
for source, targets in transitions.items():
    for target in targets:
        root.order.add_edge(activities[source], activities[target])

# Print the POWL model
print(root)