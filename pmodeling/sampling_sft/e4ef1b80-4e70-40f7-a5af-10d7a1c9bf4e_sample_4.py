import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
op_scan    = Transition(label='Opportunity Scan')
idea_work  = Transition(label='Idea Workshop')
concept    = Transition(label='Concept Merge')
resource   = Transition(label='Resource Align')
prototype  = Transition(label='Prototype Build')
feas_test  = Transition(label='Feasibility Test')
pilot      = Transition(label='Pilot Launch')
feedback   = Transition(label='Feedback Gather')
design     = Transition(label='Design Adapt')
compliance = Transition(label='Compliance Check')
scaling    = Transition(label='Scaling Plan')
ip_manage  = Transition(label='IP Management')
market     = Transition(label='Market Sync')
partner    = Transition(label='Partner Review')
exit_str   = Transition(label='Exit Strategy')

# Loop for the iterative process: gather feedback, adapt design, and repeat
loop_body = StrictPartialOrder(nodes=[feedback, design])
loop_body.order.add_edge(feedback, design)

loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype, loop_body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    op_scan,
    idea_work,
    concept,
    resource,
    loop,
    pilot,
    compliance,
    scaling,
    ip_manage,
    market,
    partner,
    exit_str
])

# Define the control‐flow dependencies
root.order.add_edge(op_scan, idea_work)
root.order.add_edge(idea_work, concept)
root.order.add_edge(concept, resource)
root.order.add_edge(resource, loop)
root.order.add_edge(loop, pilot)
root.order.add_edge(pilot, compliance)
root.order.add_edge(compliance, scaling)
root.order.add_edge(scaling, ip_manage)
root.order.add_edge(ip_manage, market)
root.order.add_edge(market, partner)
root.order.add_edge(partner, exit_str)