from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'System Assembly': Transition(label='System Assembly'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Light Calibration': Transition(label='Light Calibration'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Seedling Prep': Transition(label='Seedling Prep'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Data Integration': Transition(label='Data Integration'),
    'Waste Routing': Transition(label='Waste Routing'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Operational Test': Transition(label='Operational Test'),
    'Community Outreach': Transition(label='Community Outreach')
}

# Define the dependencies between activities
dependencies = [
    ('Site Survey', 'Design Layout'),
    ('Design Layout', 'System Assembly'),
    ('System Assembly', 'Climate Setup'),
    ('Climate Setup', 'Light Calibration'),
    ('Light Calibration', 'Seed Selection'),
    ('Seed Selection', 'Seedling Prep'),
    ('Seedling Prep', 'Nutrient Mix'),
    ('Nutrient Mix', 'Irrigation Setup'),
    ('Irrigation Setup', 'Sensor Install'),
    ('Sensor Install', 'Data Integration'),
    ('Data Integration', 'Waste Routing'),
    ('Waste Routing', 'Energy Audit'),
    ('Energy Audit', 'Regulation Check'),
    ('Regulation Check', 'Operational Test'),
    ('Operational Test', 'Community Outreach')
]

# Create the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))
for source, target in dependencies:
    root.order.add_edge(activities[source], activities[target])

# Print the POWL model
print(root)