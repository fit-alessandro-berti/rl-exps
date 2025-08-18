import pm4py

# Define transitions for each activity
idea_solicitation = pm4py.objects.powl.obj.Transition(label='Idea Solicitation')
ai_filtering = pm4py.objects.powl.obj.Transition(label='AI Filtering')
community_voting = pm4py.objects.powl.obj.Transition(label='Community Voting')
expert_review = pm4py.objects.powl.obj.Transition(label='Expert Review')
prototype_build = pm4py.objects.powl.obj.Transition(label='Prototype Build')
user_testing = pm4py.objects.powl.obj.Transition(label='User Testing')
iterate_feedback = pm4py.objects.powl.obj.Transition(label='Iterate Feedback')
risk_assess = pm4py.objects.powl.obj.Transition(label='Risk Assess')
compliance_check = pm4py.objects.powl.obj.Transition(label='Compliance Check')
pilot_launch = pm4py.objects.powl.obj.Transition(label='Pilot Launch')
performance_track = pm4py.objects.powl.obj.Transition(label='Performance Track')
impact_analyze = pm4py.objects.powl.obj.Transition(label='Impact Analyze')
insight_gather = pm4py.objects.powl.obj.Transition(label='Insight Gather')
cycle_adjust = pm4py.objects.powl.obj.Transition(label='Cycle Adjust')
final_report = pm4py.objects.powl.obj.Transition(label='Final Report')

# Define the exclusive choices and loops
# Idea Solicitation -> AI Filtering or Community Voting -> Expert Review
exclusive_choice_ai_or_community = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[ai_filtering, community_voting])
exclusive_choice_expert = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[expert_review, iterate_feedback])

# AI Filtering or Community Voting -> Expert Review or Iterate Feedback
exclusive_choice_ai_or_community_expert = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[exclusive_choice_ai_or_community, exclusive_choice_expert])

# Prototype Build -> User Testing or Iterate Feedback
exclusive_choice_prototype_or_user = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[prototype_build, user_testing])

# User Testing or Iterate Feedback -> Risk Assess or Iterate Feedback
exclusive_choice_user_or_iterate = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[user_testing, iterate_feedback])

# Risk Assess or Iterate Feedback -> Compliance Check or Iterate Feedback
exclusive_choice_risk_or_iterate = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[risk_assess, iterate_feedback])

# Compliance Check or Iterate Feedback -> Pilot Launch or Iterate Feedback
exclusive_choice_compliance_or_iterate = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[compliance_check, iterate_feedback])

# Pilot Launch -> Performance Track or Iterate Feedback
exclusive_choice_pilot_or_iterate = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[pilot_launch, iterate_feedback])

# Performance Track or Iterate Feedback -> Impact Analyze or Iterate Feedback
exclusive_choice_performance_or_iterate = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[performance_track, iterate_feedback])

# Impact Analyze or Iterate Feedback -> Insight Gather or Iterate Feedback
exclusive_choice_impact_or_iterate = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[impact_analyze, iterate_feedback])

# Insight Gather or Iterate Feedback -> Cycle Adjust or Iterate Feedback
exclusive_choice_insight_or_iterate = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[insight_gather, iterate_feedback])

# Cycle Adjust or Iterate Feedback -> Final Report or Iterate Feedback
exclusive_choice_cycle_or_iterate = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[cycle_adjust, iterate_feedback])

# Define the root node as a strict partial order
root = pm4py.objects.powl.obj.StrictPartialOrder(
    nodes=[
        exclusive_choice_ai_or_community_expert,
        exclusive_choice_prototype_or_user,
        exclusive_choice_user_or_iterate,
        exclusive_choice_risk_or_iterate,
        exclusive_choice_compliance_or_iterate,
        exclusive_choice_pilot_or_iterate,
        exclusive_choice_performance_or_iterate,
        exclusive_choice_impact_or_iterate,
        exclusive_choice_insight_or_iterate,
        exclusive_choice_cycle_or_iterate
    ]
)

# Add edges to the root node
root.order.add_edge(exclusive_choice_ai_or_community_expert, exclusive_choice_prototype_or_user)
root.order.add_edge(exclusive_choice_prototype_or_user, exclusive_choice_user_or_iterate)
root.order.add_edge(exclusive_choice_user_or_iterate, exclusive_choice_risk_or_iterate)
root.order.add_edge(exclusive_choice_risk_or_iterate, exclusive_choice_compliance_or_iterate)
root.order.add_edge(exclusive_choice_compliance_or_iterate, exclusive_choice_pilot_or_iterate)
root.order.add_edge(exclusive_choice_pilot_or_iterate, exclusive_choice_performance_or_iterate)
root.order.add_edge(exclusive_choice_performance_or_iterate, exclusive_choice_impact_or_iterate)
root.order.add_edge(exclusive_choice_impact_or_iterate, exclusive_choice_insight_or_iterate)
root.order.add_edge(exclusive_choice_insight_or_iterate, exclusive_choice_cycle_or_iterate)