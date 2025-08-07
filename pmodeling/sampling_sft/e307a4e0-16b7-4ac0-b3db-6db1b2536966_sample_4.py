import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ia = Transition(label='Initial Assess')
cs = Transition(label='Artifact Scan')
cm = Transition(label='Condition Map')
mt = Transition(label='Material Test')
cp = Transition(label='Cleaning Phase')
sc = Transition(label='Stability Check')
mr = Transition(label='Minor Repair')
sr = Transition(label='Structural Reinforce')
sr2 = Transition(label='Surface Restore')
ca = Transition(label='Coating Apply')
er = Transition(label='Ethics Review')
pv = Transition(label='Provenance Verify')
cu = Transition(label='Client Update')
fr = Transition(label='Final Report')
asr = Transition(label='Archive Store')

# Loop for repeated minor repairs and structural reinforcements
repair_loop = OperatorPOWL(operator=Operator.LOOP, children=[mr, sr])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ia, cs, cm, mt,
    cp, sc, repair_loop,
    sr2, ca,
    er, pv, cu,
    fr, asr
])

# Sequence of initial steps
root.order.add_edge(ia, cs)
root.order.add_edge(cs, cm)
root.order.add_edge(cm, mt)

# Cleaning phase follows material testing
root.order.add_edge(mt, cp)

# Stability check and repair loop follow cleaning phase
root.order.add_edge(cp, sc)
root.order.add_edge(sc, repair_loop)

# Surface restore and coating apply follow the repair loop
root.order.add_edge(repair_loop, sr2)
root.order.add_edge(sr2, ca)

# Ethics review, provenance verify, client update, final report, and archive store in parallel
root.order.add_edge(er, pv)
root.order.add_edge(pv, cu)
root.order.add_edge(cu, fr)
root.order.add_edge(fr, asr)