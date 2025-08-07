import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Milk Sourcing')
ct = Transition(label='Culture Selection')
mt = Transition(label='Milk Testing')
cf = Transition(label='Curd Formation')
ws = Transition(label='Whey Separation')
mc = Transition(label='Molding Cheese')
sp = Transition(label='Salting Process')
asg = Transition(label='Aging Setup')
em = Transition(label='Env Monitoring')
fp = Transition(label='Flavor Profiling')
pd = Transition(label='Packaging Design')
be = Transition(label='Blockchain Entry')
qa = Transition(label='Quality Audit')
rs = Transition(label='Retail Sync')
tp = Transition(label='Transport Prep')
dt = Transition(label='Delivery Tracking')
cfb = Transition(label='Customer Feedback')

# Define the adaptive aging loop: Env Monitoring then Flavor Profiling
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[em, fp])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    ms, ct, mt, cf, ws, mc, sp, asg, aging_loop,
    pd, be, qa, rs, tp, dt, cfb
])

# Sequence: Milk Sourcing -> Culture Selection -> Milk Testing -> Curd Formation -> Whey Separation -> Molding Cheese -> Salting Process
root.order.add_edge(ms, ct)
root.order.add_edge(ct, mt)
root.order.add_edge(mt, cf)
root.order.add_edge(cf, ws)
root.order.add_edge(ws, mc)
root.order.add_edge(mc, sp)

# After salting, go directly to aging setup
root.order.add_edge(sp, asg)

# After aging, the loop begins
root.order.add_edge(asg, aging_loop)

# After the loop, we branch into packaging/design and blockchain entry
root.order.add_edge(aging_loop, pd)
root.order.add_edge(aging_loop, be)

# Quality audit, then sync with retail
root.order.add_edge(pd, qa)
root.order.add_edge(be, qa)
root.order.add_edge(qa, rs)

# After retail sync, prep transport and track delivery
root.order.add_edge(rs, tp)
root.order.add_edge(tp, dt)

# Finally, customer feedback
root.order.add_edge(dt, cfb)