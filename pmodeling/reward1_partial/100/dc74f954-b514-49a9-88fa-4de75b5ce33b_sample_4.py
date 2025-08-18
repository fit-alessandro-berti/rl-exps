from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'Permit Filing': Transition(label='Permit Filing'),
    'Module Build': Transition(label='Module Build'),
    'System Install': Transition(label='System Install'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Lighting Configure': Transition(label='Lighting Configure'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Pest Check': Transition(label='Pest Check'),
    'Sensor Calibrate': Transition(label='Sensor Calibrate'),
    'Data Integration': Transition(label='Data Integration'),
    'Crop Planting': Transition(label='Crop Planting'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Yield Analyze': Transition(label='Yield Analyze'),
    'Waste Manage': Transition(label='Waste Manage'),
    'Energy Audit': Transition(label='Energy Audit')
}

# Define the dependencies
dependencies = [
    ('Site Survey', 'Design Layout'),
    ('Design Layout', 'Permit Filing'),
    ('Permit Filing', 'Module Build'),
    ('Module Build', 'System Install'),
    ('System Install', 'Climate Setup'),
    ('Climate Setup', 'Lighting Configure'),
    ('Lighting Configure', 'Irrigation Setup'),
    ('Irrigation Setup', 'Nutrient Mix'),
    ('Nutrient Mix', 'Pest Check'),
    ('Pest Check', 'Sensor Calibrate'),
    ('Sensor Calibrate', 'Data Integration'),
    ('Data Integration', 'Crop Planting'),
    ('Crop Planting', 'Growth Monitor'),
    ('Growth Monitor', 'Yield Analyze'),
    ('Yield Analyze', 'Waste Manage'),
    ('Waste Manage', 'Energy Audit')
]

# Create the POWL model
root = StrictPartialOrder(nodes=[activities[activity] for activity in activities])
for source, target in dependencies:
    root.order.add_edge(activities[source], activities[target])

# Print the result
print(root)