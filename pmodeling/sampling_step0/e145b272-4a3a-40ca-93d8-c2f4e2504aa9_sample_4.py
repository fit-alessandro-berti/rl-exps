import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.log.obj import EventLog, Trace, Event

# Define the activities
activities = ['Site Survey', 'System Design', 'Permit Filing', 'Modular Build', 'Sensor Install', 'Climate Setup', 'Nutrient Mix', 'Waste Setup', 'IoT Deploy', 'AI Scheduling', 'Energy Audit', 'Compliance Check', 'Crop Planting', 'Yield Monitor', 'Data Analysis', 'System Upgrade']

# Create the transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Create the POWL model
root = StrictPartialOrder(nodes=transitions)

# Define the dependencies
dependencies = [
    ('Site Survey', 'System Design'),
    ('System Design', 'Permit Filing'),
    ('Permit Filing', 'Modular Build'),
    ('Modular Build', 'Sensor Install'),
    ('Sensor Install', 'Climate Setup'),
    ('Climate Setup', 'Nutrient Mix'),
    ('Nutrient Mix', 'Waste Setup'),
    ('Waste Setup', 'IoT Deploy'),
    ('IoT Deploy', 'AI Scheduling'),
    ('AI Scheduling', 'Energy Audit'),
    ('Energy Audit', 'Compliance Check'),
    ('Compliance Check', 'Crop Planting'),
    ('Crop Planting', 'Yield Monitor'),
    ('Yield Monitor', 'Data Analysis'),
    ('Data Analysis', 'System Upgrade')
]

# Add the dependencies to the POWL model
for source, target in dependencies:
    root.order.add_edge(transitions[activities.index(source)], transitions[activities.index(target)])

# Print the POWL model
print(root)