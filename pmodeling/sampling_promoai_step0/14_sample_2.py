import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
outline_objectives = Transition(label='Outline objectives')
draft_plan = Transition(label='Draft plan')
review_budget_feasibility = Transition(label='Review budget feasibility')
conducted_strategy_alignment = Transition(label='Conduct strategic alignment meeting')
distribute_budget = Transition(label='Distribute budget')
documented_and_approve_adjustment = Transition(label='Documented and approve adjustment')
adjust_plan = Transition(label='Adjust Plan')
approve_final_budget = Transition(label='Approve final budget')
provide_feedback = Transition(label='Provide feedback')

# Define the partial order
root = StrictPartialOrder(nodes=[outline_objectives, draft_plan, review_budget_feasibility, conducted_strategy_alignment, distribute_budget, documented_and_approve_adjustment, adjust_plan, approve_final_budget, provide_feedback])

# Define the dependencies
root.order.add_edge(outline_objectives, draft_plan)
root.order.add_edge(draft_plan, review_budget_feasibility)
root.order.add_edge(review_budget_feasibility, conducted_strategy_alignment)
root.order.add_edge(conducted_strategy_alignment, distribute_budget)
root.order.add_edge(distribute_budget, documented_and_approve_adjustment)
root.order.add_edge(documented_and_approve_adjustment, adjust_plan)
root.order.add_edge(adjust_plan, approve_final_budget)
root.order.add_edge(approve_final_budget, distribute_budget)
root.order.add_edge(approve_final_budget, provide_feedback)

# Print the root node
print(root)