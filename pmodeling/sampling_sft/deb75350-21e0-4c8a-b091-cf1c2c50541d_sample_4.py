import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ir = Transition(label='Intake Review')
vi = Transition(label='Visual Inspect')
mt = Transition(label='Material Test')
pc = Transition(label='Provenance Check')
asrch = Transition(label='Archival Search')
ec = Transition(label='Expert Consult')
ds = Transition(label='Digital Scan')
cr = Transition(label='Condition Report')
fa = Transition(label='Forgery Assess')
lr = Transition(label='Legal Review')
ra = Transition(label='Risk Analysis')
av = Transition(label='Acquisition Vote')
ce = Transition(label='Catalog Entry')
sp = Transition(label='Storage Prep')
fa2 = Transition(label='Final Approval')

# Build the loop body for analysis tasks
body_analysis = StrictPartialOrder(nodes=[mt, pc, asrch, ec, ds, cr, fa, lr, ra])
body_analysis.order.add_edge(mt, pc)
body_analysis.order.add_edge(pc, asrch)
body_analysis.order.add_edge(asrch, ec)
body_analysis.order.add_edge(ec, ds)
body_analysis.order.add_edge(ds, cr)
body_analysis.order.add_edge(ds, fa)
body_analysis.order.add_edge(fa, lr)
body_analysis.order.add_edge(lr, ra)

# Build the loop for iterative analysis
loop_analysis = OperatorPOWL(operator=Operator.LOOP, children=[body_analysis, body_analysis])

# Build the main workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    ir,
    vi,
    loop_analysis,
    av,
    ce,
    sp,
    fa2
])

# Define the control-flow dependencies
root.order.add_edge(ir, vi)
root.order.add_edge(vi, loop_analysis)
root.order.add_edge(loop_analysis, av)
root.order.add_edge(av, ce)
root.order.add_edge(ce, sp)
root.order.add_edge(sp, fa2)