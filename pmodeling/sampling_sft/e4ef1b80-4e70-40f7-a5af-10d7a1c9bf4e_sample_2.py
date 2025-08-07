import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
opp_scan    = Transition(label='Opportunity Scan')
idea_work   = Transition(label='Idea Workshop')
concept_mrg = Transition(label='Concept Merge')
res_align   = Transition(label='Resource Align')
prot_build  = Transition(label='Prototype Build')
feas_test   = Transition(label='Feasibility Test')
pilot_launch= Transition(label='Pilot Launch')
feedback    = Transition(label='Feedback Gather')
design_adap = Transition(label='Design Adapt')
compliance  = Transition(label='Compliance Check')
scaling     = Transition(label='Scaling Plan')
ip_manage   = Transition(label='IP Management')
market_sync = Transition(label='Market Sync')
partner_rev = Transition(label='Partner Review')
exit_strat  = Transition(label='Exit Strategy')

# Define the adaptation loop: Adaptation -> Compliance -> Scaling -> IP Management -> Market Sync -> Partner Review
adapt_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    design_adap,
    compliance,
    scaling,
    ip_manage,
    market_sync,
    partner_rev
])

# Assemble the full process as a partial order
root = StrictPartialOrder(nodes=[
    opp_scan,
    idea_work,
    concept_mrg,
    res_align,
    prot_build,
    feas_test,
    pilot_launch,
    feedback,
    adapt_loop,
    exit_strat
])

# Define the control-flow dependencies
root.order.add_edge(opp_scan, idea_work)
root.order.add_edge(idea_work, concept_mrg)
root.order.add_edge(concept_mrg, res_align)
root.order.add_edge(res_align, prot_build)
root.order.add_edge(prot_build, feas_test)
root.order.add_edge(feas_test, pilot_launch)
root.order.add_edge(pilot_launch, feedback)
root.order.add_edge(feedback, adapt_loop)
root.order.add_edge(adapt_loop, pilot_launch)
root.order.add_edge(pilot_launch, exit_strat)