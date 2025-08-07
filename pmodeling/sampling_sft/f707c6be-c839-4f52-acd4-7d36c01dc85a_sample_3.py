import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
ms = Transition(label='Multi-spectral Scan')
mt = Transition(label='Material Test')
dm = Transition(label='Database Match')
pc = Transition(label='Provenance Check')
er = Transition(label='Expert Review')
hq = Transition(label='Historical Query')
lc = Transition(label='Lab Collaboration')
ia = Transition(label='Imaging Analysis')
fd = Transition(label='Forgery Detection')
ld = Transition(label='Legal Drafting')
ci = Transition(label='Certification Issue')
cb = Transition(label='Client Briefing')
au = Transition(label='Archival Update')

# Loop for continuous imaging analysis and forgery detection
loop_analysis = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ia, fd]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    ai, cc, ms, mt, dm, pc, er, hq, lc, loop_analysis, ld, ci, cb, au
])

# Sequential flow
root.order.add_edge(ai, cc)
root.order.add_edge(cc, ms)
root.order.add_edge(cc, mt)
root.order.add_edge(ms, dm)
root.order.add_edge(mt, dm)
root.order.add_edge(dm, pc)
root.order.add_edge(pc, er)
root.order.add_edge(er, hq)
root.order.add_edge(hq, lc)
root.order.add_edge(lc, loop_analysis)

# Concurrency after analysis loop
root.order.add_edge(loop_analysis, ld)
root.order.add_edge(loop_analysis, ci)
root.order.add_edge(loop_analysis, cb)
root.order.add_edge(ld, ci)
root.order.add_edge(ld, cb)
root.order.add_edge(ci, au)
root.order.add_edge(cb, au)