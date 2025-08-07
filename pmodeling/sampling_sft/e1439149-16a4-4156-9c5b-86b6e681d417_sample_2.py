import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
trend_scan      = Transition(label='Trend Scan')
idea_harvest    = Transition(label='Idea Harvest')
workshop_host   = Transition(label='Workshop Host')
concept_filter  = Transition(label='Concept Filter')
prototype_build = Transition(label='Prototype Build')
expert_review   = Transition(label='Expert Review')
feasibility_chk = Transition(label='Feasibility Check')
risk_assess     = Transition(label='Risk Assess')
pilot_launch    = Transition(label='Pilot Launch')
data_capture    = Transition(label='Data Capture')
performance_rev = Transition(label='Performance Review')
scale_plan      = Transition(label='Scale Plan')
resource_align  = Transition(label='Resource Align')
learn_share     = Transition(label='Learn Share')
culture_embed   = Transition(label='Culture Embed')

# Build the main process as a strict partial order
main_process = StrictPartialOrder(nodes=[
    trend_scan, idea_harvest, workshop_host, concept_filter,
    prototype_build, expert_review, feasibility_chk, risk_assess,
    pilot_launch, data_capture, performance_rev,
    scale_plan, resource_align, learn_share, culture_embed
])

# Define the control-flow edges for the main process
main_process.order.add_edge(trend_scan, idea_harvest)
main_process.order.add_edge(idea_harvest, workshop_host)
main_process.order.add_edge(workshop_host, concept_filter)
main_process.order.add_edge(concept_filter, prototype_build)
main_process.order.add_edge(prototype_build, expert_review)
main_process.order.add_edge(expert_review, feasibility_chk)
main_process.order.add_edge(feasibility_chk, risk_assess)
main_process.order.add_edge(risk_assess, pilot_launch)
main_process.order.add_edge(pilot_launch, data_capture)
main_process.order.add_edge(data_capture, performance_rev)
main_process.order.add_edge(performance_rev, scale_plan)
main_process.order.add_edge(scale_plan, resource_align)
main_process.order.add_edge(resource_align, learn_share)
main_process.order.add_edge(learn_share, culture_embed)

# Define the loop: after each pilot launch, review performance and either exit or repeat
loop_body = StrictPartialOrder(nodes=[
    data_capture, performance_rev, scale_plan, resource_align, learn_share, culture_embed
])
loop_body.order.add_edge(data_capture, performance_rev)
loop_body.order.add_edge(performance_rev, scale_plan)
loop_body.order.add_edge(scale_plan, resource_align)
loop_body.order.add_edge(resource_align, learn_share)
loop_body.order.add_edge(learn_share, culture_embed)

# Loop operator: Pilot Launch followed by loop_body then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[pilot_launch, loop_body])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[trend_scan, idea_harvest, workshop_host, concept_filter,
                                 prototype_build, expert_review, feasibility_chk,
                                 risk_assess, loop, scale_plan, resource_align,
                                 learn_share, culture_embed])
root.order.add_edge(trend_scan, idea_harvest)
root.order.add_edge(idea_harvest, workshop_host)
root.order.add_edge(workshop_host, concept_filter)
root.order.add_edge(concept_filter, prototype_build)
root.order.add_edge(prototype_build, expert_review)
root.order.add_edge(expert_review, feasibility_chk)
root.order.add_edge(feasibility_chk, risk_assess)
root.order.add_edge(risk_assess, loop)
root.order.add_edge(loop, scale_plan)
root.order.add_edge(scale_plan, resource_align)
root.order.add_edge(resource_align, learn_share)
root.order.add_edge(learn_share, culture_embed)