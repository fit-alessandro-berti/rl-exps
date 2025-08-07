import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
ms = Transition(label='Milk Sourcing')
cs = Transition(label='Culture Selection')
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

# Build the loop for aging and monitoring
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[em, fp])

# Build the partial order for the main workflow
main_po = StrictPartialOrder(nodes=[
    ms, cs, mt, cf, ws, mc, sp, asg, loop_aging, pd, be, qa, rs, tp, dt, cfb
])
main_po.order.add_edge(ms, cs)
main_po.order.add_edge(cs, mt)
main_po.order.add_edge(mt, cf)
main_po.order.add_edge(cf, ws)
main_po.order.add_edge(ws, mc)
main_po.order.add_edge(mc, sp)
main_po.order.add_edge(sp, asg)
main_po.order.add_edge(asg, loop_aging)
main_po.order.add_edge(loop_aging, pd)
main_po.order.add_edge(pd, be)
main_po.order.add_edge(be, qa)
main_po.order.add_edge(qa, rs)
main_po.order.add_edge(rs, tp)
main_po.order.add_edge(tp, dt)
main_po.order.add_edge(dt, cfb)

# Build the final partial order with overall flow
root = StrictPartialOrder(nodes=[
    ms, cs, mt, cf, ws, mc, sp, asg, loop_aging, pd, be, qa, rs, tp, dt, cfb
])
root.order.add_edge(ms, cs)
root.order.add_edge(cs, mt)
root.order.add_edge(mt, cf)
root.order.add_edge(cf, ws)
root.order.add_edge(ws, mc)
root.order.add_edge(mc, sp)
root.order.add_edge(sp, asg)
root.order.add_edge(asg, loop_aging)
root.order.add_edge(loop_aging, pd)
root.order.add_edge(pd, be)
root.order.add_edge(be, qa)
root.order.add_edge(qa, rs)
root.order.add_edge(rs, tp)
root.order.add_edge(tp, dt)
root.order.add_edge(dt, cfb)

# Add the overall ordering from the main workflow
for src, tgt in main_po.order.edges:
    root.order.add_edge(src, tgt)