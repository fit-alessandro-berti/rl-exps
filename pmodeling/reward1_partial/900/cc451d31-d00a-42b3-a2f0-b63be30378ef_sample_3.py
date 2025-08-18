import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

ai_filtering_choice = OperatorPOWL(operator=Operator.XOR, children=[ai_filtering, skip])
community_voting_choice = OperatorPOWL(operator=Operator.XOR, children=[community_voting, skip])
expert_review_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
prototype_build_choice = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, skip])
user_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[user_testing, skip])
iterate_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[iterate_feedback, skip])
risk_assess_choice = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
compliance_check_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
pilot_launch_choice = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, skip])
performance_track_choice = OperatorPOWL(operator=Operator.XOR, children=[performance_track, skip])
impact_analyze_choice = OperatorPOWL(operator=Operator.XOR, children=[impact_analyze, skip])
insight_gather_choice = OperatorPOWL(operator=Operator.XOR, children=[insight_gather, skip])
cycle_adjust_choice = OperatorPOWL(operator=Operator.XOR, children=[cycle_adjust, skip])
final_report_choice = OperatorPOWL(operator=Operator.XOR, children=[final_report, skip])

root = StrictPartialOrder(nodes=[
    idea_solicitation,
    ai_filtering_choice,
    community_voting_choice,
    expert_review_choice,
    prototype_build_choice,
    user_testing_choice,
    iterate_feedback_choice,
    risk_assess_choice,
    compliance_check_choice,
    pilot_launch_choice,
    performance_track_choice,
    impact_analyze_choice,
    insight_gather_choice,
    cycle_adjust_choice,
    final_report_choice
])

root.order.add_edge(idea_solicitation, ai_filtering_choice)
root.order.add_edge(ai_filtering_choice, community_voting_choice)
root.order.add_edge(community_voting_choice, expert_review_choice)
root.order.add_edge(expert_review_choice, prototype_build_choice)
root.order.add_edge(prototype_build_choice, user_testing_choice)
root.order.add_edge(user_testing_choice, iterate_feedback_choice)
root.order.add_edge(iterate_feedback_choice, risk_assess_choice)
root.order.add_edge(risk_assess_choice, compliance_check_choice)
root.order.add_edge(compliance_check_choice, pilot_launch_choice)
root.order.add_edge(pilot_launch_choice, performance_track_choice)
root.order.add_edge(performance_track_choice, impact_analyze_choice)
root.order.add_edge(impact_analyze_choice, insight_gather_choice)
root.order.add_edge(insight_gather_choice, cycle_adjust_choice)
root.order.add_edge(cycle_adjust_choice, final_report_choice)