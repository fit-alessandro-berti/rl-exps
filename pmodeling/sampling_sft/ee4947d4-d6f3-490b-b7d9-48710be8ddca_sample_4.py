import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
dc = Transition(label='Data Capture')
fa = Transition(label='Fingerprint Art')
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
isync = Transition(label='Insurance Sync')
cnotify = Transition(label='Collector Notify')

# Define the multi-party consensus loop:
#   A = [dc -> fa -> ri -> hc -> sv]
#   B = [ascan -> flag -> ds -> pr -> ar]
#   LOOP(children=[A, B])
concurrent = StrictPartialOrder(nodes=[dc, fa, ri, hc, sv])
concurrent.order.add_edge(dc, fa)
concurrent.order.add_edge(fa, ri)
concurrent.order.add_edge(ri, hc)
concurrent.order.add_edge(hc, sv)
anomaly = StrictPartialOrder(nodes=[ascan, flag, ds, pr, ar])
anomaly.order.add_edge(ascan, flag)
anomaly.order.add_edge(flag, ds)
anomaly.order.add_edge(ds, pr)
anomaly.order.add_edge(pr, ar)
loop = OperatorPOWL(operator=Operator.LOOP, children=[concurrent, anomaly])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[loop, te, lu, flag, ds, pr, ar, tm, fl, isync, cnotify])
root.order.add_edge(loop, te)
root.order.add_edge(loop, lu)
root.order.add_edge(te, flag)
root.order.add_edge(flag, ds)
root.order.add_edge(ds, pr)
root.order.add_edge(pr, ar)
root.order.add_edge(ar, tm)
root.order.add_edge(tm, fl)
root.order.add_edge(fl, isync)
root.order.add_edge(isync, cnotify)