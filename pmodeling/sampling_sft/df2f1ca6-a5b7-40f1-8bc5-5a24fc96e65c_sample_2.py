import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Material Sourcing')
av = Transition(label='Artisan Vetting')
sr = Transition(label='Sample Review')
df = Transition(label='Design Finalize')
bp = Transition(label='Batch Scheduling')
qc = Transition(label='Quality Check')
cp = Transition(label='Custom Packaging')
op = Transition(label='Order Processing')
sh = Transition(label='Shipment Plan')
ma = Transition(label='Market Analysis')
da = Transition(label='Demand Forecast')
pa = Transition(label='Price Adjust')
isyn = Transition(label='Inventory Sync')
cl = Transition(label='Craft Coordination')
fl = Transition(label='Feedback Loop')
tm = Transition(label='Trend Monitor')

# Loop for iterative demand and pricing adjustment
demand_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[da, pa]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, av, sr, df, bp, qc, cp, op, sh,
    ma, demand_loop, isyn, cl, fl, tm
])

# Add control-flow edges
root.order.add_edge(ms, av)
root.order.add_edge(av, sr)
root.order.add_edge(sr, df)
root.order.add_edge(df, bp)
root.order.add_edge(bp, qc)
root.order.add_edge(qc, cp)
root.order.add_edge(cp, op)
root.order.add_edge(op, sh)
root.order.add_edge(op, ma)
root.order.add_edge(ma, demand_loop)
root.order.add_edge(demand_loop, pa)
root.order.add_edge(pa, demand_loop)
root.order.add_edge(pa, isyn)
root.order.add_edge(isyn, cl)
root.order.add_edge(cl, fl)
root.order.add_edge(fl, tm)

# Optional trend monitoring can occur concurrently
root.order.add_edge(tm, cl)
root.order.add_edge(tm, fl)