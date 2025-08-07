import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[])

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Light Mapping': Transition(label='Light Mapping'),
    'Water Testing': Transition(label='Water Testing'),
    'Design Modules': Transition(label='Design Modules'),
    'IoT Setup': Transition(label='IoT Setup'),
    'Sensor Calibration': Transition(label='Sensor Calibration'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Climate Control': Transition(label='Climate Control'),
    'Regulatory Check': Transition(label='Regulatory Check'),
    'Community Meet': Transition(label='Community Meet'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Staff Training': Transition(label='Staff Training'),
    'Installation': Transition(label='Installation'),
    'System Testing': Transition(label='System Testing'),
    'Yield Analysis': Transition(label='Yield Analysis'),
    'Resource Audit': Transition(label='Resource Audit'),
    'Impact Review': Transition(label='Impact Review')
}

# Define the edges
edges = [
    ('Site Survey', 'Light Mapping'),
    ('Site Survey', 'Water Testing'),
    ('Light Mapping', 'Design Modules'),
    ('Water Testing', 'Design Modules'),
    ('Design Modules', 'IoT Setup'),
    ('IoT Setup', 'Sensor Calibration'),
    ('Sensor Calibration', 'Nutrient Mix'),
    ('Nutrient Mix', 'Climate Control'),
    ('Climate Control', 'Regulatory Check'),
    ('Regulatory Check', 'Community Meet'),
    ('Community Meet', 'Energy Audit'),
    ('Energy Audit', 'Staff Training'),
    ('Staff Training', 'Installation'),
    ('Installation', 'System Testing'),
    ('System Testing', 'Yield Analysis'),
    ('Yield Analysis', 'Resource Audit'),
    ('Resource Audit', 'Impact Review')
]

# Add activities to the root model
for activity in activities.values():
    root.nodes.append(activity)

# Add edges to the root model
for edge in edges:
    root.order.add_edge(edge[0], edge[1])

# Print the root model
print(root)