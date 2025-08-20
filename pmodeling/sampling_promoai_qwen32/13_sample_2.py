import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
file_complaint = Transition(label='File complaint')
log_complaint = Transition(label='Log complaint')
assign_complaint = Transition(label='Assign complaint to relevant department')
review_details = Transition(label='Review complaint details')
approve_notify = Transition(label='Approve and notify customer')
reject_notify = Transition(label='Reject and notify customer')
process_reimbursement = Transition(label='Process reimbursement')
resolve_complaint = Transition(label='Resolve complaint')
provide_feedback = Transition(label='Provide feedback')

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[review_details, approve_notify, process_reimbursement, resolve_complaint])
choice = OperatorPOWL(operator=Operator.XOR, children=[approve_notify, reject_notify])
root = StrictPartialOrder(nodes=[file_complaint, log_complaint, assign_complaint, loop, choice, resolve_complaint, provide_feedback])
root.order.add_edge(file_complaint, log_complaint)
root.order.add_edge(log_complaint, assign_complaint)
root.order.add_edge(assign_complaint, review_details)
root.order.add_edge(approve_notify, process_reimbursement)
root.order.add_edge(process_reimbursement, resolve_complaint)
root.order.add_edge(reject_notify, resolve_complaint)
root.order.add_edge(resolve_complaint, provide_feedback)

root