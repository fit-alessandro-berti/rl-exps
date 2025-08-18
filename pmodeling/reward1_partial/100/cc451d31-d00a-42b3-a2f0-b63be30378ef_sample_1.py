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

# Define operators for the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[community_voting, expert_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[user_testing, iterate_feedback])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, compliance_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[performance_track, impact_analyze])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[insight_gather, cycle_adjust])

# Create the root node with all possible paths from the start to the end
root = StrictPartialOrder(nodes=[
    idea_solicitation,
    ai_filtering,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    final_report
])

# Add dependencies between nodes
root.order.add_edge(idea_solicitation, ai_filtering)
root.order.add_edge(ai_filtering, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, final_report)

# Print the root node
print(root)