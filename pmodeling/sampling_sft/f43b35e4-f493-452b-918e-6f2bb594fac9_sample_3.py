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
fl = Transition(label='Feedback Loop')
qc = Transition(label='Quality Check')
cert = Transition(label='Certification')
pk = Transition(label='Packaging')
dp = Transition(label='Delivery Plan')
psup = Transition(label='Post Support')

# Loop for iterative feedback and software calibration
loop_software = OperatorPOWL(
    operator=Operator.LOOP,
    children=[fc, fl]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    cb, dd, ps, cf, ca, su,
    it, loop_software,
    pm, st, qc, cert, pk, dp, psup
])

# Define the control-flow dependencies
root.order.add_edge(cb, dd)
root.order.add_edge(dd, ps)
root.order.add_edge(ps, cf)
root.order.add_edge(cf, ca)
root.order.add_edge(ca, su)
root.order.add_edge(su, it)
root.order.add_edge(it, loop_software)
root.order.add_edge(loop_software, pm)
root.order.add_edge(pm, st)
root.order.add_edge(st, qc)
root.order.add_edge(qc, cert)
root.order.add_edge(cert, pk)
root.order.add_edge(pk, dp)
root.order.add_edge(dp, psup)

# Print the root model for verification
print(root)