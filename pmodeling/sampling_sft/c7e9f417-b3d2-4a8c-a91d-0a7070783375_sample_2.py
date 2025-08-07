import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ba = Transition(label='Brand Audit')
eq = Transition(label='Equity Review')
ma = Transition(label='Market Analysis')
lc = Transition(label='Legal Clearance')
tc = Transition(label='Trademark Check')
pm = Transition(label='Portfolio Merge')
cs = Transition(label='Customer Sync')
ca = Transition(label='Cultural Align')
ib = Transition(label='Internal Brief')
cd = Transition(label='Campaign Design')
rp = Transition(label='Resource Plan')
sm = Transition(label='Stakeholder Meet')
lp = Transition(label='Launch Prep')
fl = Transition(label='Feedback Loop')
pt = Transition(label='Performance Track')

# Build the loop body: Feedback Loop -> Performance Track
loop_body = StrictPartialOrder(nodes=[fl, pt])
loop_body.order.add_edge(fl, pt)

# Define the loop: do Launch Prep, then optionally do Feedback Loop -> Performance Track and repeat
launch_loop = OperatorPOWL(operator=Operator.LOOP, children=[lp, loop_body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    ba, eq, ma, lc, tc,
    pm, cs, ca, ib, cd,
    launch_loop,
    sm
])

# Add the control-flow edges
root.order.add_edge(ba, eq)
root.order.add_edge(eq, ma)
root.order.add_edge(ma, lc)
root.order.add_edge(lc, tc)
root.order.add_edge(tc, pm)
root.order.add_edge(pm, cs)
root.order.add_edge(cs, ca)
root.order.add_edge(ca, ib)
root.order.add_edge(ib, cd)
root.order.add_edge(cd, launch_loop)
root.order.add_edge(launch_loop, sm)