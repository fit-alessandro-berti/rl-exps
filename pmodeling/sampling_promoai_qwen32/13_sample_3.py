import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_complaint = Transition(label='Assign complaint to relevant department')
review_complaint = Transition(label='Review complaint details')
approve_notify = Transition(label='Approve and notify customer')
reject_notify = Transition(label='Reject and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
provide_feedback = Transition(label='Provide feedback')
resolve_complaint = Transition(label='Resolve complaint')

# Define the POWL model
root = StrictPartialOrder(nodes=[file_complaint, log_complaint, assign_complaint, review_complaint, approve_notify, reject_notify, process_reimbursement, provide_feedback, resolve_complaint])
root.order.add_edge(file_complaint, log_complaint)
root.order.add_edge(log_complaint, assign_complaint)
root.order.add_edge(assign_complaint, review_complaint)
root.order.add_edge(review_complaint, approve_notify)
root.order.add_edge(approve_notify, process_reimbursement)
root.order.add_edge(process_reimbursement, resolve_complaint)
root.order.add_edge(resolve_complaint, provide_feedback)
root.order.add_edge(review_complaint, reject_notify)
root.order.add_edge(reject_notify, resolve_complaint)

# Adding a silent transition to represent the choice between approving and rejecting
skip = SilentTransition()
xor = OperatorPOWL(operator=Operator.XOR, children=[approve_notify, reject_notify])
root.nodes.add(xor)
root.order.add_edge(review_complaint, xor)
root.order.add_edge(xor, approve_notify)
root.order.add_edge(xor, reject_notify)

# Adding a silent transition to represent the choice between processing reimbursement and not processing
skip = SilentTransition()
xor = OperatorPOWL(operator=Operator.XOR, children=[process_reimbursement, skip])
root.nodes.add(xor)
root.order.add_edge(approve_notify, xor)
root.order.add_edge(xor, process_reimbursement)

# Adding a silent transition to represent the choice between providing feedback and not providing
skip = SilentTransition()
xor = OperatorPOWL(operator=Operator.XOR, children=[provide_feedback, skip])
root.nodes.add(xor)
root.order.add_edge(resolve_complaint, xor)
root.order.add_edge(xor, provide_feedback)