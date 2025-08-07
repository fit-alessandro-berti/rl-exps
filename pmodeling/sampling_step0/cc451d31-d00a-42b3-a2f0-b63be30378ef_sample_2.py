import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
idea_solicitation = Transition(label='Idea Solicitation')
ai_filtering = Transition(label='AI Filtering')
community_voting = Transition(label='Community Voting')
expert_review = Transition(label='Expert Review')
prototype_build = Transition(label='Prototype Build')
user_testing = Transition(label='User Testing')
iterate_feedback = Transition(label='Iterate Feedback')
risk_assess = Transition(label='Risk Assess')
compliance_check = Transition(label='Compliance Check')
pilot_launch = Transition(label='Pilot Launch')
performance_track = Transition(label='Performance Track')
impact_analyze = Transition(label='Impact Analyze')
insight_gather = Transition(label='Insight Gather')
cycle_adjust = Transition(label='Cycle Adjust')
final_report = Transition(label='Final Report')

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[community_voting, expert_review, prototype_build, user_testing, iterate_feedback])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, compliance_check, pilot_launch])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[performance_track, impact_analyze, insight_gather])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[cycle_adjust, final_report])

# Define the partial order structure
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)