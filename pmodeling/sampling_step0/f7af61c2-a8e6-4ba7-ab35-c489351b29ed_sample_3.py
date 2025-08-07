import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Analysis': Transition(label='Site Analysis'),
    'Structure Check': Transition(label='Structure Check'),
    'Farm Design': Transition(label='Farm Design'),
    'Env Control': Transition(label='Env Control'),
    'Nutrient Prep': Transition(label='Nutrient Prep'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Automated Plant': Transition(label='Automated Plant'),
    'Sensor Setup': Transition(label='Sensor Setup'),
    'Microclimate Mon': Transition(label='Microclimate Mon'),
    'Health Monitor': Transition(label='Health Monitor'),
    'Light Adjust': Transition(label='Light Adjust'),
    'Irrigation Mod': Transition(label='Irrigation Mod'),
    'Waste Recycle': Transition(label='Waste Recycle'),
    'Energy Optimize': Transition(label='Energy Optimize'),
    'Quality Check': Transition(label='Quality Check'),
    'Crop Harvest': Transition(label='Crop Harvest'),
    'Distribution Plan': Transition(label='Distribution Plan')
}

# Define the dependencies
dependencies = [
    ('Site Analysis', 'Structure Check'),
    ('Structure Check', 'Farm Design'),
    ('Farm Design', 'Env Control'),
    ('Env Control', 'Nutrient Prep'),
    ('Nutrient Prep', 'Seed Selection'),
    ('Seed Selection', 'Automated Plant'),
    ('Automated Plant', 'Sensor Setup'),
    ('Sensor Setup', 'Microclimate Mon'),
    ('Microclimate Mon', 'Health Monitor'),
    ('Health Monitor', 'Light Adjust'),
    ('Light Adjust', 'Irrigation Mod'),
    ('Irrigation Mod', 'Waste Recycle'),
    ('Waste Recycle', 'Energy Optimize'),
    ('Energy Optimize', 'Quality Check'),
    ('Quality Check', 'Crop Harvest'),
    ('Crop Harvest', 'Distribution Plan')
]

# Create the POWL model
root = StrictPartialOrder()
for activity in activities.values():
    root.add_node(activity)

for source, target in dependencies:
    root.add_edge(activities[source], activities[target])

# Print the root node
print(root)