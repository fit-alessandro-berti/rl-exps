import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
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
fl = Transition(label='Feedback Loop')
qc = Transition(label='Quality Check')
cert = Transition(label='Certification')
pkg = Transition(label='Packaging')
dp = Transition(label='Delivery Plan')
psup = Transition(label='Post Support')

# Build the iterative calibration loop: Feedback Loop -> Flight Calibrate
cal_loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, fc])

# Build the main assembly pipeline
main_seq = StrictPartialOrder(nodes=[
    cb, dd, ps, cf, ca, su,
    it, cal_loop,
    pm, st, qc, cert,
    pkg, dp, psup
])
main_seq.order.add_edge(cb, dd)
main_seq.order.add_edge(dd, ps)
main_seq.order.add_edge(ps, cf)
main_seq.order.add_edge(cf, ca)
main_seq.order.add_edge(ca, su)
main_seq.order.add_edge(su, it)
main_seq.order.add_edge(it, cal_loop)
main_seq.order.add_edge(cal_loop, pm)
main_seq.order.add_edge(pm, st)
main_seq.order.add_edge(st, qc)
main_seq.order.add_edge(qc, cert)
main_seq.order.add_edge(cert, pkg)
main_seq.order.add_edge(pkg, dp)
main_seq.order.add_edge(dp, psup)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[cb])
root.order.add_edge(cb, dd)
root.order.add_edge(dd, ps)
root.order.add_edge(ps, cf)
root.order.add_edge(cf, ca)
root.order.add_edge(ca, su)
root.order.add_edge(su, it)
root.order.add_edge(it, cal_loop)
root.order.add_edge(cal_loop, pm)
root.order.add_edge(pm, st)
root.order.add_edge(st, qc)
root.order.add_edge(qc, cert)
root.order.add_edge(cert, pkg)
root.order.add_edge(pkg, dp)
root.order.add_edge(dp, psup)