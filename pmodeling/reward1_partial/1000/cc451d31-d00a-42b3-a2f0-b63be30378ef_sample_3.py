import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    idea_solicitation,
    ai_filtering,
    community_voting,
    expert_review,
    prototype_build,
    user_testing,
    iterate_feedback,
    risk_assess,
    compliance_check,
    pilot_launch,
    performance_track,
    impact_analyze,
    insight_gather,
    cycle_adjust,
    final_report
])

# Define the edges in the partial order
root.order.add_edge(idea_solicitation, ai_filtering)
root.order.add_edge(ai_filtering, community_voting)
root.order.add_edge(community_voting, expert_review)
root.order.add_edge(expert_review, prototype_build)
root.order.add_edge(prototype_build, user_testing)
root.order.add_edge(user_testing, iterate_feedback)
root.order.add_edge(iterate_feedback, risk_assess)
root.order.add_edge(risk_assess, compliance_check)
root.order.add_edge(compliance_check, pilot_launch)
root.order.add_edge(pilot_launch, performance_track)
root.order.add_edge(performance_track, impact_analyze)
root.order.add_edge(impact_analyze, insight_gather)
root.order.add_edge(insight_gather, cycle_adjust)
root.order.add_edge(cycle_adjust, final_report)

# Print the root to verify
print(root)