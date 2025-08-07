import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ts = Transition(label='Trend Sensing')
ifusion = Transition(label='Idea Fusion')
pb = Transition(label='Prototype Build')
er = Transition(label='Expert Review')
ft = Transition(label='Field Testing')
ip_analysis = Transition(label='IP Analysis')
compliance = Transition(label='Compliance Check')
ps = Transition(label='Partner Setup')
up = Transition(label='User Profiling')
lp = Transition(label='Launch Prep')
fl = Transition(label='Feedback Loop')
sp = Transition(label='Scale Planning')
ra = Transition(label='Risk Assess')
ds = Transition(label='Demand Scan')

# Loop: Field Testing -> Feedback Loop -> repeat
testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[ft, fl])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ts, ifusion, pb, testing_loop,
    er, ip_analysis, compliance, ps,
    up, lp, sp, ra, ds
])

# Define the control-flow dependencies
root.order.add_edge(ts, ifusion)
root.order.add_edge(ifusion, pb)
root.order.add_edge(pb, testing_loop)
root.order.add_edge(testing_loop, er)
root.order.add_edge(er, ip_analysis)
root.order.add_edge(ip_analysis, compliance)
root.order.add_edge(compliance, ps)
root.order.add_edge(pb, up)
root.order.add_edge(up, lp)
root.order.add_edge(lp, sp)
root.order.add_edge(sp, ra)
root.order.add_edge(ra, ds)

# Print the root model for verification
print(root)