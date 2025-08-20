import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
FileComplaint = Transition(label='File complaint')
LogComplaint = Transition(label='Log complaint')
AssignComplaint = Transition(label='Assign complaint to relevant department')
ReviewDetails = Transition(label='Review complaint details')
ApproveNotify = Transition(label='Approve and notify customer')
RejectNotify = Transition(label='Reject and notify customer')
ProcessRefund = Transition(label='Process reimbursement')
ResolveComplaint = Transition(label='Resolve complaint')
ProvideFeedback = Transition(label='Provide feedback')

# Define a silent transition for when a refund is not approved
NoRefund = SilentTransition()

# Define the loop structure for processing refunds
RefundLoop = OperatorPOWL(operator=Operator.LOOP, children=[ProcessRefund, ResolveComplaint])

# Define the XOR choice for approving or rejecting the complaint
ApprovalChoice = OperatorPOWL(operator=Operator.XOR, children=[ApproveNotify, RejectNotify])

# Define the sequence of events after logging the complaint
ComplaintProcessing = StrictPartialOrder(nodes=[AssignComplaint, ReviewDetails, ApprovalChoice])
ComplaintProcessing.order.add_edge(AssignComplaint, ReviewDetails)
ComplaintProcessing.order.add_edge(ReviewDetails, ApprovalChoice)

# Define the main sequence of events in the process
MainSequence = StrictPartialOrder(nodes=[FileComplaint, LogComplaint, ComplaintProcessing, RefundLoop, ResolveComplaint, ProvideFeedback])
MainSequence.order.add_edge(FileComplaint, LogComplaint)
MainSequence.order.add_edge(LogComplaint, ComplaintProcessing)
MainSequence.order.add_edge(ComplaintProcessing, RefundLoop)
MainSequence.order.add_edge(RefundLoop, ResolveComplaint)
MainSequence.order.add_edge(ResolveComplaint, ProvideFeedback)

# Define the final POWL model
root = MainSequence