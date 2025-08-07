import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
da = Transition(label='Data Aggregation')
ad = Transition(label='Anomaly Detect')
ra = Transition(label='Risk Assess')
dm = Transition(label='Demand Model')
sn = Transition(label='Stakeholder Sync')
an = Transition(label='Auto Negotiate')
io = Transition(label='Inventory Optimize')
cp = Transition(label='Contingency Plan')
ra2 = Transition(label='Resource Allocate')
sc = Transition(label='Sustainability Check')
cv = Transition(label='Compliance Verify')
iscore = Transition(label='Impact Score')
dp = Transition(label='Distribution Plan')
fl = Transition(label='Feedback Loop')
pa = Transition(label='Performance Audit')
se = Transition(label='Schedule Execute')

# Define the stakeholder feedback loop: Stakeholder Sync -> Auto Negotiate -> Inventory Optimize
feedback_loop = StrictPartialOrder(nodes=[sn, an, io])
feedback_loop.order.add_edge(sn, an)
feedback_loop.order.add_edge(an, io)

# Define the performance audit sequence: Performance Audit -> Schedule Execute
performance_audit = StrictPartialOrder(nodes=[pa, se])
performance_audit.order.add_edge(pa, se)

# Build the root partial order with the main adaptive supply chain process
root = StrictPartialOrder(nodes=[
    da, ad, ra, dm, feedback_loop,
    cp, ra2, sc, cv, iscore, dp,
    fl, performance_audit
])

# Add the control-flow dependencies
root.order.add_edge(da, ad)
root.order.add_edge(ad, ra)
root.order.add_edge(ra, dm)
root.order.add_edge(dm, feedback_loop)
root.order.add_edge(ra, cp)
root.order.add_edge(cp, ra2)
root.order.add_edge(ra2, sc)
root.order.add_edge(sc, cv)
root.order.add_edge(cv, iscore)
root.order.add_edge(iscore, dp)
root.order.add_edge(dp, fl)
root.order.add_edge(fl, performance_audit)
root.order.add_edge(performance_audit, se)

# Output the root partial order
print(root)