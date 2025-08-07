import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Loop for continuous monitoring and profiling
loop = OperatorPOWL(operator=Operator.LOOP, children=[em, fp])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, cs, mt, cf, ws, mc, sp, asg, loop, pd, be, qa, rs, tp, dt, cfb
])

# Define the control-flow dependencies
root.order.add_edge(ms, cs)
root.order.add_edge(ms, mt)
root.order.add_edge(cs, mt)
root.order.add_edge(mt, cf)
root.order.add_edge(cf, ws)
root.order.add_edge(ws, mc)
root.order.add_edge(mc, sp)
root.order.add_edge(sp, asg)
root.order.add_edge(asg, loop)
root.order.add_edge(loop, pd)
root.order.add_edge(pd, be)
root.order.add_edge(be, qa)
root.order.add_edge(qa, rs)
root.order.add_edge(rs, tp)
root.order.add_edge(tp, dt)
root.order.add_edge(dt, cfb)

# Print the root model (optional)
print(root)