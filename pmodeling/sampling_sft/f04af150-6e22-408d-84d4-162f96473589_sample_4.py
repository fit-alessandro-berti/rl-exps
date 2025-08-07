import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Material Sourcing')
sv = Transition(label='Supplier Vetting')
dr = Transition(label='Design Review')
pb = Transition(label='Prototype Build')
qa = Transition(label='Quality Audit')
bs = Transition(label='Batch Scheduling')
hc = Transition(label='Handcrafting')
pd = Transition(label='Packaging Design')
cl = Transition(label='Custom Labeling')
sc = Transition(label='Sustainability Check')
isync = Transition(label='Inventory Sync')
ma = Transition(label='Market Analysis')
oa = Transition(label='Order Aggregation')
dp = Transition(label='Distribution Plan')
cf = Transition(label='Customer Feedback')

# Loop for iterative design-build-audit cycle
design_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pb, qa]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, sv, dr, design_loop, bs, hc,
    pd, cl, sc, isync, ma, oa, dp, cf
])

# Add edges
root.order.add_edge(ms, sv)
root.order.add_edge(sv, dr)
root.order.add_edge(dr, design_loop)
root.order.add_edge(design_loop, bs)
root.order.add_edge(bs, hc)
root.order.add_edge(hc, pd)
root.order.add_edge(pd, cl)
root.order.add_edge(cl, sc)
root.order.add_edge(sc, isync)
root.order.add_edge(isync, ma)
root.order.add_edge(ma, oa)
root.order.add_edge(oa, dp)
root.order.add_edge(dp, cf)

# Print the root model for verification
print(root)