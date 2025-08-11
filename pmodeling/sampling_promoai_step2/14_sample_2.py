from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
outline_objectives = Transition(label='Outline objectives')
draft_plan = Transition(label='Draft plan')
conduct_strategic_alignment_meeting = Transition(label='Conduct strategic alignment meeting')
provide_feedback = Transition(label='Provide feedback')
adjust_plan = Transition(label='Adjust Plan')
document_and_approve_adjustment = Transition(label='Documented and approve adjustment')
distribute_budget = Transition(label='Distribute budget')
approve_final_budget = Transition(label='Approve final budget')
implement_plan = Transition(label='Implement plan')

# Create the POWL model
root = StrictPartialOrder(nodes=[outline_objectives, draft_plan, conduct_strategic_alignment_meeting, provide_feedback, adjust_plan, document_and_approve_adjustment, distribute_budget, approve_final_budget, implement_plan])

# Define the partial order dependencies
root.order.add_edge(outline_objectives, draft_plan)
root.order.add_edge(draft_plan, conduct_strategic_alignment_meeting)
root.order.add_edge(conduct_strategic_alignment_meeting, provide_feedback)
root.order.add_edge(provide_feedback, adjust_plan)
root.order.add_edge(adjust_plan, document_and_approve_adjustment)
root.order.add_edge(document_and_approve_adjustment, distribute_budget)
root.order.add_edge(distribute_budget, approve_final_budget)
root.order.add_edge(approve_final_budget, implement_plan)

print(root)