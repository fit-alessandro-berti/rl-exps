import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = ['Intake Document', 'Visual Inspect', 'Imaging Scan', 'Material Test', 'Database Cross',
              'Provenance Check', 'Expert Consult', 'Carbon Dating', 'Forensic Analyze', 'Anomaly Review',
              'Risk Assess', 'Report Draft', 'Insurance Quote', 'Storage Plan', 'Final Approval']

# Create transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Define the POWL model
root = StrictPartialOrder()

# Add activities to the root
for activity in activities:
    root.nodes.append(transitions[activity])

# Define dependencies between activities
dependencies = [
    ('Intake Document', 'Visual Inspect'),
    ('Visual Inspect', 'Imaging Scan'),
    ('Visual Inspect', 'Material Test'),
    ('Imaging Scan', 'Database Cross'),
    ('Material Test', 'Provenance Check'),
    ('Provenance Check', 'Expert Consult'),
    ('Expert Consult', 'Carbon Dating'),
    ('Carbon Dating', 'Forensic Analyze'),
    ('Forensic Analyze', 'Anomaly Review'),
    ('Anomaly Review', 'Risk Assess'),
    ('Risk Assess', 'Report Draft'),
    ('Report Draft', 'Insurance Quote'),
    ('Insurance Quote', 'Storage Plan'),
    ('Storage Plan', 'Final Approval')
]

# Add edges to the root based on dependencies
for source, target in dependencies:
    root.order.add_edge(transitions[source], transitions[target])

# Print the final POWL model
print(root)