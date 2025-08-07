import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Material Sourcing')
av = Transition(label='Artisan Vetting')
sr = Transition(label='Sample Review')
df = Transition(label='Design Finalize')
cp = Transition(label='Custom Packaging')
cs = Transition(label='Craft Coordination')
sp = Transition(label='Shipment Plan')
dp = Transition(label='Demand Forecast')
pa = Transition(label='Price Adjust')
os = Transition(label='Order Processing')
isync = Transition(label='Inventory Sync')
tl = Transition(label='Trend Monitor')
fl = Transition(label='Feedback Loop')

# Loop for continuous trend monitoring and demand adjustment
loop_demand = OperatorPOWL(
    operator=Operator.LOOP,
    children=[tl, dp]
)

# Exclusive choice between Price Adjust and Inventory Sync
price_or_sync = OperatorPOWL(
    operator=Operator.XOR,
    children=[pa, isync]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, av, sr, df, cp, cs, sp,
    loop_demand,
    price_or_sync,
    dp,
    os
])

# Add dependencies
root.order.add_edge(ms, av)
root.order.add_edge(av, sr)
root.order.add_edge(sr, df)
root.order.add_edge(df, cp)
root.order.add_edge(cp, cs)
root.order.add_edge(cs, sp)
root.order.add_edge(cs, loop_demand)
root.order.add_edge(loop_demand, price_or_sync)
root.order.add_edge(price_or_sync, os)
root.order.add_edge(os, dp)