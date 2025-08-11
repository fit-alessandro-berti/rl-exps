import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_complaint = Transition(label='Assign complaint to relevant department')
review_complaint = Transition(label='Review complaint details')
approve_and_notify = Transition(label='Approve and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
reject_and_notify = Transition(label='Reject and notify customer')
resolve_complaint = Transition(label='Resolve complaint')
provide_feedback = Transition(label='Provide feedback')

# Define the POWL model
root = StrictPartialOrder(nodes=[file_complaint, log_complaint, assign_complaint, review_complaint, approve_and_notify, process_reimbursement, reject_and_notify, resolve_complaint, provide_feedback])

# Define the order of the POWL model
root.order.add_edge(file_complaint, log_complaint)
root.order.add_edge(log_complaint, assign_complaint)
root.order.add_edge(assign_complaint, review_complaint)
root.order.add_edge(review_complaint, approve_and_notify)
root.order.add_edge(approve_and_notify, process_reimbursement)
root.order.add_edge(approve_and_notify, reject_and_notify)
root.order.add_edge(reject_and_notify, resolve_complaint)
root.order.add_edge(resolve_complaint, provide_feedback)

# Print the POWL model
print(root)