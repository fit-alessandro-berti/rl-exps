import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
cs = Transition(label='Component Sourcing')
fa = Transition(label='Frame Assembly')
mi = Transition(label='Motor Installation')
sm = Transition(label='Sensor Mounting')
ws = Transition(label='Wiring Setup')
fw = Transition(label='Firmware Upload')
ai = Transition(label='AI Module')
cal = Transition(label='Calibration Phase')
st = Transition(label='Stress Testing')
fs = Transition(label='Flight Simulation')
pa = Transition(label='Pattern Adjustment')
qi = Transition(label='Quality Inspect')
cc = Transition(label='Compliance Check')
pf = Transition(label='Packaging Final')
ds = Transition(label='Delivery Setup')

# Define the iterative flight pattern adjustment loop:
# A = Flight Simulation -> Pattern Adjustment
# B = repeat
loop_body = StrictPartialOrder(nodes=[fs, pa])
loop_body.order.add_edge(fs, pa)

# Loop: do A, then optionally do B and repeat
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    cs, fa, mi, sm, ws, fw, ai,
    cal, st, flight_loop,
    qi, cc, pf, ds
])

# Sequential dependencies
root.order.add_edge(cs, fa)
root.order.add_edge(fa, mi)
root.order.add_edge(fa, sm)
root.order.add_edge(fa, ws)
root.order.add_edge(mi, fw)
root.order.add_edge(sm, fw)
root.order.add_edge(ws, fw)
root.order.add_edge(fw, ai)
root.order.add_edge(ai, cal)
root.order.add_edge(cal, st)
root.order.add_edge(st, flight_loop)
root.order.add_edge(flight_loop, qi)
root.order.add_edge(qi, cc)
root.order.add_edge(cc, pf)
root.order.add_edge(pf, ds)