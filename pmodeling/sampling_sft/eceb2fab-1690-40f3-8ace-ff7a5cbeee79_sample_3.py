import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
cs = Transition(label='Condition Scan')
mt = Transition(label='Material Test')
ds = Transition(label='Disassembly')
sc = Transition(label='Surface Clean')
sr = Transition(label='Structural Repair')
rec = Transition(label='Reconstruction')
fm = Transition(label='Finish Match')
sp = Transition(label='Stabilize Parts')
doc = Transition(label='Documentation')
qa = Transition(label='Quality Audit')
val = Transition(label='Valuation')
ma = Transition(label='Market Analysis')
to = Transition(label='Target Outreach')
cp = Transition(label='Client Feedback')
dp = Transition(label='Delivery Prep')
skip = SilentTransition()

# Loop for iterative analysis and stabilization
loop_analysis = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cs, mt]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, loop_analysis, ds, sc, sr, rec, fm, sp,
    loop_analysis, qa, val, ma, to, cp, dp
])

# Define the control-flow dependencies
root.order.add_edge(pc, loop_analysis)
root.order.add_edge(loop_analysis, ds)
root.order.add_edge(ds, sc)
root.order.add_edge(sc, sr)
root.order.add_edge(sr, rec)
root.order.add_edge(rec, fm)
root.order.add_edge(fm, sp)
root.order.add_edge(sp, qa)
root.order.add_edge(qa, val)
root.order.add_edge(val, ma)
root.order.add_edge(ma, to)
root.order.add_edge(to, cp)
root.order.add_edge(cp, dp)

print(root)