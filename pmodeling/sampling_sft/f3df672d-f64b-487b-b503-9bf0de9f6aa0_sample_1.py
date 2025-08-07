import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
dc = Transition(label='Data Collection')
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
hr = Transition(label='Historical Review')
or_history = Transition(label='Oral History')
bp = Transition(label='Blockchain Verify')
er = Transition(label='Expert Panel')
cr = Transition(label='Condition Report')
lr = Transition(label='Legal Review')
cert = Transition(label='Certification')
au = Transition(label='Archival Update')
is_setup = Transition(label='Insurance Setup')
ep = Transition(label='Exhibition Prep')
im = Transition(label='IoT Monitoring')
rv = Transition(label='Re-validation')
skip = SilentTransition()

# Build the re-validation sub-process: re-validation then optionally skip back to IoT monitoring
reval_po = StrictPartialOrder(nodes=[rv, im])
reval_po.order.add_edge(rv, im)

# LOOP: perform initial data collection, then optionally do provenance check & material scan
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[dc, pc, ms])

# Exclusive choice: either do the expert panel or skip
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[er, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    loop1,
    hr,
    or_history,
    bp,
    expert_choice,
    cr,
    lr,
    cert,
    au,
    is_setup,
    ep,
    reval_po
])

# Define the control-flow dependencies
root.order.add_edge(dc, hr)
root.order.add_edge(dc, or_history)
root.order.add_edge(dc, bp)
root.order.add_edge(pc, expert_choice)
root.order.add_edge(ms, expert_choice)
root.order.add_edge(hr, expert_choice)
root.order.add_edge(or_history, expert_choice)
root.order.add_edge(bp, expert_choice)
root.order.add_edge(expert_choice, cr)
root.order.add_edge(hr, cr)
root.order.add_edge(or_history, cr)
root.order.add_edge(bp, cr)
root.order.add_edge(expert_choice, cr)
root.order.add_edge(cr, lr)
root.order.add_edge(lr, cert)
root.order.add_edge(cert, au)
root.order.add_edge(au, is_setup)
root.order.add_edge(is_setup, ep)
root.order.add_edge(ep, reval_po)
root.order.add_edge(reval_po, im)
root.order.add_edge(im, reval_po)