import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_complaint = Transition(label='Assign complaint to relevant department')
review_complaint = Transition(label='Review complaint details')
approve_and_notify = Transition(label='Approve and notify customer')
reject_and_notify = Transition(label='Reject and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
resolve_complaint = Transition(label='Resolve complaint')
provide_feedback = Transition(label='Provide feedback')

# Define the choice between approval and rejection
choice = OperatorPOWL(operator=Operator.XOR, children=[approve_and_notify, reject_and_notify])

# Define the loop for processing the reimbursement
loop = OperatorPOWL(operator=Operator.LOOP, children=[process_reimbursement, resolve_complaint])

# Define the sequence of activities
sequence = StrictPartialOrder(nodes=[file_complaint, log_complaint, assign_complaint, review_complaint, choice, loop, provide_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[sequence])

# Add the edges
root.order.add_edge(file_complaint, log_complaint)
root.order.add_edge(log_complaint, assign_complaint)
root.order.add_edge(assign_complaint, review_complaint)
root.order.add_edge(review_complaint, choice)
root.order.add_edge(choice, loop)
root.order.add_edge(loop, provide_feedback)