import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
OutlineObjectives = Transition(label='Outline objectives')
DraftPlan = Transition(label='Draft plan')
ConductStrategicAlignmentMeeting = Transition(label='Conduct strategic alignment meeting')
ReviewBudgetFeasibility = Transition(label='Review budget feasibility')
ProvideFeedback = Transition(label='Provide feedback')
AdjustPlan = Transition(label='Adjust Plan')
DocumentedAndApproveAdjustment = Transition(label='Documented and approve adjustment')
ApproveFinalBudget = Transition(label='Approve final budget')
DistributeBudget = Transition(label='Distribute budget')
ImplementPlan = Transition(label='Implement plan')

# Define the sequence of activities
sequence = StrictPartialOrder(nodes=[OutlineObjectives, DraftPlan, ConductStrategicAlignmentMeeting, ReviewBudgetFeasibility, ProvideFeedback, AdjustPlan, DocumentedAndApproveAdjustment, ApproveFinalBudget, DistributeBudget, ImplementPlan])

# Define the loop for adjustments
adjustment_loop = OperatorPOWL(operator=Operator.LOOP, children=[ProvideFeedback, AdjustPlan, DocumentedAndApproveAdjustment])

# Define the choice between providing feedback and adjusting the plan
feedback_or_adjustment = OperatorPOWL(operator=Operator.XOR, children=[ProvideFeedback, adjustment_loop])

# Define the final root node with the sequence and the choice
root = StrictPartialOrder(nodes=[sequence, feedback_or_adjustment])
root.order.add_edge(sequence, feedback_or_adjustment)