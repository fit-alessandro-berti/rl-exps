import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
trend_scan = Transition(label='Trend Scan')
idea_harvest = Transition(label='Idea Harvest')
workshop_host = Transition(label='Workshop Host')
concept_filter = Transition(label='Concept Filter')
prototype_build = Transition(label='Prototype Build')
expert_review = Transition(label='Expert Review')
feasibility_check = Transition(label='Feasibility Check')
risk_assess = Transition(label='Risk Assess')
pilot_launch = Transition(label='Pilot Launch')
data_capture = Transition(label='Data Capture')
performance_review = Transition(label='Performance Review')
scale_plan = Transition(label='Scale Plan')
resource_align = Transition(label='Resource Align')
learn_share = Transition(label='Learn Share')
culture_embed = Transition(label='Culture Embed')

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    trend_scan, idea_harvest, workshop_host, concept_filter, prototype_build,
    expert_review, feasibility_check, risk_assess, pilot_launch, data_capture,
    performance_review, scale_plan, resource_align, learn_share, culture_embed
])

# Add dependencies if needed (e.g., workflow logic)
# Example: root.order.add_edge(trend_scan, idea_harvest)
# Add more dependencies as per the actual process flow

# Save the final result in the variable 'root'
print(root)