import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ov = Transition(label='Order Validate')
ro = Transition(label='Route Optimize')
da = Transition(label='Drone Assign')
pc = Transition(label='Preflight Check')
lp = Transition(label='Load Package')
fl = Transition(label='Flight Launch')
tm = Transition(label='Traffic Monitor')
wa = Transition(label='Weather Assess')
oa = Transition(label='Obstacle Avoid')
bc = Transition(label='Battery Check')
dv = Transition(label='Delivery Verify')
bs = Transition(label='Biometric Scan')
pr = Transition(label='Package Release')
rf = Transition(label='Return Flight')
pf = Transition(label='Post Flight')
da1 = Transition(label='Data Analyze')
fc = Transition(label='Feedback Collect')

# Loop for continuous monitoring and handling of unexpected issues
loop_monitor = OperatorPOWL(
    operator=Operator.LOOP,
    children=[tm, wa, oa, bc]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    ov, ro, da, pc, lp, fl,
    loop_monitor,
    dv, bs, pr, rf, pf,
    da1, fc
])

# Define the control-flow dependencies
root.order.add_edge(ov, ro)
root.order.add_edge(ro, da)
root.order.add_edge(da, pc)
root.order.add_edge(pc, lp)
root.order.add_edge(lp, fl)
root.order.add_edge(fl, loop_monitor)
root.order.add_edge(loop_monitor, dv)
root.order.add_edge(dv, bs)
root.order.add_edge(bs, pr)
root.order.add_edge(pr, rf)
root.order.add_edge(rf, pf)
root.order.add_edge(pf, da1)
root.order.add_edge(da1, fc)

print(root)