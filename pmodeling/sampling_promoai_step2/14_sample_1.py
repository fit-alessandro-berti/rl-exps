import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
outline_objectives = Transition(label='Outline objectives')
draft_plan = Transition(label='Draft plan')
conduct_alignment_meeting = Transition(label='Conduct strategic alignment meeting')
provide_feedback = Transition(label='Provide feedback')
documented_and_approve_adjustment = Transition(label='Documented and approve adjustment')
adjust_plan = Transition(label='Adjust Plan')
finance_review = Transition(label='Review budget feasibility')
approve_final_budget = Transition(label='Approve final budget')
implement_plan = Transition(label='Implement plan')
distribute_budget = Transition(label='Distribute budget')

# Define the partial order model
root = StrictPartialOrder(nodes=[
    outline_objectives,
    draft_plan,
    conduct_alignment_meeting,
    provide_feedback,
    documented_and_approve_adjustment,
    adjust_plan,
    finance_review,
    approve_final_budget,
    implement_plan,
    distribute_budget
])

# Define the dependencies
root.order.add_edge(outline_objectives, draft_plan)
root.order.add_edge(draft_plan, conduct_alignment_meeting)
root.order.add_edge(conduct_alignment_meeting, provide_feedback)
root.order.add_edge(provide_feedback, documented_and_approve_adjustment)
root.order.add_edge(documented_and_approve_adjustment, adjust_plan)
root.order.add_edge(adjust_plan, finance_review)
root.order.add_edge(finance_review, approve_final_budget)
root.order.add_edge(approve_final_budget, implement_plan)
root.order.add_edge(implement_plan, distribute_budget)

print(root)