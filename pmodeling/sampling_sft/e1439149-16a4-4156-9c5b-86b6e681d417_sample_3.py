import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
trend_scan    = Transition(label='Trend Scan')
idea_harvest  = Transition(label='Idea Harvest')
workshop_host = Transition(label='Workshop Host')
concept_filter= Transition(label='Concept Filter')
prototype_build= Transition(label='Prototype Build')
expert_review = Transition(label='Expert Review')
feasibility_check= Transition(label='Feasibility Check')
risk_assess   = Transition(label='Risk Assess')
pilot_launch  = Transition(label='Pilot Launch')
data_capture  = Transition(label='Data Capture')
performance_review = Transition(label='Performance Review')
scale_plan    = Transition(label='Scale Plan')
resource_align= Transition(label='Resource Align')
learn_share   = Transition(label='Learn Share')
culture_embed = Transition(label='Culture Embed')

# Loop for iterative feedback and refinement
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert_review, prototype_build]
)

# Parallel assessment of feasibility and risk
parallel_assess = StrictPartialOrder(nodes=[feasibility_check, risk_assess])
parallel_assess.order.add_edge(feasibility_check, pilot_launch)
parallel_assess.order.add_edge(risk_assess, pilot_launch)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    trend_scan,
    idea_harvest,
    workshop_host,
    concept_filter,
    prototype_build,
    feedback_loop,
    parallel_assess,
    pilot_launch,
    data_capture,
    performance_review,
    scale_plan,
    resource_align,
    learn_share,
    culture_embed
])

# Define the control-flow edges
root.order.add_edge(trend_scan, idea_harvest)
root.order.add_edge(idea_harvest, workshop_host)
root.order.add_edge(workshop_host, concept_filter)
root.order.add_edge(concept_filter, prototype_build)
root.order.add_edge(prototype_build, feedback_loop)
root.order.add_edge(feedback_loop, prototype_build)
root.order.add_edge(prototype_build, parallel_assess)
root.order.add_edge(parallel_assess, pilot_launch)
root.order.add_edge(pilot_launch, data_capture)
root.order.add_edge(data_capture, performance_review)
root.order.add_edge(performance_review, scale_plan)
root.order.add_edge(scale_plan, resource_align)
root.order.add_edge(resource_align, learn_share)
root.order.add_edge(learn_share, culture_embed)