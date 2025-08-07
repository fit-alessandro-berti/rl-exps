import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Material Sourcing')
sv = Transition(label='Supplier Vetting')
dr = Transition(label='Design Review')
pb = Transition(label='Prototype Build')
qa = Transition(label='Quality Audit')
hs = Transition(label='Handcrafting')
pd = Transition(label='Packaging Design')
cl = Transition(label='Custom Labeling')
sc = Transition(label='Sustainability Check')
isync = Transition(label='Inventory Sync')
ma = Transition(label='Market Analysis')
oa = Transition(label='Order Aggregation')
dp = Transition(label='Distribution Plan')
cf = Transition(label='Customer Feedback')

# Loop for continuous feedback and analysis
loop_analysis = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cf, ma]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, sv, dr, pb, qa, hs,
    pd, cl, sc, isync,
    ma, oa, dp, loop_analysis
])

# Add control-flow dependencies
root.order.add_edge(ms, sv)
root.order.add_edge(sv, dr)
root.order.add_edge(dr, pb)
root.order.add_edge(pb, qa)
root.order.add_edge(qa, hs)
root.order.add_edge(hs, pd)
root.order.add_edge(pd, cl)
root.order.add_edge(cl, sc)
root.order.add_edge(sc, isync)
root.order.add_edge(isync, ma)
root.order.add_edge(ma, loop_analysis)
root.order.add_edge(loop_analysis, oa)
root.order.add_edge(oa, dp)

# Print the root model for verification
print(root)