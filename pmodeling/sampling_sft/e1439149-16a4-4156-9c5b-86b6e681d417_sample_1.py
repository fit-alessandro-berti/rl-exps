import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
trend_scan        = Transition(label='Trend Scan')
idea_harvest      = Transition(label='Idea Harvest')
workshop_host     = Transition(label='Workshop Host')
concept_filter    = Transition(label='Concept Filter')
prototype_build   = Transition(label='Prototype Build')
expert_review     = Transition(label='Expert Review')
feasibility_check = Transition(label='Feasibility Check')
risk_assess       = Transition(label='Risk Assess')
pilot_launch      = Transition(label='Pilot Launch')
data_capture      = Transition(label='Data Capture')
performance_rev   = Transition(label='Performance Review')
scale_plan        = Transition(label='Scale Plan')
resource_align    = Transition(label='Resource Align')
learn_share       = Transition(label='Learn Share')
culture_embed     = Transition(label='Culture Embed')

# Build the partial order
root = StrictPartialOrder(nodes=[
    trend_scan,
    idea_harvest,
    workshop_host,
    concept_filter,
    prototype_build,
    expert_review,
    feasibility_check,
    risk_assess,
    pilot_launch,
    data_capture,
    performance_rev,
    scale_plan,
    resource_align,
    learn_share,
    culture_embed
])

# Sequence of activities
root.order.add_edge(trend_scan, idea_harvest)
root.order.add_edge(idea_harvest, workshop_host)
root.order.add_edge(workshop_host, concept_filter)
root.order.add_edge(concept_filter, prototype_build)
root.order.add_edge(prototype_build, expert_review)
root.order.add_edge(expert_review, feasibility_check)
root.order.add_edge(feasibility_check, risk_assess)
root.order.add_edge(risk_assess, pilot_launch)

# Parallel paths after pilot launch
root.order.add_edge(pilot_launch, data_capture)
root.order.add_edge(pilot_launch, performance_rev)

# After data capture and performance review, choose one path
root.order.add_edge(data_capture, scale_plan)
root.order.add_edge(performance_rev, scale_plan)

# Both paths lead to resource alignment and knowledge sharing
root.order.add_edge(scale_plan, resource_align)
root.order.add_edge(scale_plan, learn_share)

# Both resource alignment and knowledge sharing lead to culture embedding
root.order.add_edge(resource_align, culture_embed)
root.order.add_edge(learn_share, culture_embed)