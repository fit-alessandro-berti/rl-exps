import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Define the multi-stage testing partial order
test_po = StrictPartialOrder(nodes=[bt, si2, fs, st])
test_po.order.add_edge(bt, si2)
test_po.order.add_edge(si2, fs)
test_po.order.add_edge(fs, st)

# Define the loop for repeated compliance and quality checks
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[cc, qa])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    cb, dd, co, fb, pa, si, mm, test_po,
    am, si2, fs, st, loop,
    pd, dp
])

# Add dependencies
root.order.add_edge(cb, dd)
root.order.add_edge(dd, co)
root.order.add_edge(co, fb)
root.order.add_edge(fb, pa)
root.order.add_edge(pa, si)
root.order.add_edge(pa, mm)
root.order.add_edge(si, si2)
root.order.add_edge(mm, si2)
root.order.add_edge(si2, am)
root.order.add_edge(am, test_po)
root.order.add_edge(test_po, loop)
root.order.add_edge(loop, pd)
root.order.add_edge(pd, dp)