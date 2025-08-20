import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_department = Transition(label='Assign complaint to relevant department')
review_details = Transition(label='Review complaint details')
approve_notify = Transition(label='Approve and notify customer')
reject_notify = Transition(label='Reject and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
resolve_complaint = Transition(label='Resolve complaint')
provide_feedback = Transition(label='Provide feedback')
skip = SilentTransition()

# Define the choice between approve and reject notifications
notification_choice = OperatorPOWL(operator=Operator.XOR, children=[approve_notify, reject_notify])

# Define the loop for processing reimbursement
reimbursement_loop = OperatorPOWL(operator=Operator.LOOP, children=[process_reimbursement])

# Define the order of operations
order = StrictPartialOrder(nodes=[file_complaint, log_complaint, assign_department, review_details, notification_choice, reimbursement_loop, resolve_complaint, provide_feedback])
order.order.add_edge(file_complaint, log_complaint)
order.order.add_edge(log_complaint, assign_department)
order.order.add_edge(assign_department, review_details)
order.order.add_edge(review_details, notification_choice)
order.order.add_edge(notification_choice, reimbursement_loop)
order.order.add_edge(reimbursement_loop, resolve_complaint)
order.order.add_edge(resolve_complaint, provide_feedback)

# Define the root as the order of operations
root = order