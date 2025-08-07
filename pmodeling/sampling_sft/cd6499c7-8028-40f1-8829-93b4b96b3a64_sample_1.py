import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
sp = Transition(label='Starter Prep')
mp = Transition(label='Milk Pasteurize')
cf = Transition(label='Curd Formation')
wd = Transition(label='Whey Drain')
cp = Transition(label='Cheese Press')
spc = Transition(label='Salting Process')
asg = Transition(label='Aging Setup')
tc = Transition(label='Temperature Control')
bl = Transition(label='Batch Labeling')
ep = Transition(label='Eco Packaging')
ia = Transition(label='Inventory Audit')
oc = Transition(label='Order Coordination')
rc = Transition(label='Regulatory Check')
sp2 = Transition(label='Shipment Planning')
vl = Transition(label='Vendor Liaison')
wr = Transition(label='Waste Reduction')

# Define the loop for aging and temperature control
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[asg, tc])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, qt, sp, mp, cf, wd, cp, spc, aging_loop, bl, ep, ia, oc, rc, sp2, vl, wr
])

# Define the control-flow dependencies
root.order.add_edge(ms, qt)
root.order.add_edge(qt, sp)
root.order.add_edge(sp, mp)
root.order.add_edge(mp, cf)
root.order.add_edge(cf, wd)
root.order.add_edge(wd, cp)
root.order.add_edge(cp, spc)
root.order.add_edge(spc, aging_loop)
root.order.add_edge(aging_loop, bl)
root.order.add_edge(bl, ep)
root.order.add_edge(ep, ia)
root.order.add_edge(ia, oc)
root.order.add_edge(oc, rc)
root.order.add_edge(rc, sp2)
root.order.add_edge(sp2, vl)
root.order.add_edge(vl, wr)

# Add silent transitions to mark the end of the process
skip = SilentTransition()
root.order.add_edge(wr, skip)