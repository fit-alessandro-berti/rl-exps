import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Env Analysis', 'Structure Build', 'Hydroponics Fit', 'Nutrient Mix', 'Climate Setup', 'Energy Audit', 'Crop Select', 'Pest Control', 'Growth Monitor', 'Harvest Plan', 'Waste Recycle', 'Community Meet', 'Supply Sync', 'Data Review']

# Create transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Define the dependencies between activities
dependencies = {
    'Site Survey': ['Env Analysis'],
    'Env Analysis': ['Structure Build'],
    'Structure Build': ['Hydroponics Fit'],
    'Hydroponics Fit': ['Nutrient Mix'],
    'Nutrient Mix': ['Climate Setup'],
    'Climate Setup': ['Energy Audit'],
    'Energy Audit': ['Crop Select'],
    'Crop Select': ['Pest Control'],
    'Pest Control': ['Growth Monitor'],
    'Growth Monitor': ['Harvest Plan'],
    'Harvest Plan': ['Waste Recycle'],
    'Waste Recycle': ['Community Meet'],
    'Community Meet': ['Supply Sync'],
    'Supply Sync': ['Data Review']
}

# Create a partial order model
root = StrictPartialOrder(nodes=transitions.values())
for source, targets in dependencies.items():
    for target in targets:
        root.order.add_edge(transitions[source], transitions[target])

# Print the root model
print(root)