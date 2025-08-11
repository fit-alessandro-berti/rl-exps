import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
outline_objectives = Transition(label='Outline objectives')
draft_plan = Transition(label='Draft plan')
strategic_alignment = Transition(label='Conduct strategic alignment meeting')
provide_feedback = Transition(label='Provide feedback')
review_budget_feasibility = Transition(label='Review budget feasibility')
documented_and_approve_adjustment = Transition(label='Documented and approve adjustment')
adjust_plan = Transition(label='Adjust Plan')
approve_final_budget = Transition(label='Approve final budget')
distribute_budget = Transition(label='Distribute budget')
implement_plan = Transition(label='Implement plan')

# Define the POWL model
root = StrictPartialOrder(nodes=[outline_objectives, draft_plan, strategic_alignment, provide_feedback, review_budget_feasibility, documented_and_approve_adjustment, adjust_plan, approve_final_budget, distribute_budget, implement_plan])

# Define the partial order dependencies
root.order.add_edge(outline_objectives, draft_plan)
root.order.add_edge(draft_plan, strategic_alignment)
root.order.add_edge(strategic_alignment, provide_feedback)
root.order.add_edge(provide_feedback, review_budget_feasibility)
root.order.add_edge(review_budget_feasibility, documented_and_approve_adjustment)
root.order.add_edge(documented_and_approve_adjustment, adjust_plan)
root.order.add_edge(adjust_plan, approve_final_budget)
root.order.add_edge(approve_final_budget, distribute_budget)
root.order.add_edge(distribute_budget, implement_plan)

print(root)