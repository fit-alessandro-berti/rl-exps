from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = ['Provenance Check', 'Condition Scan', 'Material Test', 'Disassembly', 'Surface Clean', 'Structural Repair', 'Reconstruction', 'Finish Match', 'Stabilize Parts', 'Documentation', 'Quality Audit', 'Valuation', 'Market Analysis', 'Target Outreach', 'Delivery Prep', 'Client Feedback']

# Create transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Create the POWL model
root = StrictPartialOrder()

# Add the activities to the root node
for activity in activities:
    root.nodes.append(transitions[activity])

# Define the dependencies between activities
dependencies = [
    ('Provenance Check', 'Condition Scan'),
    ('Condition Scan', 'Material Test'),
    ('Material Test', 'Disassembly'),
    ('Disassembly', 'Surface Clean'),
    ('Surface Clean', 'Structural Repair'),
    ('Structural Repair', 'Reconstruction'),
    ('Reconstruction', 'Finish Match'),
    ('Finish Match', 'Stabilize Parts'),
    ('Stabilize Parts', 'Documentation'),
    ('Documentation', 'Quality Audit'),
    ('Quality Audit', 'Valuation'),
    ('Valuation', 'Market Analysis'),
    ('Market Analysis', 'Target Outreach'),
    ('Target Outreach', 'Delivery Prep'),
    ('Delivery Prep', 'Client Feedback')
]

# Add the dependencies to the root node
for source, target in dependencies:
    root.order.add_edge(transitions[source], transitions[target])

# Print the POWL model
print(root)