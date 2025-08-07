import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
cs = Transition(label='Collection Survey')
pc = Transition(label='Provenance Check')
lr = Transition(label='Legal Review')
st = Transition(label='Scientific Test')
ma = Transition(label='Material Analysis')
oa = Transition(label='Ownership Audit')
es = Transition(label='Ethical Screening')
cr = Transition(label='Condition Report')
ec = Transition(label='Expert Consultation')
tp = Transition(label='Transport Planning')
sp = Transition(label='Secure Packing')
cc = Transition(label='Customs Clearance')
iu = Transition(label='Insurance Setup')
ap = Transition(label='Final Approval')
ep = Transition(label='Exhibit Preparation')

# Define the choice for legal or ethical review
legal_xor = OperatorPOWL(operator=Operator.XOR, children=[lr, es])

# Define the loop for iterative scientific testing
# A: scientific test, B: material analysis
loop = OperatorPOWL(operator=Operator.LOOP, children=[st, ma])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    cs, pc, legal_xor,
    loop, cr, ec,
    tp, sp, cc, iu,
    ap, ep
])

# Define the control-flow dependencies
root.order.add_edge(cs, pc)
root.order.add_edge(pc, legal_xor)
root.order.add_edge(legal_xor, loop)
root.order.add_edge(loop, cr)
root.order.add_edge(cr, ec)
root.order.add_edge(ec, tp)
root.order.add_edge(tp, sp)
root.order.add_edge(sp, cc)
root.order.add_edge(cc, iu)
root.order.add_edge(iu, ap)
root.order.add_edge(ap, ep)