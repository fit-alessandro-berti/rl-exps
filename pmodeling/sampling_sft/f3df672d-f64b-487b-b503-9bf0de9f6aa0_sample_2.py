import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
dc = Transition(label='Data Collection')
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
hr = Transition(label='Historical Review')
ep = Transition(label='Expert Panel')
bv = Transition(label='Blockchain Verify')
oh = Transition(label='Oral History')
cr = Transition(label='Condition Report')
lr = Transition(label='Legal Review')
cert = Transition(label='Certification')
au = Transition(label='Archival Update')
isup = Transition(label='Insurance Setup')
eprep = Transition(label='Exhibition Prep')
im = Transition(label='IoT Monitoring')
rv = Transition(label='Re-validation')

# Build the loop body: IoT Monitoring then Re-validation
body = StrictPartialOrder(nodes=[im, rv])
body.order.add_edge(im, rv)

# LOOP: repeat IoT Monitoring then Re-validation until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, body])

# Build the exclusive choice for legal review (either Blockchain Verify or Oral History)
xor_legal = OperatorPOWL(operator=Operator.XOR, children=[bv, oh])

# Build the exclusive choice for archival update (either Blockchain Verify or Oral History)
xor_archive = OperatorPOWL(operator=operator=Operator.XOR, children=[bv, oh])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    dc, pc, ms, hr, ep, xor_legal, cr, lr, cert, au, isup, eprep, loop, xor_archive
])

# Define the control-flow dependencies
root.order.add_edge(dc, pc)
root.order.add_edge(pc, ms)
root.order.add_edge(ms, hr)
root.order.add_edge(hr, ep)
root.order.add_edge(ep, xor_legal)
root.order.add_edge(xor_legal, cr)
root.order.add_edge(cr, lr)
root.order.add_edge(lr, cert)
root.order.add_edge(cert, isup)
root.order.add_edge(isup, eprep)
root.order.add_edge(eprep, loop)
root.order.add_edge(loop, xor_archive)
root.order.add_edge(xor_archive, au)