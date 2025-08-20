import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

OutlineObjectives = Transition(label='Outline objectives')
DraftPlan = Transition(label='Draft plan')
ConductStrategicAlignmentMeeting = Transition(label='Conduct strategic alignment meeting')
ReviewBudgetFeasibility = Transition(label='Review budget feasibility')
AdjustPlan = Transition(label='Adjust Plan')
DocumentedAndApproveAdjustment = Transition(label='Documented and approve adjustment')
ApproveFinalBudget = Transition(label='Approve final budget')
DistributeBudget = Transition(label='Distribute budget')
ImplementPlan = Transition(label='Implement plan')
ProvideFeedback = Transition(label='Provide feedback')

outline_and_draft = StrictPartialOrder(nodes=[OutlineObjectives, DraftPlan])
outline_and_draft.order.add_edge(OutlineObjectives, DraftPlan)

strategic_alignment = StrictPartialOrder(nodes=[ConductStrategicAlignmentMeeting, ProvideFeedback])
strategic_alignment.order.add_edge(ConductStrategicAlignmentMeeting, ProvideFeedback)

review_budget = StrictPartialOrder(nodes=[ReviewBudgetFeasibility, DocumentedAndApproveAdjustment])
review_budget.order.add_edge(ReviewBudgetFeasibility, DocumentedAndApproveAdjustment)

adjustment_loop = OperatorPOWL(operator=Operator.LOOP, children=[AdjustPlan, strategic_alignment])

budget_approval = StrictPartialOrder(nodes=[ApproveFinalBudget, DistributeBudget])
budget_approval.order.add_edge(ApproveFinalBudget, DistributeBudget)

root = StrictPartialOrder(nodes=[outline_and_draft, adjustment_loop, review_budget, budget_approval])
root.order.add_edge(outline_and_draft, adjustment_loop)
root.order.add_edge(adjustment_loop, review_budget)
root.order.add_edge(review_budget, budget_approval)
root.order.add_edge(budget_approval, ImplementPlan)