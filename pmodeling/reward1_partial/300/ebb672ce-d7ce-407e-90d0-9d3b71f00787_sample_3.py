import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Design Layout', 'Modular Build', 'Install Pumps', 'Setup Sensors', 'Calibrate Lights', 'Nutrient Mix', 'Plant Seeding', 'Water Cycling', 'Energy Audit', 'Pest Control', 'Growth Monitor', 'Data Analysis', 'Yield Forecast', 'Supply Order', 'Waste Recycle', 'System Upgrade']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the partial order structure
root = StrictPartialOrder(nodes=transitions)

# Define the dependencies between activities
dependencies = [
    ('Site Survey', 'Design Layout'),
    ('Design Layout', 'Modular Build'),
    ('Modular Build', 'Install Pumps'),
    ('Install Pumps', 'Setup Sensors'),
    ('Setup Sensors', 'Calibrate Lights'),
    ('Calibrate Lights', 'Nutrient Mix'),
    ('Nutrient Mix', 'Plant Seeding'),
    ('Plant Seeding', 'Water Cycling'),
    ('Water Cycling', 'Energy Audit'),
    ('Energy Audit', 'Pest Control'),
    ('Pest Control', 'Growth Monitor'),
    ('Growth Monitor', 'Data Analysis'),
    ('Data Analysis', 'Yield Forecast'),
    ('Yield Forecast', 'Supply Order'),
    ('Supply Order', 'Waste Recycle'),
    ('Waste Recycle', 'System Upgrade')
]

# Add dependencies to the partial order
for source, target in dependencies:
    root.order.add_edge(source, target)

# Print the result
print(root)