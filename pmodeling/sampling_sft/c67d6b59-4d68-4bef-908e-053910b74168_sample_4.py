import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
cm = Transition(label='Client Meet')
dd = Transition(label='Design Draft')
vs = Transition(label='Vendor Select')
co = Transition(label='Component Order')
pi = Transition(label='Parts Inspect')
fb = Transition(label='Feedback Review')
ad = Transition(label='Adjust Design')
sb = Transition(label='Frame Build')
ws = Transition(label='Wiring Setup')
sl = Transition(label='Software Load')
fs = Transition(label='Flight Sim')
qt = Transition(label='Quality Test')
cc = Transition(label='Compliance Check')
pp = Transition(label='Packaging Prep')
fd = Transition(label='Final Demo')
sd = Transition(label='Ship Drone')

# Build the assembly sequence as a partial order
assembly = StrictPartialOrder(nodes=[
    dd, vs, co, pi, fb, ad,
    sb, ws, sl, fs, qt, cc, pp, fd, sd
])
assembly.order.add_edge(dd, vs)
assembly.order.add_edge(vs, co)
assembly.order.add_edge(co, pi)
assembly.order.add_edge(pi, fb)
assembly.order.add_edge(fb, ad)
assembly.order.add_edge(ad, sb)
assembly.order.add_edge(sb, ws)
assembly.order.add_edge(ws, sl)
assembly.order.add_edge(sl, fs)
assembly.order.add_edge(fs, qt)
assembly.order.add_edge(qt, cc)
assembly.order.add_edge(cc, pp)
assembly.order.add_edge(pp, fd)
assembly.order.add_edge(fd, sd)

# Define the overall process as a loop: Client Meet, then repeatedly do the assembly sequence until ship drone
root = OperatorPOWL(operator=Operator.LOOP, children=[cm, assembly])