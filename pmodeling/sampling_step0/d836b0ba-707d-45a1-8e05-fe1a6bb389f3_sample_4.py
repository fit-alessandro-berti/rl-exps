import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Select': Transition(label='Site Select'),
    'Design Layout': Transition(label='Design Layout'),
    'Sensor Integrate': Transition(label='Sensor Integrate'),
    'Crop Choose': Transition(label='Crop Choose'),
    'Soil Prepare': Transition(label='Soil Prepare'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Pest Control': Transition(label='Pest Control'),
    'Lighting Install': Transition(label='Lighting Install'),
    'Staff Train': Transition(label='Staff Train'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Market Analyze': Transition(label='Market Analyze'),
    'Package Design': Transition(label='Package Design'),
    'Logistics Plan': Transition(label='Logistics Plan'),
    'Data Analyze': Transition(label='Data Analyze'),
    'Feedback Loop': Transition(label='Feedback Loop')
}

# Define the dependencies between activities
dependencies = [
    ('Site Select', 'Design Layout'),
    ('Design Layout', 'Sensor Integrate'),
    ('Sensor Integrate', 'Crop Choose'),
    ('Crop Choose', 'Soil Prepare'),
    ('Soil Prepare', 'Irrigation Setup'),
    ('Irrigation Setup', 'Pest Control'),
    ('Pest Control', 'Lighting Install'),
    ('Lighting Install', 'Staff Train'),
    ('Staff Train', 'Compliance Check'),
    ('Compliance Check', 'Market Analyze'),
    ('Market Analyze', 'Package Design'),
    ('Package Design', 'Logistics Plan'),
    ('Logistics Plan', 'Data Analyze'),
    ('Data Analyze', 'Feedback Loop')
]

# Create the root node
root = StrictPartialOrder(nodes=[activities['Site Select'], activities['Design Layout'], activities['Sensor Integrate'], activities['Crop Choose'], activities['Soil Prepare'], activities['Irrigation Setup'], activities['Pest Control'], activities['Lighting Install'], activities['Staff Train'], activities['Compliance Check'], activities['Market Analyze'], activities['Package Design'], activities['Logistics Plan'], activities['Data Analyze'], activities['Feedback Loop']])

# Add the dependencies to the root node
for dep in dependencies:
    root.order.add_edge(dep[0], dep[1])

# Print the root node
print(root)