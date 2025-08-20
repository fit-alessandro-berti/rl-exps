import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_complaint = Transition(label='Assign complaint to relevant department')
review_complaint_details = Transition(label='Review complaint details')
approve_and_notify_customer = Transition(label='Approve and notify customer')
reject_and_notify_customer = Transition(label='Reject and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
resolve_complaint = Transition(label='Resolve complaint')
provide_feedback = Transition(label='Provide feedback')

# Define silent transitions
skip = SilentTransition()

# Define the loop structure for processing reimbursement
loop_process_reimbursement = OperatorPOWL(operator=Operator.LOOP, children=[process_reimbursement])

# Define the XOR choice between approving or rejecting the complaint
xor_approve_or_reject = OperatorPOWL(operator=Operator.XOR, children=[approve_and_notify_customer, reject_and_notify_customer])

# Define the partial order for the main process
root = StrictPartialOrder(nodes=[file_complaint, log_complaint, assign_complaint, review_complaint_details, xor_approve_or_reject, loop_process_reimbursement, resolve_complaint, provide_feedback])

# Define the order of execution
root.order.add_edge(file_complaint, log_complaint)
root.order.add_edge(log_complaint, assign_complaint)
root.order.add_edge(assign_complaint, review_complaint_details)
root.order.add_edge(review_complaint_details, xor_approve_or_reject)
root.order.add_edge(xor_approve_or_reject, loop_process_reimbursement)
root.order.add_edge(loop_process_reimbursement, resolve_complaint)
root.order.add_edge(resolve_complaint, provide_feedback)