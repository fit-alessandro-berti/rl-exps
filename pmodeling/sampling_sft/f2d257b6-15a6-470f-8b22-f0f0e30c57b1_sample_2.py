import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
ms = Transition(label='Material Sampling')
rc = Transition(label='Radiocarbon Test')
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

# Material sampling branch: Radiocarbon Test -> Chemical Analysis -> Historical Match
sampling_po = StrictPartialOrder(nodes=[rc, ca, hm])
sampling_po.order.add_edge(rc, ca)
sampling_po.order.add_edge(ca, hm)

# Main process partial order
main_po = StrictPartialOrder(nodes=[
    ai, cc, ms, sampling_po,
    fs, ec, pr, im,
    msurvey, ve, cert, da, fs2
])
main_po.order.add_edge(ai, cc)
main_po.order.add_edge(cc, ms)
main_po.order.add_edge(ms, sampling_po)
main_po.order.add_edge(sampling_po, fs)
main_po.order.add_edge(fs, ec)
main_po.order.add_edge(ec, pr)
main_po.order.add_edge(pr, im)
main_po.order.add_edge(im, msurvey)
main_po.order.add_edge(msurvey, ve)
main_po.order.add_edge(ve, cert)
main_po.order.add_edge(cert, da)
main_po.order.add_edge(da, fs2)

# Final loop: loop over (Forgery Scan, Market Survey) until exit
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[fs, msurvey])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    ai, cc, ms, sampling_po,
    fs, ec, pr, im,
    loop, ve, cert, da, fs2
])
root.order.add_edge(ai, cc)
root.order.add_edge(cc, ms)
root.order.add_edge(ms, sampling_po)
root.order.add_edge(sampling_po, fs)
root.order.add_edge(fs, ec)
root.order.add_edge(ec, pr)
root.order.add_edge(pr, im)
root.order.add_edge(im, loop)
root.order.add_edge(loop, ve)
root.order.add_edge(ve, cert)
root.order.add_edge(cert, da)
root.order.add_edge(da, fs2)