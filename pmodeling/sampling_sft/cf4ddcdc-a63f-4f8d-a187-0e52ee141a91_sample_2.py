import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
rr = Transition(label='Return Request')
ac = Transition(label='Authorization Check')
ps = Transition(label='Pickup Schedule')
td = Transition(label='Transport Dispatch')
rg = Transition(label='Receiving Goods')
qi = Transition(label='Quality Inspect')
sp = Transition(label='Sort Items')
rp = Transition(label='Refurbish Prep')
rc = Transition(label='Recycle Process')
iu = Transition(label='Inventory Update')
cn = Transition(label='Customer Notify')
da = Transition(label='Disposal Arrange')
ca = Transition(label='Compliance Audit')
caudit = Transition(label='Compliance Audit')  # duplicate for loop
co = Transition(label='Cost Analysis')
rgen = Transition(label='Report Generate')

# Loop for compliance audit (repeat until no errors)
loop = OperatorPOWL(operator=Operator.LOOP, children=[caudit, ca])

# Build the partial order
root = StrictPartialOrder(nodes=[
    rr, ac, ps, td, rg, qi, sp, rp, rc, iu, cn, da, loop, co, rgen
])

# Define the control-flow dependencies
root.order.add_edge(rr, ac)
root.order.add_edge(ac, ps)
root.order.add_edge(ps, td)
root.order.add_edge(td, rg)
root.order.add_edge(rg, qi)
root.order.add_edge(qi, sp)
root.order.add_edge(sp, rp)
root.order.add_edge(rp, rc)
root.order.add_edge(rc, iu)
root.order.add_edge(iu, cn)
root.order.add_edge(cn, da)
root.order.add_edge(da, loop)
root.order.add_edge(loop, co)
root.order.add_edge(co, rgen)