import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ba = Transition(label='Brand Audit')
er = Transition(label='Equity Review')
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

# Loop for ongoing performance tracking
loop = OperatorPOWL(operator=Operator.LOOP, children=[pt, fl])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ba, er, ma, lc, tc, pm, cs, ca, ib, cd, rp, sm, lp, loop
])

# Define the control-flow dependencies
root.order.add_edge(ba, er)
root.order.add_edge(ba, ma)
root.order.add_edge(er, lc)
root.order.add_edge(ma, lc)
root.order.add_edge(lc, tc)
root.order.add_edge(tc, pm)
root.order.add_edge(pm, cs)
root.order.add_edge(cs, ca)
root.order.add_edge(ca, ib)
root.order.add_edge(ib, cd)
root.order.add_edge(cd, rp)
root.order.add_edge(rp, sm)
root.order.add_edge(sm, lp)
root.order.add_edge(sm, loop)

# Final concurrent activities after loop
root.order.add_edge(loop, lp)