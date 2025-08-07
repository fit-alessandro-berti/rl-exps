import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
dc = Transition(label='Data Capture')
fp = Transition(label='Fingerprint Art')
ri = Transition(label='Record Input')
hc = Transition(label='Historical Check')
sv = Transition(label='Stakeholder Vote')
cv = Transition(label='Consensus Validate')
te = Transition(label='Timestamp Entry')
lu = Transition(label='Ledger Update')
ascan = Transition(label='AI PatternScan')
flag = Transition(label='Flag Anomaly')
ds = Transition(label='Dispute Submit')
pr = Transition(label='Panel Review')
ar = Transition(label='Arbitrate Case')
tm = Transition(label='Trade Monitor')
fl = Transition(label='Feedback Loop')
ins = Transition(label='Insurance Sync')
cn = Transition(label='Collector Notify')

# Loop for anomaly detection: Flag Anomaly -> Dispute Submit -> Panel Review -> Arbitrate Case
anomaly_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[flag, ds, pr, ar]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    dc, fp, ri, hc, sv, cv, te, lu,
    ascan, anomaly_loop,
    tm, fl, ins, cn
])

# Sequential control-flow edges
root.order.add_edge(dc, fp)
root.order.add_edge(fp, ri)
root.order.add_edge(ri, hc)
root.order.add_edge(hc, sv)
root.order.add_edge(sv, cv)
root.order.add_edge(cv, te)
root.order.add_edge(te, lu)
root.order.add_edge(lu, ascan)
root.order.add_edge(ascan, anomaly_loop)
root.order.add_edge(anomaly_loop, tm)
root.order.add_edge(tm, fl)
root.order.add_edge(fl, ins)
root.order.add_edge(ins, cn)