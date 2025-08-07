import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Material Sourcing')
av = Transition(label='Artisan Vetting')
sr = Transition(label='Sample Review')
df = Transition(label='Design Finalize')
cp = Transition(label='Custom Packaging')
oc = Transition(label='Craft Coordination')
bp = Transition(label='Batch Scheduling')
qc = Transition(label='Quality Check')
ip = Transition(label='Inventory Sync')
op = Transition(label='Order Processing')
sp = Transition(label='Shipment Plan')
df = Transition(label='Demand Forecast')
pa = Transition(label='Price Adjust')
ma = Transition(label='Market Analysis')
fl = Transition(label='Feedback Loop')
tm = Transition(label='Trend Monitor')

# Loop for continuous demand monitoring & price adjustment
loop_demand = OperatorPOWL(operator=Operator.LOOP, children=[df, pa])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, av, sr, df, bp, qc, ip, oc, sp, loop_demand, ma, fl, tm
])

# Define control-flow dependencies
root.order.add_edge(ms, av)
root.order.add_edge(av, sr)
root.order.add_edge(sr, df)
root.order.add_edge(df, bp)
root.order.add_edge(bp, qc)
root.order.add_edge(qc, ip)
root.order.add_edge(ip, oc)
root.order.add_edge(oc, sp)
root.order.add_edge(sp, loop_demand)
root.order.add_edge(loop_demand, ma)
root.order.add_edge(ma, fl)
root.order.add_edge(fl, tm)

# The final loop can be exited at any time
root.order.add_edge(tm, loop_demand)