import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
cb = Transition(label='Client Brief')
dd = Transition(label='Design Draft')
ps = Transition(label='Part Sourcing')
cf = Transition(label='Component Fabric')
ca = Transition(label='Circuit Assembly')
su = Transition(label='Software Upload')
it = Transition(label='Initial Testing')
fc = Transition(label='Flight Calibrate')
pm = Transition(label='Payload Mount')
st = Transition(label='Stress Testing')
fb = Transition(label='Feedback Loop')
qc = Transition(label='Quality Check')
cert = Transition(label='Certification')
pack = Transition(label='Packaging')
dp = Transition(label='Delivery Plan')
psu = Transition(label='Post Support')

# Define the iterative feedback loop: Feedback Loop -> Quality Check -> Flight Calibrate -> Feedback Loop
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[fb, qc, fc]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    cb, dd, ps, cf, ca, su, it, feedback_loop,
    pm, st, cert, pack, dp, psu
])

# Define the control-flow dependencies
root.order.add_edge(cb, dd)
root.order.add_edge(dd, ps)
root.order.add_edge(ps, cf)
root.order.add_edge(cf, ca)
root.order.add_edge(ca, su)
root.order.add_edge(su, it)
root.order.add_edge(it, feedback_loop)
root.order.add_edge(feedback_loop, pm)
root.order.add_edge(pm, st)
root.order.add_edge(st, cert)
root.order.add_edge(cert, pack)
root.order.add_edge(pack, dp)
root.order.add_edge(dp, psu)