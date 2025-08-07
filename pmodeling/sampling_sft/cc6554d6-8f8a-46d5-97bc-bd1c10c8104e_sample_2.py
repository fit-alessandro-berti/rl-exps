import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
df = Transition(label='Demand Forecast')
ra = Transition(label='Risk Assess')
sa = Transition(label='Supplier Audit')
isv = Transition(label='Inventory Scan')
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

# Define the loop body (after a delay, reroute and analyze)
body = StrictPartialOrder(nodes=[dm, sr, ca, cc, ae, ir])
body.order.add_edge(dm, sr)
body.order.add_edge(sr, ca)
body.order.add_edge(ca, cc)
body.order.add_edge(cc, ae)
body.order.add_edge(ae, ir)

# Define the loop: after delay, execute the body then optionally loop again
loop = OperatorPOWL(operator=Operator.LOOP, children=[dm, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    df, ra, sa, isv, ro, op, cr,
    loop, pt, fl, su
])

# Add control-flow dependencies
root.order.add_edge(df, ra)
root.order.add_edge(ra, sa)
root.order.add_edge(sa, isv)
root.order.add_edge(isv, ro)
root.order.add_edge(ro, op)
root.order.add_edge(op, cr)

# Body execution after delay
root.order.add_edge(loop, pt)

# Optional loop reentry
root.order.add_edge(pt, loop)

# Final feedback and strategy update
root.order.add_edge(loop, fl)
root.order.add_edge(fl, su)