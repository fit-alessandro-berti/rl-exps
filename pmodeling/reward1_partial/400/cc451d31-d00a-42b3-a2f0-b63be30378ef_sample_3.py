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

# Define the loop and XOR nodes
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[
    idea_solicitation,
    ai_filtering,
    community_voting,
    expert_review,
    prototype_build,
    user_testing,
    iterate_feedback
])

xor_node = OperatorPOWL(operator=Operator.XOR, children=[
    risk_assess,
    compliance_check,
    pilot_launch,
    performance_track,
    impact_analyze
])

# Create the root node
root = StrictPartialOrder(nodes=[loop_node, xor_node])
root.order.add_edge(loop_node, xor_node)

# Print the root node
print(root)