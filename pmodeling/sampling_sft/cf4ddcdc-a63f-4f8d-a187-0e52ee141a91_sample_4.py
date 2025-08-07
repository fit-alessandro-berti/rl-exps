import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
rr    = Transition(label='Return Request')
auth  = Transition(label='Authorization Check')
ps    = Transition(label='Pickup Schedule')
td    = Transition(label='Transport Dispatch')
rg    = Transition(label='Receiving Goods')
qi    = Transition(label='Quality Inspect')
sorti = Transition(label='Sort Items')
refp  = Transition(label='Refurbish Prep')
rp    = Transition(label='Recycle Process')
inv   = Transition(label='Inventory Update')
cn    = Transition(label='Customer Notify')
dp    = Transition(label='Disposal Arrange')
ca    = Transition(label='Compliance Audit')
ca2   = Transition(label='Compliance Audit')  # duplicate for loop
cost  = Transition(label='Cost Analysis')
rgen  = Transition(label='Report Generate')

# Define the loop body: Compliance Audit -> Cost Analysis -> Report Generate
body = StrictPartialOrder(nodes=[ca, cost, rgen])
body.order.add_edge(ca, cost)
body.order.add_edge(cost, rgen)

# Loop: do Compliance Audit, then optionally do the body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[ca2, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[rr, auth, ps, td, rg, qi, sorti, refp, rp, inv, cn, dp, loop, ca2])
root.order.add_edge(rr, auth)
root.order.add_edge(auth, ps)
root.order.add_edge(ps, td)
root.order.add_edge(td, rg)
root.order.add_edge(rg, qi)
root.order.add_edge(qi, sorti)
root.order.add_edge(sorti, refp)
root.order.add_edge(refp, rp)
root.order.add_edge(rp, inv)
root.order.add_edge(inv, cn)
root.order.add_edge(cn, dp)
root.order.add_edge(cn, loop)
root.order.add_edge(loop, ca2)  # to ensure the loop is executed at least once