import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cc = Transition(label='Client Consult')
sf = Transition(label='Spec Finalize')
dd = Transition(label='Design Draft')
at = Transition(label='Aerodynamics Test')
ai = Transition(label='AI Integration')
ms = Transition(label='Material Sourcing')
co = Transition(label='Component Order')
al = Transition(label='Assembly Line')
fi = Transition(label='Firmware Install')
et = Transition(label='Environmental Test')
qc = Transition(label='Quality Check')
bp = Transition(label='Brand Packaging')
sp = Transition(label='Shipping Prep')
ds = Transition(label='Delivery Schedule')
ps = Transition(label='Post-Sale Support')

# Loop for iterative design refinement
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[at, ai])

# Build the partial order
root = StrictPartialOrder(nodes=[
    cc, sf, dd, design_loop,
    ms, co, al, fi,
    et, qc, bp,
    sp, ds, ps
])

# Define the control-flow dependencies
root.order.add_edge(cc, sf)
root.order.add_edge(sf, dd)
root.order.add_edge(dd, design_loop)

root.order.add_edge(design_loop, ms)
root.order.add_edge(ms, co)
root.order.add_edge(co, al)
root.order.add_edge(al, fi)
root.order.add_edge(fi, et)

root.order.add_edge(et, qc)
root.order.add_edge(qc, bp)

root.order.add_edge(bp, sp)
root.order.add_edge(sp, ds)
root.order.add_edge(ds, ps)

print(root)