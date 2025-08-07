import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
ia = Transition(label='Initial Assess')
cs = Transition(label='Artifact Scan')
cm = Transition(label='Condition Map')
mt = Transition(label='Material Test')
cp = Transition(label='Cleaning Phase')
sc = Transition(label='Stability Check')
mr = Transition(label='Minor Repair')
sr = Transition(label='Surface Restore')
cr = Transition(label='Coating Apply')
sr2 = Transition(label='Structural Reinforce')
er = Transition(label='Ethics Review')
pv = Transition(label='Provenance Verify')
cu = Transition(label='Client Update')
fr = Transition(label='Final Report')
asr = Transition(label='Archive Store')

# Define the cleaning‐repair sequence as a partial order
clean_repair = StrictPartialOrder(nodes=[cp, mr, sr])
# No edges => they are concurrent

# Define the structural‐coating loop: Structural Reinforce then Coating Apply, repeated until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[sr2, cr])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    ia, cs, cm, mt,
    clean_repair,
    sc,
    loop,
    er, pv,
    cu,
    fr, asr
])

# Add the control‐flow edges
root.order.add_edge(ia, cs)
root.order.add_edge(cs, cm)
root.order.add_edge(cm, mt)
root.order.add_edge(mt, clean_repair)
root.order.add_edge(clean_repair, sc)
root.order.add_edge(sc, loop)
root.order.add_edge(loop, er)
root.order.add_edge(er, pv)
root.order.add_edge(pv, cu)
root.order.add_edge(cu, fr)
root.order.add_edge(fr, asr)