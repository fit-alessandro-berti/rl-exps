import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Milk Selection')
qt = Transition(label='Quality Testing')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Cheese Crafting')
ca = Transition(label='Controlled Aging')
sr = Transition(label='Sensory Review')
cp = Transition(label='Custom Packaging')
lp = Transition(label='Label Printing')
ep = Transition(label='Export Licensing')
dp = Transition(label='Documentation Prep')
cc_clear = Transition(label='Customs Clearance')
cs = Transition(label='Cold Shipping')
dt = Transition(label='Delivery Tracking')
fr = Transition(label='Feedback Review')
ma = Transition(label='Market Analysis')

# Define the loop body: sensory review -> custom packaging -> label printing
loop_body = StrictPartialOrder(nodes=[sr, cp, lp])
loop_body.order.add_edge(sr, cp)
loop_body.order.add_edge(cp, lp)

# Define the export & shipping loop: export licensing -> documentation prep -> customs clearance -> cold shipping
export_loop = StrictPartialOrder(nodes=[ep, dp, cc_clear, cs])
export_loop.order.add_edge(ep, dp)
export_loop.order.add_edge(dp, cc_clear)
export_loop.order.add_edge(cc_clear, cs)

# Define the overall export & shipping loop: do export_loop once, then optionally repeat loop_body then export_loop again
loop = OperatorPOWL(operator=Operator.LOOP, children=[export_loop, loop_body])

# Assemble the complete workflow
root = StrictPartialOrder(nodes=[ms, qt, mp, cc, ca, loop, dt, fr, ma])
root.order.add_edge(ms, qt)
root.order.add_edge(qt, mp)
root.order.add_edge(mp, cc)
root.order.add_edge(cc, ca)
root.order.add_edge(ca, loop)
root.order.add_edge(loop, dt)
root.order.add_edge(dt, fr)
root.order.add_edge(fr, ma)