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

# Define silent transitions for the loop
skip = SilentTransition()

# Define the loop structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, user_testing, iterate_feedback])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, compliance_check])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor])

# Add edges to the root
root.order.add_edge(loop, xor)

# Print the final POWL model
print(root)