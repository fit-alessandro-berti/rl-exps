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

# Loop for continuous feedback and performance tracking
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, pt])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ba, er, ma, lc, tc, pm, cs, ca, ib, cd, rp, sm, lp, feedback_loop
])

# Sequence of Brand Audit to Portfolio Merge
root.order.add_edge(ba, er)
root.order.add_edge(er, ma)
root.order.add_edge(ma, lc)
root.order.add_edge(lc, tc)
root.order.add_edge(tc, pm)

# Parallel customer sync, cultural align, and internal brief
root.order.add_edge(pm, cs)
root.order.add_edge(pm, ca)
root.order.add_edge(pm, ib)

# Parallel campaign design and resource plan
root.order.add_edge(cs, cd)
root.order.add_edge(ca, cd)
root.order.add_edge(ib, cd)
root.order.add_edge(cd, rp)

# Stakeholder meet then launch prep
root.order.add_edge(rp, sm)
root.order.add_edge(sm, lp)

# Finally, the feedback loop (concurrent with launch prep)
root.order.add_edge(lp, feedback_loop)