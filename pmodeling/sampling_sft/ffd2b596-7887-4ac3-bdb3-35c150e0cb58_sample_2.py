import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cs = Transition(label='Component Sourcing')
fb = Transition(label='Client Feedback')
fb_loop = Transition(label='Feedback Loop')  # For continuous feedback integration
fb_skip = SilentTransition()
fb_xor = OperatorPOWL(operator=Operator.XOR, children=[fb, fb_skip])
fb_seq = StrictPartialOrder(nodes=[fb_loop, fb_xor])
fb_seq.order.add_edge(fb_loop, fb_xor)

fb_loop.order.add_edge(fb_xor, fb_loop)  # Loop back to start after each feedback iteration

cb = Transition(label='Component Build')
ma = Transition(label='Motor Assembly')
sb = Transition(label='Sensor Calibrate')
mb = Transition(label='Frame Build')
bi = Transition(label='Battery Integrate')
si = Transition(label='Software Install')
at = Transition(label='Algorithm Tune')
st = Transition(label='Signal Test')
qc = Transition(label='Quality Inspect')
dc = Transition(label='Durability Check')
fs = Transition(label='Flight Simulate')
cr = Transition(label='Compliance Review')
pp = Transition(label='Packaging Prep')
lp = Transition(label='Logistics Plan')

# Build the partial order
root = StrictPartialOrder(nodes=[
    cs, fb_loop,
    cb, ma, sb, mb,
    bi, si, at, st, qc, dc,
    fs, cr,
    pp, lp
])

# Define the control-flow dependencies
root.order.add_edge(cs, cb)
root.order.add_edge(cb, ma)
root.order.add_edge(cb, sb)
root.order.add_edge(cb, mb)
root.order.add_edge(ma, bi)
root.order.add_edge(sb, bi)
root.order.add_edge(mb, bi)
root.order.add_edge(bi, si)
root.order.add_edge(si, at)
root.order.add_edge(at, st)
root.order.add_edge(st, qc)
root.order.add_edge(qc, dc)
root.order.add_edge(dc, fs)
root.order.add_edge(fs, cr)
root.order.add_edge(cr, pp)
root.order.add_edge(pp, lp)

# Add the feedback loop at the end
root.order.add_edge(lp, fb_loop)