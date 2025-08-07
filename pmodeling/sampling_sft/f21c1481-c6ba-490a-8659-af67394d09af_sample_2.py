import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
cs = Transition(label='Collection Survey')
pc = Transition(label='Provenance Check')
lr = Transition(label='Legal Review')
sa = Transition(label='Scientific Test')
ma = Transition(label='Material Analysis')
oa = Transition(label='Ownership Audit')
es = Transition(label='Ethical Screening')
cr = Transition(label='Condition Report')
ec = Transition(label='Expert Consultation')
tp = Transition(label='Transport Planning')
sp = Transition(label='Secure Packing')
cc = Transition(label='Customs Clearance')
iu = Transition(label='Insurance Setup')
ep = Transition(label='Exhibit Preparation')
fa = Transition(label='Final Approval')

# Build the loop for scientific testing
# A = do a scientific test, then optionally do material analysis
loop_science = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sa, ma]
)

# Build the loop for expert consultation
# B = do an expert consultation, then optionally consult again
loop_expert = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ec, ec]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    cs, pc, lr, loop_science,
    oa, es,
    cr, loop_expert,
    tp, sp, cc, iu, ep, fa
])

# Define the control-flow dependencies
root.order.add_edge(cs, pc)
root.order.add_edge(pc, lr)
root.order.add_edge(lr, loop_science)
root.order.add_edge(loop_science, oa)
root.order.add_edge(oa, es)
root.order.add_edge(es, cr)
root.order.add_edge(cr, loop_expert)
root.order.add_edge(loop_expert, tp)
root.order.add_edge(tp, sp)
root.order.add_edge(sp, cc)
root.order.add_edge(cc, iu)
root.order.add_edge(iu, ep)
root.order.add_edge(ep, fa)