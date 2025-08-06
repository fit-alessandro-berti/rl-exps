from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = ['Provenance Check', 'Material Scan', 'Context Review', 'Expert Consult', 'Image Capture', 'Condition Test', 'Forgery Risk', 'Registry Crosscheck', 'Legal Verify', 'Ethics Review', 'Report Draft', 'Certificate Issue', 'Digital Archive', 'Transfer Setup', 'Final Approval']
activities_transitions = [Transition(label=activity) for activity in activities]

# Define the partial order
root = StrictPartialOrder(nodes=activities_transitions)

# Add dependencies between activities
root.order.add_edge(activities_transitions[0], activities_transitions[1])  # Provenance Check -> Material Scan
root.order.add_edge(activities_transitions[1], activities_transitions[2])  # Material Scan -> Context Review
root.order.add_edge(activities_transitions[2], activities_transitions[3])  # Context Review -> Expert Consult
root.order.add_edge(activities_transitions[3], activities_transitions[4])  # Expert Consult -> Image Capture
root.order.add_edge(activities_transitions[4], activities_transitions[5])  # Image Capture -> Condition Test
root.order.add_edge(activities_transitions[5], activities_transitions[6])  # Condition Test -> Forging Risk
root.order.add_edge(activities_transitions[6], activities_transitions[7])  # Forging Risk -> Registry Crosscheck
root.order.add_edge(activities_transitions[7], activities_transitions[8])  # Registry Crosscheck -> Legal Verify
root.order.add_edge(activities_transitions[8], activities_transitions[9])  # Legal Verify -> Ethics Review
root.order.add_edge(activities_transitions[9], activities_transitions[10])  # Ethics Review -> Report Draft
root.order.add_edge(activities_transitions[10], activities_transitions[11])  # Report Draft -> Certificate Issue
root.order.add_edge(activities_transitions[11], activities_transitions[12])  # Certificate Issue -> Digital Archive
root.order.add_edge(activities_transitions[12], activities_transitions[13])  # Digital Archive -> Transfer Setup
root.order.add_edge(activities_transitions[13], activities_transitions[14])  # Transfer Setup -> Final Approval

# Print the root POWL model
print(root)