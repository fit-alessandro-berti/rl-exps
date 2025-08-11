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
prototype_loop = OperatorPOWL(operator=Operator.LOOP, children=[user_testing, iterate_feedback])

# Define XOR nodes
evaluation_loop = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
compliance_loop = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
launch_loop = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, skip])

# Define partial order
root = StrictPartialOrder(nodes=[prototype_loop, evaluation_loop, compliance_loop, launch_loop])
root.order.add_edge(prototype_loop, evaluation_loop)
root.order.add_edge(prototype_loop, compliance_loop)
root.order.add_edge(prototype_loop, launch_loop)

# Add additional nodes to the partial order
root.nodes.extend([idea_solicitation, ai_filtering, community_voting, prototype_build, performance_track, impact_analyze, insight_gather, cycle_adjust, final_report])

# Add edges to the partial order
root.order.add_edge(idea_solicitation, ai_filtering)
root.order.add_edge(idea_solicitation, community_voting)
root.order.add_edge(ai_filtering, evaluation_loop)
root.order.add_edge(community_voting, evaluation_loop)
root.order.add_edge(evaluation_loop, prototype_build)
root.order.add_edge(prototype_build, compliance_loop)
root.order.add_edge(compliance_loop, launch_loop)
root.order.add_edge(launch_loop, performance_track)
root.order.add_edge(performance_track, impact_analyze)
root.order.add_edge(impact_analyze, insight_gather)
root.order.add_edge(insight_gather, cycle_adjust)
root.order.add_edge(cycle_adjust, final_report)

# Print the final POWL model
print(root)