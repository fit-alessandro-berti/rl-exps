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

# Define the control-flow operators
choice_ai_voting = OperatorPOWL(operator=Operator.XOR, children=[ai_filtering, community_voting])
choice_review_iterate = OperatorPOWL(operator=Operator.XOR, children=[expert_review, iterate_feedback])
choice_test_risk = OperatorPOWL(operator=Operator.XOR, children=[user_testing, risk_assess])
choice_check_launch = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, pilot_launch])
choice_track_insight = OperatorPOWL(operator=Operator.XOR, children=[performance_track, impact_analyze])
choice_gather_adjust = OperatorPOWL(operator=Operator.XOR, children=[insight_gather, cycle_adjust])
loop_final_report = OperatorPOWL(operator=Operator.LOOP, children=[final_report])

# Define the partial order
root = StrictPartialOrder(nodes=[idea_solicitation, choice_ai_voting, choice_review_iterate, choice_test_risk, choice_check_launch, choice_track_insight, choice_gather_adjust, loop_final_report])
root.order.add_edge(idea_solicitation, choice_ai_voting)
root.order.add_edge(idea_solicitation, choice_review_iterate)
root.order.add_edge(choice_ai_voting, choice_review_iterate)
root.order.add_edge(choice_review_iterate, choice_test_risk)
root.order.add_edge(choice_test_risk, choice_check_launch)
root.order.add_edge(choice_check_launch, choice_track_insight)
root.order.add_edge(choice_track_insight, choice_gather_adjust)
root.order.add_edge(choice_gather_adjust, loop_final_report)

# Add the loop edge
root.order.add_edge(loop_final_report, idea_solicitation)