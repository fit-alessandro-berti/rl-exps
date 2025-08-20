import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_complaint = Transition(label='Assign complaint to relevant department')
review_complaint_details = Transition(label='Review complaint details')
approve_and_notify_customer = Transition(label='Approve and notify customer')
reject_and_notify_customer = Transition(label='Reject and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
provide_feedback = Transition(label='Provide feedback')
resolve_complaint = Transition(label='Resolve complaint')

# Define the silent activities
skip = SilentTransition()

# Define the loops
loop_review = OperatorPOWL(operator=Operator.LOOP, children=[review_complaint_details])
loop_assign = OperatorPOWL(operator=Operator.LOOP, children=[assign_complaint, loop_review])

# Define the exclusive choice
xor_decision = OperatorPOWL(operator=Operator.XOR, children=[approve_and_notify_customer, reject_and_notify_customer])

# Define the partial order
root = StrictPartialOrder(nodes=[file_complaint, log_complaint, loop_assign, xor_decision, process_reimbursement, provide_feedback, resolve_complaint])
root.order.add_edge(file_complaint, log_complaint)
root.order.add_edge(log_complaint, loop_assign)
root.order.add_edge(loop_assign, xor_decision)
root.order.add_edge(xor_decision, process_reimbursement)
root.order.add_edge(xor_decision, provide_feedback)
root.order.add_edge(process_reimbursement, resolve_complaint)
root.order.add_edge(provide_feedback, resolve_complaint)
root.order.add_edge(resolve_complaint, file_complaint)