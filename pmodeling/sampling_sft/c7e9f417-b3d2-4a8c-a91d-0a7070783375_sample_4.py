import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Define the feedback‐loop sub‐process: Feedback Loop -> Performance Track -> Feedback Loop…
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, pt])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ba, eq, ma, lc, tc, pm, cs, ca, ib, cd, rp, sm, lp, feedback_loop
])

# Add the control‐flow edges
root.order.add_edge(ba, eq)
root.order.add_edge(ba, ma)
root.order.add_edge(eq, lc)
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
root.order.add_edge(lp, feedback_loop)