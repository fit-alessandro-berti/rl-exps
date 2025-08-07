import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Loop for adaptive inventory management
inventory_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[isync, StrictPartialOrder(nodes=[ms, sv, dr, pb, qa, bs, hc, pd, cl, sc, isync])]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    ms, sv, dr, pb, qa, bs, hc, pd, cl, sc, inventory_loop,
    ma, oa, dp, cf
])

# Define the control-flow dependencies
root.order.add_edge(ms, sv)
root.order.add_edge(sv, dr)
root.order.add_edge(dr, pb)
root.order.add_edge(pb, qa)
root.order.add_edge(qa, bs)
root.order.add_edge(bs, hc)
root.order.add_edge(hc, pd)
root.order.add_edge(pd, cl)
root.order.add_edge(cl, sc)
root.order.add_edge(sc, inventory_loop)

root.order.add_edge(ma, oa)
root.order.add_edge(oa, dp)
root.order.add_edge(dp, cf)

# The loop (inventory_sync) is concurrent with all other activities
for node in root.nodes:
    if node != inventory_loop:
        root.order.add_edge(inventory_loop, node)