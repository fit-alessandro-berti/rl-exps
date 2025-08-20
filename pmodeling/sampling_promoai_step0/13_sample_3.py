import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.process_tree.obj import ProcessTree

# Define the POWL model
# Start with the initial activity (customer files a complaint)
file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_department = Transition(label='Assign complaint to relevant department')
review_details = Transition(label='Review complaint details')
approve_and_notify = Transition(label='Approve and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
reject_and_notify = Transition(label='Reject and notify customer')
provide_feedback = Transition(label='Provide feedback')
resolve_complaint = Transition(label='Resolve complaint')

# Define the partial order
root = StrictPartialOrder(nodes=[file_complaint, log_complaint, assign_department, review_details, approve_and_notify, process_reimbursement, reject_and_notify, provide_feedback, resolve_complaint])

# Define the partial order dependencies
root.order.add_edge(file_complaint, log_complaint)
root.order.add_edge(log_complaint, assign_department)
root.order.add_edge(assign_department, review_details)
root.order.add_edge(review_details, approve_and_notify)
root.order.add_edge(review_details, process_reimbursement)
root.order.add_edge(review_details, reject_and_notify)
root.order.add_edge(approve_and_notify, provide_feedback)
root.order.add_edge(approve_and_notify, resolve_complaint)
root.order.add_edge(reject_and_notify, resolve_complaint)
root.order.add_edge(process_reimbursement, provide_feedback)
root.order.add_edge(process_reimbursement, resolve_complaint)

# Print the POWL model
print(root)