import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ra = Transition(label='Requirement Analysis')
cs = Transition(label='Component Sourcing')
qc = Transition(label='Quality Check')
fa = Transition(label='Frame Assembly')
mi = Transition(label='Motor Installation')
ss = Transition(label='Sensor Setup')
cu = Transition(label='Control Unit')
fu = Transition(label='Firmware Upload')
sc = Transition(label='System Calibration')
ft = Transition(label='Flight Testing')
ec = Transition(label='Error Correction')
cf = Transition(label='Cosmetic Finish')
pp = Transition(label='Packaging Prep')
um = Transition(label='User Manual')
ct = Transition(label='Client Training')
ss2 = Transition(label='Support Scheduling')

# Define the flight testing loop: Flight Testing -> Error Correction -> Flight Testing, repeated until exit
loop_body = StrictPartialOrder(nodes=[ft, ec])
loop_body.order.add_edge(ft, ec)
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ra, cs, qc, fa, mi, ss, cu, fu, sc, flight_loop, cf, pp, um, ct, ss2
])

# Sequential dependencies
root.order.add_edge(ra, cs)
root.order.add_edge(cs, qc)
root.order.add_edge(qc, fa)
root.order.add_edge(fa, mi)
root.order.add_edge(fa, ss)
root.order.add_edge(mi, cu)
root.order.add_edge(ss, cu)
root.order.add_edge(cu, fu)
root.order.add_edge(fu, sc)
root.order.add_edge(sc, flight_loop)
root.order.add_edge(flight_loop, cf)
root.order.add_edge(cf, pp)
root.order.add_edge(pp, um)
root.order.add_edge(um, ct)
root.order.add_edge(ct, ss2)