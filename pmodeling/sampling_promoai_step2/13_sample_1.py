import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_to_department = Transition(label='Assign complaint to relevant department')
review_details = Transition(label='Review complaint details')
approve_and_notify = Transition(label='Approve and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
reject_and_notify = Transition(label='Reject and notify customer')
provide_feedback = Transition(label='Provide feedback')
resolve_complaint = Transition(label='Resolve complaint')

# Define the relationships between the activities
root = StrictPartialOrder(nodes=[
    file_complaint,
    log_complaint,
    assign_to_department,
    review_details,
    approve_and_notify,
    process_reimbursement,
    reject_and_notify,
    provide_feedback,
    resolve_complaint
])

root.order.add_edge(file_complaint, log_complaint)
root.order.add_edge(log_complaint, assign_to_department)
root.order.add_edge(assign_to_department, review_details)
root.order.add_edge(review_details, approve_and_notify)
root.order.add_edge(review_details, reject_and_notify)
root.order.add_edge(approve_and_notify, process_reimbursement)
root.order.add_edge(reject_and_notify, process_reimbursement)
root.order.add_edge(process_reimbursement, resolve_complaint)
root.order.add_edge(resolve_complaint, provide_feedback)

# The final result is in the 'root' variable