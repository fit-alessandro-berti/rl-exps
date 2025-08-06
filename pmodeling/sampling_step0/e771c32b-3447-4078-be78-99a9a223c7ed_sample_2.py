import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Climate Plan': Transition(label='Climate Plan'),
    'System Design': Transition(label='System Design'),
    'AI Setup': Transition(label='AI Setup'),
    'Seed Sourcing': Transition(label='Seed Sourcing'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Install Hydro': Transition(label='Install Hydro'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Staff Training': Transition(label='Staff Training'),
    'Trial Growth': Transition(label='Trial Growth'),
    'Yield Measure': Transition(label='Yield Measure'),
    'Waste Cycle': Transition(label='Waste Cycle'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Market Study': Transition(label='Market Study'),
    'Community Meet': Transition(label='Community Meet'),
    'Optimize Environment': Transition(label='Optimize Environment')
}

# Define dependencies between activities
dependencies = [
    ('Site Survey', 'Climate Plan'),
    ('Climate Plan', 'System Design'),
    ('System Design', 'AI Setup'),
    ('AI Setup', 'Seed Sourcing'),
    ('Seed Sourcing', 'Nutrient Mix'),
    ('Nutrient Mix', 'Install Hydro'),
    ('Install Hydro', 'Energy Audit'),
    ('Energy Audit', 'Staff Training'),
    ('Staff Training', 'Trial Growth'),
    ('Trial Growth', 'Yield Measure'),
    ('Yield Measure', 'Waste Cycle'),
    ('Waste Cycle', 'Compliance Check'),
    ('Compliance Check', 'Market Study'),
    ('Market Study', 'Community Meet'),
    ('Community Meet', 'Optimize Environment')
]

# Create the POWL model
root = StrictPartialOrder()
for activity, label in activities.items():
    root.add_transition(label)

for source, target in dependencies:
    root.add_transition_edge(source, target)

# Print the POWL model
print(root)