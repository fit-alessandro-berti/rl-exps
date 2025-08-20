import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
OutlineObjectives = Transition(label='Outline objectives')
DraftPlan = Transition(label='Draft plan')
ConductStrategicAlignmentMeeting = Transition(label='Conduct strategic alignment meeting')
ReviewBudgetFeasibility = Transition(label='Review budget feasibility')
AdjustPlan = Transition(label='Adjust Plan')
DocumentedAndApproveAdjustment = Transition(label='Documented and approve adjustment')
ApproveFinalBudget = Transition(label='Approve final budget')
DistributeBudget = Transition(label='Distribute budget')
ImplementPlan = Transition(label='Implement plan')

# Define loops and choices
AdjustmentLoop = OperatorPOWL(operator=Operator.LOOP, children=[AdjustPlan, DocumentedAndApproveAdjustment])
AdjustmentChoice = OperatorPOWL(operator=Operator.XOR, children=[AdjustmentLoop, SilentTransition()])

# Define partial order
root = StrictPartialOrder(nodes=[OutlineObjectives, DraftPlan, ConductStrategicAlignmentMeeting, ReviewBudgetFeasibility, AdjustmentChoice, ApproveFinalBudget, DistributeBudget, ImplementPlan])
root.order.add_edge(OutlineObjectives, DraftPlan)
root.order.add_edge(DraftPlan, ConductStrategicAlignmentMeeting)
root.order.add_edge(ConductStrategicAlignmentMeeting, ReviewBudgetFeasibility)
root.order.add_edge(ReviewBudgetFeasibility, AdjustmentChoice)
root.order.add_edge(AdjustmentChoice, ApproveFinalBudget)
root.order.add_edge(ApproveFinalBudget, DistributeBudget)
root.order.add_edge(DistributeBudget, ImplementPlan)