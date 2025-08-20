import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_complaint = Transition(label='Assign complaint to relevant department')
review_details = Transition(label='Review complaint details')
approve_notify = Transition(label='Approve and notify customer')
reject_notify = Transition(label='Reject and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
provide_feedback = Transition(label='Provide feedback')
resolve_complaint = Transition(label='Resolve complaint')
skip = SilentTransition()

# Define the process structure
xor_decision = OperatorPOWL(operator=Operator.XOR, children=[approve_notify, reject_notify])
loop_reimbursement = OperatorPOWL(operator=Operator.LOOP, children=[process_reimbursement, approve_notify])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[provide_feedback, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[file_complaint, log_complaint, assign_complaint, review_details, xor_decision, loop_reimbursement, resolve_complaint, xor_feedback])
root.order.add_edge(file_complaint, log_complaint)
root.order.add_edge(log_complaint, assign_complaint)
root.order.add_edge(assign_complaint, review_details)
root.order.add_edge(review_details, xor_decision)
root.order.add_edge(xor_decision, loop_reimbursement)
root.order.add_edge(loop_reimbursement, resolve_complaint)
root.order.add_edge(resolve_complaint, xor_feedback)