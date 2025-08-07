import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
cp = Transition(label='Curd Processing')
sa = Transition(label='Salt Application')
mi = Transition(label='Mold Inoculation')
pm = Transition(label='Press Molding')
bs = Transition(label='Brine Soaking')
asg = Transition(label='Aging Setup')
hc = Transition(label='Humidity Control')
mc = Transition(label='Microbial Check')
pd = Transition(label='Packaging Design')
lp = Transition(label='Label Printing')
tl = Transition(label='Trace Logging')
dp = Transition(label='Distribution Plan')
cr = Transition(label='Customer Review')
ia = Transition(label='Inventory Audit')
sa2 = Transition(label='Sustainability Audit')

# Loop for seasonal staff coordination: do daily tasks then optionally do audit & sustainability checks
staff_loop = OperatorPOWL(operator=Operator.LOOP, children=[asg, ia, sa2])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ms, qt, cp, sa, mi, pm, bs,
    asg, hc, mc,
    pd, lp, tl, dp, cr
])

# Add sequential dependencies
root.order.add_edge(ms, qt)
root.order.add_edge(qt, cp)
root.order.add_edge(cp, sa)
root.order.add_edge(sa, mi)
root.order.add_edge(mi, pm)
root.order.add_edge(pm, bs)
root.order.add_edge(bs, asg)
root.order.add_edge(asg, staff_loop)
root.order.add_edge(staff_loop, hc)
root.order.add_edge(staff_loop, mc)
root.order.add_edge(mc, pd)
root.order.add_edge(pd, lp)
root.order.add_edge(lp, tl)
root.order.add_edge(tl, dp)
root.order.add_edge(dp, cr)

# Print the root model for verification
print(root)