import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ia   = Transition(label='Initial Assess')
dc   = Transition(label='Disassemble Parts')
uc   = Transition(label='Ultrasonic Clean')
ic   = Transition(label='Inspect Components')
fg   = Transition(label='Fabricate Gears')
dr   = Transition(label='Dial Restoration')
rm   = Transition(label='Repaint Markers')
rmov = Transition(label='Reassemble Movement')
lb   = Transition(label='Lubricate Bearings')
ct   = Transition(label='Calibrate Timing')
pc   = Transition(label='Polish Case')
rc   = Transition(label='Re-case Watch')
qt   = Transition(label='Quality Testing')
dp   = Transition(label='Document Process')
pk   = Transition(label='Package Product')

# Build the repair body: components -> restoration -> assembly -> calibration -> polishing -> re-casing -> testing
body = StrictPartialOrder(nodes=[ic, fg, dr, rm, rmov, lb, ct, pc, rc, qt])
body.order.add_edge(ic, fg)
body.order.add_edge(ic, dr)
body.order.add_edge(ic, rm)
body.order.add_edge(fg, rmov)
body.order.add_edge(dr, rmov)
body.order.add_edge(rmov, lb)
body.order.add_edge(lb, ct)
body.order.add_edge(ct, pc)
body.order.add_edge(pc, rc)
body.order.add_edge(rc, qt)

# Define the loop: do Initial Assess, then optionally do the repair body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[ia, body])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[loop, dp, pk])
root.order.add_edge(loop, dp)
root.order.add_edge(loop, pk)