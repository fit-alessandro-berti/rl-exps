import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Collection Survey', 'Provenance Check', 'Legal Review', 'Scientific Test', 'Material Analysis', 'Ownership Audit', 'Ethical Screening', 'Condition Report', 'Expert Consultation', 'Transport Planning', 'Secure Packing', 'Customs Clearance', 'Insurance Setup', 'Exhibit Preparation', 'Final Approval']

# Create the POWL model
root = StrictPartialOrder(nodes=activities)

# Add edges to define the workflow
# Example: Collection Survey -> Provenance Check
root.order.add_edge(activities[0], activities[1])

# Add more edges as per the process description
# ...

# Print the final POWL model
print(root)