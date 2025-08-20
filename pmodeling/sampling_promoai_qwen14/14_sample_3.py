import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Outline_objectives = Transition(label='Outline objectives')
Draft_plan = Transition(label='Draft plan')
Conduct_strategic_alignment_meeting = Transition(label='Conduct strategic alignment meeting')
Review_budget_feasibility = Transition(label='Review budget feasibility')
Adjust_Plan = Transition(label='Adjust Plan')
Documented_and_approve_adjustment = Transition(label='Documented and approve adjustment')
Approve_final_budget = Transition(label='Approve final budget')
Distribute_budget = Transition(label='Distribute budget')
Implement_plan = Transition(label='Implement plan')

# Define the POWL model for the process
root = StrictPartialOrder(nodes=[Outline_objectives, Draft_plan, Conduct_strategic_alignment_meeting, Review_budget_feasibility, Adjust_Plan, Documented_and_approve_adjustment, Approve_final_budget, Distribute_budget, Implement_plan])

# Define the partial order relationships
root.order.add_edge(Outline_objectives, Draft_plan)
root.order.add_edge(Draft_plan, Conduct_strategic_alignment_meeting)
root.order.add_edge(Conduct_strategic_alignment_meeting, Review_budget_feasibility)
root.order.add_edge(Review_budget_feasibility, Adjust_Plan)
root.order.add_edge(Adjust_Plan, Documented_and_approve_adjustment)
root.order.add_edge(Documented_and_approve_adjustment, Approve_final_budget)
root.order.add_edge(Approve_final_budget, Distribute_budget)
root.order.add_edge(Distribute_budget, Implement_plan)