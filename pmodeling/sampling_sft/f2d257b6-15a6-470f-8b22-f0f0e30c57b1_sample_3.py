import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
ms = Transition(label='Material Sampling')
rt = Transition(label='Radiocarbon Test')
pr = Transition(label='Provenance Review')
ic = Transition(label='Imaging Capture')
ca = Transition(label='Chemical Analysis')
hm = Transition(label='Historical Match')
ec = Transition(label='Expert Consult')
fs = Transition(label='Forgery Scan')
msurvey = Transition(label='Market Survey')
ve = Transition(label='Value Estimate')
cert = Transition(label='Certification')
da = Transition(label='Digital Archive')
fs2 = Transition(label='Final Storage')

# Loop for expert consultation: do Expert Consult, then either exit or repeat
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ec, OperatorPOWL(operator=Operator.XOR, children=[skip, ec]))
    
# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ai, cc, ms, rt,
    pr, ic, ca, hm,
    expert_loop,
    fs, msurvey, ve,
    cert, da, fs2
])

# Define the control-flow dependencies
root.order.add_edge(ai, cc)
root.order.add_edge(cc, ms)
root.order.add_edge(ms, rt)
root.order.add_edge(pr, ic)
root.order.add_edge(pr, ca)
root.order.add_edge(pr, hm)
root.order.add_edge(ic, expert_loop)
root.order.add_edge(ca, expert_loop)
root.order.add_edge(hm, expert_loop)
root.order.add_edge(expert_loop, fs)
root.order.add_edge(fs, msurvey)
root.order.add_edge(msurvey, ve)
root.order.add_edge(ve, cert)
root.order.add_edge(cert, da)
root.order.add_edge(da, fs2)