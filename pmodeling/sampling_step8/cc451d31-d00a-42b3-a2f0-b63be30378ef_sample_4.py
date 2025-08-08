import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop and exclusive choice nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[user_testing, iterate_feedback])
xor = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, compliance_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, performance_track])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[impact_analyze, insight_gather])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[cycle_adjust, final_report])

# Define the root node and its dependencies
root = StrictPartialOrder(nodes=[idea_solicitation, ai_filtering, community_voting, expert_review, prototype_build, loop, xor, xor2, xor3, xor4])
root.order.add_edge(idea_solicitation, ai_filtering)
root.order.add_edge(ai_filtering, community_voting)
root.order.add_edge(community_voting, expert_review)
root.order.add_edge(expert_review, prototype_build)
root.order.add_edge(prototype_build, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, final_report)