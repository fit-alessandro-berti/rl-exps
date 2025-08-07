import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
cs = Transition(label='Component Sourcing')
fb = Transition(label='Client Feedback')
fr = Transition(label='Frame Build')
ma = Transition(label='Motor Assembly')
sb = Transition(label='Signal Test')
si = Transition(label='Software Install')
at = Transition(label='Algorithm Tune')
bi = Transition(label='Battery Integrate')
qc = Transition(label='Quality Inspect')
dc = Transition(label='Durability Check')
fs = Transition(label='Flight Simulate')
cp = Transition(label='Packaging Prep')
lp = Transition(label='Logistics Plan')

# Build the calibration sub-process: Sensor Calibrate -> Signal Test
calibration = StrictPartialOrder(nodes=[fb, sb])
calibration.order.add_edge(fb, sb)

# Build the quality assurance sub-process: Durability Check -> Flight Simulate
qa = StrictPartialOrder(nodes=[dc, fs])
qa.order.add_edge(dc, fs)

# Build the final assembly sub-process: Software Install -> Algorithm Tune -> Battery Integrate -> Quality Inspect -> Durability Check
final_assembly = StrictPartialOrder(nodes=[si, at, bi, qc, dc])
final_assembly.order.add_edge(si, at)
final_assembly.order.add_edge(at, bi)
final_assembly.order.add_edge(bi, qc)
final_assembly.order.add_edge(qc, dc)

# Build the loop for iterative compliance review and feedback
loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_review, feedback])

# Assemble the top‐level process
root = StrictPartialOrder(nodes=[
    cs, fr, ma, calibration, final_assembly, loop, cp, lp
])

# Define the control‐flow dependencies
root.order.add_edge(cs, fr)
root.order.add_edge(fr, ma)
root.order.add_edge(ma, calibration)
root.order.add_edge(calibration, final_assembly)
root.order.add_edge(final_assembly, loop)
root.order.add_edge(loop, cp)
root.order.add_edge(cp, lp)