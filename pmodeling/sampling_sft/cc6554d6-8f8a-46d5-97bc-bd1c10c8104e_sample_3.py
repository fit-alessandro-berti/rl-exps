import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
df = Transition(label='Demand Forecast')
ra = Transition(label='Risk Assess')
sa = Transition(label='Supplier Audit')
iscan = Transition(label='Inventory Scan')
ro = Transition(label='Route Optimize')
op = Transition(label='Order Prioritize')
cr = Transition(label='Contract Review')
dm = Transition(label='Delay Monitor')
sr = Transition(label='Shipment Reroute')
ca = Transition(label='Cost Analyze')
cc = Transition(label='Compliance Check')
ae = Transition(label='Alternative Engage')
ir = Transition(label='Inventory Reallocate')
pt = Transition(label='Performance Track')
fl = Transition(label='Feedback Loop')
su = Transition(label='Strategy Update')

# Build the loop body: Order Prioritize -> Route Optimize -> Delay Monitor -> Shipment Reroute
body = StrictPartialOrder(nodes=[op, ro, dm, sr])
body.order.add_edge(op, ro)
body.order.add_edge(ro, dm)
body.order.add_edge(dm, sr)

# Loop: perform the body, then either exit or repeat the body
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, body])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    df, ra, sa, iscan, loop, ca, cc, ae, ir, pt, fl, su
])
# Demand Forecast -> Risk Assess -> Supplier Audit -> Inventory Scan
root.order.add_edge(df, ra)
root.order.add_edge(ra, sa)
root.order.add_edge(sa, iscan)
# Inventory Scan -> (Loop: Order Prioritize -> Route Optimize -> Delay Monitor -> Shipment Reroute)
root.order.add_edge(iscan, loop)
# Loop -> Cost Analyze -> Compliance Check -> Alternative Engage -> Inventory Reallocate
root.order.add_edge(loop, ca)
root.order.add_edge(ca, cc)
root.order.add_edge(cc, ae)
root.order.add_edge(ae, ir)
# Inventory Reallocate -> Performance Track -> Feedback Loop -> Strategy Update
root.order.add_edge(ir, pt)
root.order.add_edge(pt, fl)
root.order.add_edge(fl, su)