import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_complaint = Transition(label='Assign complaint to relevant department')
review_complaint = Transition(label='Review complaint details')
approve_notify = Transition(label='Approve and notify customer')
reject_notify = Transition(label='Reject and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
resolve_complaint = Transition(label='Resolve complaint')
provide_feedback = Transition(label='Provide feedback')

# Define the choice between approving and notifying or rejecting and notifying
choice = OperatorPOWL(operator=Operator.XOR, children=[approve_notify, reject_notify])

# Define the loop for processing reimbursement if approved
loop = OperatorPOWL(operator=Operator.LOOP, children=[process_reimbursement, approve_notify])

# Define the partial order
root = StrictPartialOrder(nodes=[file_complaint, log_complaint, assign_complaint, review_complaint, choice, loop, resolve_complaint, provide_feedback])

# Add edges to define the partial order
root.order.add_edge(file_complaint, log_complaint)
root.order.add_edge(log_complaint, assign_complaint)
root.order.add_edge(assign_complaint, review_complaint)
root.order.add_edge(review_complaint, choice)
root.order.add_edge(choice, loop)
root.order.add_edge(loop, resolve_complaint)
root.order.add_edge(resolve_complaint, provide_feedback)