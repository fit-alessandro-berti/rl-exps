import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
cp = Transition(label='Culture Prep')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
mc = Transition(label='Molding Cheese')
pb = Transition(label='Pressing Blocks')
sp = Transition(label='Salting Process')
am = Transition(label='Aging Monitoring')
fp = Transition(label='Flavor Profiling')
pd = Transition(label='Packaging Design')
ccs = Transition(label='Compliance Check')
mr = Transition(label='Market Research')
ds = Transition(label='Direct Shipping')
cf = Transition(label='Customer Feedback')
ra = Transition(label='Recipe Adjust')

# Define the loop for aging monitoring and flavor profiling
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[am, fp])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    ms, qt, cp, mp, cc, wd, mc, pb, sp, loop_aging, pd, ccs,
    mr, ds, cf, ra
])

# Sequence for cheese production
root.order.add_edge(ms, qt)
root.order.add_edge(qt, cp)
root.order.add_edge(cp, mp)
root.order.add_edge(mp, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mc)
root.order.add_edge(mc, pb)
root.order.add_edge(pb, sp)

# After pressing, go directly to aging monitoring loop
root.order.add_edge(sp, loop_aging)

# After the loop, do packaging design
root.order.add_edge(loop_aging, pd)

# Compliance and research after packaging
root.order.add_edge(pd, ccs)
root.order.add_edge(pd, mr)

# Shipping and feedback after compliance and research
root.order.add_edge(ccs, ds)
root.order.add_edge(mr, ds)
root.order.add_edge(ds, cf)

# Recipe adjust after feedback
root.order.add_edge(cf, ra)

# Final feedback loop: repeat recipe adjust until no more feedback
skip = SilentTransition()
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[ra, skip])
root.order.add_edge(cf, loop_feedback)

print(root)