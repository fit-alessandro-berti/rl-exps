import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
ts = Transition(label='Trend Scan')
is = Transition(label='Idea Sprint')
fc = Transition(label='Feasibility Check')
rr = Transition(label='Risk Review')
tp = Transition(label='Tech Prototype')
ms = Transition(label='Market Simulate')
sa = Transition(label='Stakeholder Align')
ba = Transition(label='Budget Adjust')
ts = Transition(label='Talent Source')
pl = Transition(label='Pilot Launch')
dr = Transition(label='Data Refine')
sa = Transition(label='Scale Analysis')
ip = Transition(label='Integration Plan')
cm = Transition(label='Change Manage')
kt = Transition(label='Knowledge Transfer')

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[tp, sa])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ba, cm])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ip, kt])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[dr, cm])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[sa, ba])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ip, kt])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[dr, cm])

xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop3, xor4])

root = StrictPartialOrder(nodes=[ts, is, fc, rr, tp, ms, sa, ba, ts, pl, dr, sa, ip, cm, kt, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(ts, is)
root.order.add_edge(is, fc)
root.order.add_edge(fc, rr)
root.order.add_edge(rr, tp)
root.order.add_edge(tp, ms)
root.order.add_edge(ms, sa)
root.order.add_edge(sa, ba)
root.order.add_edge(ba, ts)
root.order.add_edge(ts, pl)
root.order.add_edge(pl, dr)
root.order.add_edge(dr, sa)
root.order.add_edge(sa, ip)
root.order.add_edge(ip, cm)
root.order.add_edge(cm, kt)
root.order.add_edge(xor, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)

print(root)