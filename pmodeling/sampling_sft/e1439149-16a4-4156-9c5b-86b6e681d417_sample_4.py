import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
trend_scan    = Transition(label='Trend Scan')
idea_harvest  = Transition(label='Idea Harvest')
workshop_host = Transition(label='Workshop Host')
concept_filter= Transition(label='Concept Filter')
prototype_build = Transition(label='Prototype Build')
expert_review = Transition(label='Expert Review')
feasibility_check = Transition(label='Feasibility Check')
risk_assess   = Transition(label='Risk Assess')
pilot_launch  = Transition(label='Pilot Launch')
data_capture  = Transition(label='Data Capture')
performance_review = Transition(label='Performance Review')
scale_plan    = Transition(label='Scale Plan')
resource_align = Transition(label='Resource Align')
learn_share   = Transition(label='Learn Share')
culture_embed = Transition(label='Culture Embed')

# Build the parallel learning & knowledge sharing branch (skip if no external experts)
skip = SilentTransition()
learn_share_branch = StrictPartialOrder(nodes=[learn_share, skip])
# No edges => both can run in parallel

# Build the core iterative innovation loop:
#   1. Data Capture
#   2. Performance Review
#   3. Scale Plan
#   4. Resource Align
#   5. Learn Share (parallel branch)
# Then repeat from 1
loop_body = StrictPartialOrder(nodes=[data_capture, performance_review, scale_plan, resource_align, learn_share_branch])
loop_body.order.add_edge(data_capture, performance_review)
loop_body.order.add_edge(performance_review, scale_plan)
loop_body.order.add_edge(scale_plan, resource_align)
loop_body.order.add_edge(resource_align, learn_share_branch)

# The LOOP operator: execute loop_body, then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    trend_scan, idea_harvest, workshop_host, concept_filter,
    prototype_build, expert_review, feasibility_check, risk_assess,
    pilot_launch, loop, scale_plan, resource_align,
    learn_share, culture_embed
])

# Add the sequential dependencies
root.order.add_edge(trend_scan, idea_harvest)
root.order.add_edge(idea_harvest, workshop_host)
root.order.add_edge(workshop_host, concept_filter)
root.order.add_edge(concept_filter, prototype_build)
root.order.add_edge(prototype_build, expert_review)
root.order.add_edge(expert_review, feasibility_check)
root.order.add_edge(feasibility_check, risk_assess)
root.order.add_edge(risk_assess, pilot_launch)
root.order.add_edge(pilot_launch, loop)

# After the loop, add the scaling and embedding activities
root.order.add_edge(loop, scale_plan)
root.order.add_edge(scale_plan, resource_align)
root.order.add_edge(resource_align, learn_share)
root.order.add_edge(learn_share, culture_embed)