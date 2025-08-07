import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
ac = Transition(label='AI Imaging')
sc = Transition(label='Style Compare')
ct = Transition(label='Chemical Test')
av = Transition(label='Aging Verify')
rm = Transition(label='Record Match')
dq = Transition(label='Database Query')
pr = Transition(label='Panel Review')
fr = Transition(label='Forgery Risk')
mv = Transition(label='Market Value')
rd = Transition(label='Report Draft')
cs = Transition(label='Certification')
as1 = Transition(label='Approval Stage')
sp = Transition(label='Secure Packing')
tp = Transition(label='Transport Prep')

# Loop for continuous database querying and record matching
loop_query = OperatorPOWL(operator=Operator.LOOP, children=[dq, rm])

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, ms, ac, sc,
    ct, av, loop_query,
    pr, fr, mv,
    rd, cs, as1,
    sp, tp
])

# Sequence edges
root.order.add_edge(pc, ms)
root.order.add_edge(ms, ac)
root.order.add_edge(ms, sc)

# Material analysis branches
root.order.add_edge(ac, ct)
root.order.add_edge(sc, ct)

# All subsequent activities depend on chemical test result
root.order.add_edge(ct, av)
root.order.add_edge(ct, loop_query)

# Loop edge (Aging Verify -> loop_query)
root.order.add_edge(av, loop_query)

# Loop edges (loop_query -> Panel Review)
root.order.add_edge(loop_query, pr)

# Parallel edges from Panel Review to Forgeries Risk and Market Value
root.order.add_edge(pr, fr)
root.order.add_edge(pr, mv)

# All outputs of Panel Review branch into Report Draft
root.order.add_edge(fr, rd)
root.order.add_edge(mv, rd)

# Report Draft then goes to Certification and Approval Stage
root.order.add_edge(rd, cs)
root.order.add_edge(rd, as1)

# Final approval stages (Certification and Approval Stage) are parallel
root.order.add_edge(cs, as1)

# Approval Stage then Secure Packing
root.order.add_edge(as1, sp)

# Secure Packing then Transport Prep
root.order.add_edge(sp, tp)