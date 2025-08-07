import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cb = Transition(label='Client Brief')
dd = Transition(label='Design Draft')
co = Transition(label='Component Order')
fb = Transition(label='Firmware Build')
pa = Transition(label='PCB Assembly')
si = Transition(label='Sensor Install')
mm = Transition(label='Motor Mount')
bt = Transition(label='Battery Test')
am = Transition(label='AI Module')
si2 = Transition(label='System Integrate')
fs = Transition(label='Flight Simulate')
st = Transition(label='Stress Test')
cc = Transition(label='Compliance Check')
qa = Transition(label='Quality Audit')
pd = Transition(label='Package Drone')
dp = Transition(label='Delivery Plan')

# Build the testing & compliance partial order
test_po = StrictPartialOrder(nodes=[bt, si, mm, st])
test_po.order.add_edge(bt, si)
test_po.order.add_edge(si, mm)
test_po.order.add_edge(mm, st)

compliance_po = StrictPartialOrder(nodes=[cc])
compliance_po.order.add_edge(fb, cc)

# Define the main assembly & testing loop
loop_body = StrictPartialOrder(nodes=[pa, si2, fs, test_po, compliance_po])
loop_body.order.add_edge(pa, si2)
loop_body.order.add_edge(si2, fs)
loop_body.order.add_edge(fs, test_po)
loop_body.order.add_edge(test_po, compliance_po)

# Loop: do Design Draft, then either exit or do the loop_body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[dd, loop_body])

# Assemble the overall process
root = StrictPartialOrder(nodes=[cb, loop, qa, pd, dp])
root.order.add_edge(cb, loop)
root.order.add_edge(loop, qa)
root.order.add_edge(qa, pd)
root.order.add_edge(pd, dp)