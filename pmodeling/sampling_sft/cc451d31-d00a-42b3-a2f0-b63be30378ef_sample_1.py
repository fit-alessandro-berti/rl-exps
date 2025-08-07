import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ts = Transition(label='Idea Solicitation')
ai = Transition(label='AI Filtering')
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

# Build the iterative prototyping phase as a partial order
prototyping_po = StrictPartialOrder(nodes=[ut, ifb])
prototyping_po.order.add_edge(ut, ifb)

# Build the loop for iterative prototyping
loop = OperatorPOWL(operator=Operator.LOOP, children=[pb, prototyping_po])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[ts, ai, cv, er, loop, ra, cc, pl, pt, ia, ig, ca, fr])

# Define the control-flow dependencies
root.order.add_edge(ts, ai)
root.order.add_edge(ts, cv)
root.order.add_edge(ts, er)
root.order.add_edge(ai, loop)
root.order.add_edge(cv, loop)
root.order.add_edge(er, loop)
root.order.add_edge(loop, ra)
root.order.add_edge(loop, cc)
root.order.add_edge(ra, pl)
root.order.add_edge(cc, pl)
root.order.add_edge(pl, pt)
root.order.add_edge(pl, ia)
root.order.add_edge(pt, ig)
root.order.add_edge(ia, ig)
root.order.add_edge(ig, ca)
root.order.add_edge(ca, fr)