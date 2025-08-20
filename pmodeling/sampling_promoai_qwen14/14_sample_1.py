import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
outline_objectives = Transition(label='Outline objectives')
draft_plan = Transition(label='Draft plan')
conduct_strategic_alignment_meeting = Transition(label='Conduct strategic alignment meeting')
review_budget_feasibility = Transition(label='Review budget feasibility')
adjust_plan = Transition(label='Adjust Plan')
provide_feedback = Transition(label='Provide feedback')
documented_and_approve_adjustment = Transition(label='Documented and approve adjustment')
approve_final_budget = Transition(label='Approve final budget')
distribute_budget = Transition(label='Distribute budget')
implement_plan = Transition(label='Implement plan')

# Define operators and partial orders
strategic_alignment = OperatorPOWL(operator=Operator.XOR, children=[conduct_strategic_alignment_meeting, provide_feedback])
budget_review = OperatorPOWL(operator=Operator.LOOP, children=[review_budget_feasibility, adjust_plan, documented_and_approve_adjustment])
approval_process = OperatorPOWL(operator=Operator.XOR, children=[approve_final_budget, distribute_budget])

# Define the root process tree
root = StrictPartialOrder(nodes=[outline_objectives, draft_plan, strategic_alignment, budget_review, approval_process, implement_plan])

# Define the partial order of activities
root.order.add_edge(outline_objectives, draft_plan)
root.order.add_edge(draft_plan, strategic_alignment)
root.order.add_edge(strategic_alignment, budget_review)
root.order.add_edge(budget_review, approval_process)
root.order.add_edge(approval_process, implement_plan)

# Define the partial order within the XOR and LOOP operators
strategic_alignment.order.add_edge(conduct_strategic_alignment_meeting, provide_feedback)
budget_review.order.add_edge(review_budget_feasibility, adjust_plan)
budget_review.order.add_edge(adjust_plan, documented_and_approve_adjustment)
approval_process.order.add_edge(approve_final_budget, distribute_budget)

print(root)