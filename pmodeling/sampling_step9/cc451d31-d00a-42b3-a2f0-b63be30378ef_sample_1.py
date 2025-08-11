import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, iterate_feedback])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[user_testing, iterate_feedback])

# Define XOR nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[idea_solicitation, ai_filtering, community_voting, expert_review, loop1, loop2, xor1, xor2, pilot_launch, performance_track, impact_analyze, insight_gather, cycle_adjust, final_report])
root.order.add_edge(idea_solicitation, ai_filtering)
root.order.add_edge(ai_filtering, community_voting)
root.order.add_edge(community_voting, expert_review)
root.order.add_edge(expert_review, loop1)
root.order.add_edge(loop1, iterate_feedback)
root.order.add_edge(prototype_build, loop2)
root.order.add_edge(loop2, iterate_feedback)
root.order.add_edge(iterate_feedback, user_testing)
root.order.add_edge(user_testing, loop2)
root.order.add_edge(loop2, iterate_feedback)
root.order.add_edge(prototype_build, xor1)
root.order.add_edge(prototype_build, xor2)
root.order.add_edge(xor1, risk_assess)
root.order.add_edge(xor2, compliance_check)
root.order.add_edge(risk_assess, pilot_launch)
root.order.add_edge(compliance_check, pilot_launch)
root.order.add_edge(pilot_launch, performance_track)
root.order.add_edge(performance_track, impact_analyze)
root.order.add_edge(impact_analyze, insight_gather)
root.order.add_edge(insight_gather, cycle_adjust)
root.order.add_edge(cycle_adjust, final_report)

print(root)