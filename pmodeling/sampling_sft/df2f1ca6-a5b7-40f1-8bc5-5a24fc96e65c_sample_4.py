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
sp = Transition(label='Shipment Plan')
dfc = Transition(label='Demand Forecast')
pa = Transition(label='Price Adjust')
isync = Transition(label='Inventory Sync')
trend = Transition(label='Trend Monitor')
ml = Transition(label='Market Analysis')
fl = Transition(label='Feedback Loop')
cc = Transition(label='Craft Coordination')

# Loop for demand and pricing adaptation
demand_loop = OperatorPOWL(operator=Operator.LOOP, children=[dfc, pa])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, av, sr, df, bp, qc, cp, op, sp,
    demand_loop, isync, trend, ml, fl, cc
])

# Add sequential dependencies
root.order.add_edge(ms, av)
root.order.add_edge(av, sr)
root.order.add_edge(sr, df)
root.order.add_edge(df, bp)
root.order.add_edge(bp, qc)
root.order.add_edge(qc, cp)
root.order.add_edge(cp, op)
root.order.add_edge(op, sp)

# Demand and pricing loop: after QC, enter loop then exit
root.order.add_edge(qc, demand_loop)
root.order.add_edge(demand_loop, sp)

# Inventory sync and market analysis before demand forecast
root.order.add_edge(isync, demand_loop)
root.order.add_edge(ml, demand_loop)

# Trend monitoring before market analysis
root.order.add_edge(trend, ml)

# Feedback loop after shipment
root.order.add_edge(sp, fl)
root.order.add_edge(fl, cc)

# Loop for craft coordination within demand adaptation
root.order.add_edge(demand_loop, cc)