import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
outline_objectives = Transition(label='Outline objectives')
draft_plan = Transition(label='Draft plan')
conduct_alignment_meeting = Transition(label='Conduct strategic alignment meeting')
documented_and_approve_adjustment = Transition(label='Documented and approve adjustment')
adjust_plan = Transition(label='Adjust Plan')
review_budget_feasibility = Transition(label='Review budget feasibility')
approve_final_budget = Transition(label='Approve final budget')
distribute_budget = Transition(label='Distribute budget')
implement_plan = Transition(label='Implement plan')

# Define the partial order model
root = StrictPartialOrder(nodes=[
    outline_objectives,
    draft_plan,
    conduct_alignment_meeting,
    documented_and_approve_adjustment,
    adjust_plan,
    review_budget_feasibility,
    approve_final_budget,
    distribute_budget,
    implement_plan
])

# Define the order dependencies
root.order.add_edge(outline_objectives, draft_plan)
root.order.add_edge(draft_plan, conduct_alignment_meeting)
root.order.add_edge(conduct_alignment_meeting, documented_and_approve_adjustment)
root.order.add_edge(documented_and_approve_adjustment, adjust_plan)
root.order.add_edge(adjust_plan, review_budget_feasibility)
root.order.add_edge(review_budget_feasibility, approve_final_budget)
root.order.add_edge(approve_final_budget, distribute_budget)
root.order.add_edge(distribute_budget, implement_plan)

print(root)