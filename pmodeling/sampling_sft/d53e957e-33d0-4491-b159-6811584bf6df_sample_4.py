import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
dc = Transition(label='Data Capture')
ts = Transition(label='Trend Scan')
iw = Transition(label='Idea Workshop')
cd = Transition(label='Concept Draft')
er = Transition(label='Expert Review')
pb = Transition(label='Prototype Build')
rc = Transition(label='Regulation Check')
ia = Transition(label='IP Alignment')
ss = Transition(label='Supply Sync')
mm = Transition(label='Market Mapping')
pl = Transition(label='Pilot Launch')
fl = Transition(label='Feedback Loop')
di = Transition(label='Design Iterate')
im = Transition(label='Impact Measure')
sa = Transition(label='Strategy Adapt')

# Loop for continuous monitoring & adaptation
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[im, sa]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    dc, ts, iw, cd, er, pb, rc, ia, ss, mm, pl, fl, di, monitor_loop
])

# Sequential dependencies
root.order.add_edge(dc, ts)
root.order.add_edge(ts, iw)
root.order.add_edge(iw, cd)
root.order.add_edge(cd, er)
root.order.add_edge(er, pb)
root.order.add_edge(pb, rc)
root.order.add_edge(rc, ia)
root.order.add_edge(ia, ss)
root.order.add_edge(ss, mm)
root.order.add_edge(mm, pl)
root.order.add_edge(pl, fl)
root.order.add_edge(fl, di)
root.order.add_edge(di, im)

# Loop at the end for continuous monitoring & adaptation
root.order.add_edge(im, monitor_loop)
root.order.add_edge(monitor_loop, im)