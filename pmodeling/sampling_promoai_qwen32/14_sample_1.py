import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
outline_objectives = Transition(label='Outline objectives')
draft_plan = Transition(label='Draft plan')
strategic_alignment_meeting = Transition(label='Conduct strategic alignment meeting')
review_budget_feasibility = Transition(label='Review budget feasibility')
adjust_plan = Transition(label='Adjust Plan')
documented_approve_adjustment = Transition(label='Documented and approve adjustment')
approve_final_budget = Transition(label='Approve final budget')
distribute_budget = Transition(label='Distribute budget')
implement_plan = Transition(label='Implement plan')

# Define the loops and choices
adjustment_loop = OperatorPOWL(operator=Operator.LOOP, children=[adjust_plan, documented_approve_adjustment])
review_loop = OperatorPOWL(operator=Operator.LOOP, children=[strategic_alignment_meeting, review_budget_feasibility, adjustment_loop])
main_flow = OperatorPOWL(operator=Operator.SEQUENCE, children=[outline_objectives, draft_plan, review_loop, approve_final_budget, distribute_budget, implement_plan])

# Define the root
root = StrictPartialOrder(nodes=[main_flow])