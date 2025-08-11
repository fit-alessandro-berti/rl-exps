import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Opportunity Scan', 'Idea Workshop', 'Concept Merge', 'Resource Align', 'Prototype Build', 'Feasibility Test', 'Pilot Launch', 'Feedback Gather', 'Design Adapt', 'Compliance Check', 'Scaling Plan', 'IP Management', 'Market Sync', 'Partner Review', 'Exit Strategy']

# Create the transitions
transitions = [Transition(label=activity) for activity in activities]

# Create the partial order model
root = StrictPartialOrder(nodes=transitions)

# Define the dependencies between the transitions
dependencies = [
    ('Opportunity Scan', 'Idea Workshop'),
    ('Idea Workshop', 'Concept Merge'),
    ('Concept Merge', 'Resource Align'),
    ('Resource Align', 'Prototype Build'),
    ('Prototype Build', 'Feasibility Test'),
    ('Feasibility Test', 'Pilot Launch'),
    ('Pilot Launch', 'Feedback Gather'),
    ('Feedback Gather', 'Design Adapt'),
    ('Design Adapt', 'Compliance Check'),
    ('Compliance Check', 'Scaling Plan'),
    ('Scaling Plan', 'IP Management'),
    ('IP Management', 'Market Sync'),
    ('Market Sync', 'Partner Review'),
    ('Partner Review', 'Exit Strategy')
]

# Add the dependencies to the partial order model
for source, target in dependencies:
    root.order.add_edge(transitions[activities.index(source)], transitions[activities.index(target)])

# Print the final model
print(root)