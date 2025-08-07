import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ts = Transition(label='Idea Solicitation')
af = Transition(label='AI Filtering')
cv = Transition(label='Community Voting')
er = Transition(label='Expert Review')
pb = Transition(label='Prototype Build')
ut = Transition(label='User Testing')
ifb = Transition(label='Iterate Feedback')
ra = Transition(label='Risk Assess')
cc = Transition(label='Compliance Check')
pl = Transition(label='Pilot Launch')
pt = Transition(label='Performance Track')
ia = Transition(label='Impact Analyze')
ig = Transition(label='Insight Gather')
ca = Transition(label='Cycle Adjust')
fr = Transition(label='Final Report')

# Define the iterative feedback loop: User Testing -> Iterate Feedback -> repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[ut, ifb])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    ts, af, cv, er, pb, loop, ra, cc, pl, pt, ia, ig, ca, fr
])

# Define the control-flow dependencies
root.order.add_edge(ts, af)
root.order.add_edge(af, cv)
root.order.add_edge(af, er)
root.order.add_edge(cv, pb)
root.order.add_edge(er, pb)
root.order.add_edge(pb, loop)
root.order.add_edge(loop, ra)
root.order.add_edge(loop, cc)
root.order.add_edge(ra, pl)
root.order.add_edge(cc, pl)
root.order.add_edge(pl, pt)
root.order.add_edge(pt, ia)
root.order.add_edge(ia, ig)
root.order.add_edge(ig, ca)
root.order.add_edge(ca, fr)