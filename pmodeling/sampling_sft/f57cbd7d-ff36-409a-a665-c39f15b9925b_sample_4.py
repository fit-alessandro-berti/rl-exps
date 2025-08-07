import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ts = Transition(label='Trend Scan')
isprint = Transition(label='Idea Sprint')
fc = Transition(label='Feasibility Check')
rr = Transition(label='Risk Review')
tp = Transition(label='Tech Prototype')
ms = Transition(label='Market Simulate')
sa = Transition(label='Stakeholder Align')
ba = Transition(label='Budget Adjust')
tsrc = Transition(label='Talent Source')
pl = Transition(label='Pilot Launch')
dr = Transition(label='Data Refine')
sa2 = Transition(label='Scale Analysis')
ip = Transition(label='Integration Plan')
cm = Transition(label='Change Manage')
kt = Transition(label='Knowledge Transfer')

# Define the loop body for iterative pilot-launch refinement
loop_body = StrictPartialOrder(nodes=[dr, sa2, ip, cm, kt])
loop_body.order.add_edge(dr, sa2)
loop_body.order.add_edge(sa2, ip)
loop_body.order.add_edge(ip, cm)
loop_body.order.add_edge(cm, kt)

# Loop operator: do Pilot Launch, then optionally do the loop_body again
loop = OperatorPOWL(operator=Operator.LOOP, children=[pl, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ts, isprint, fc, rr, tp, ms, sa, ba, tsrc,
    loop, sa2
])

# Define the sequence of activities
root.order.add_edge(ts, isprint)
root.order.add_edge(isprint, fc)
root.order.add_edge(fc, rr)
root.order.add_edge(rr, tp)
root.order.add_edge(tp, ms)
root.order.add_edge(ms, sa)
root.order.add_edge(sa, ba)
root.order.add_edge(ba, tsrc)
root.order.add_edge(tsrc, loop)
root.order.add_edge(loop, sa2)