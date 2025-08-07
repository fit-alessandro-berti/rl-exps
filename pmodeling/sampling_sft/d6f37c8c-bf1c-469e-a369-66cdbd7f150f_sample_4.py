import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
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

# Define the multi-stage testing as a partial order
testing = StrictPartialOrder(nodes=[bt, si2, fs, st])
testing.order.add_edge(bt, si2)
testing.order.add_edge(si2, fs)
testing.order.add_edge(fs, st)

# Define the main process as a strict partial order
root = StrictPartialOrder(nodes=[cb, dd, co, fb, pa, si, mm, testing, cc, qa, pd, dp])
root.order.add_edge(cb, dd)
root.order.add_edge(dd, co)
root.order.add_edge(co, fb)
root.order.add_edge(fb, pa)
root.order.add_edge(pa, si)
root.order.add_edge(pa, mm)
root.order.add_edge(si, testing)
root.order.add_edge(mm, testing)
root.order.add_edge(testing, cc)
root.order.add_edge(cc, qa)
root.order.add_edge(qa, pd)
root.order.add_edge(pd, dp)