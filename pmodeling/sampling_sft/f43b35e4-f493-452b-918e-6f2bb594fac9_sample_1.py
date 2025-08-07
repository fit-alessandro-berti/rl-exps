import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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
psup = Transition(label='Post Support')

# Define the feedback loop: Feedback Loop -> Quality Check -> Feedback Loop
loop_body = StrictPartialOrder(nodes=[qc, fb])
loop_body.order.add_edge(qc, fb)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fb, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    cb, dd, ps, cf, ca, su,
    it, fc, pm, st, feedback_loop,
    cert, pack, dp, psup
])

# Define the control-flow dependencies
root.order.add_edge(cb, dd)
root.order.add_edge(dd, ps)
root.order.add_edge(ps, cf)
root.order.add_edge(cf, ca)
root.order.add_edge(ca, su)
root.order.add_edge(su, it)
root.order.add_edge(it, fc)
root.order.add_edge(fc, pm)
root.order.add_edge(pm, st)
root.order.add_edge(st, feedback_loop)
root.order.add_edge(feedback_loop, qc)
root.order.add_edge(qc, cert)
root.order.add_edge(cert, pack)
root.order.add_edge(pack, dp)
root.order.add_edge(dp, psup)