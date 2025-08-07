import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
dc = Transition(label='Data Capture')
df = Transition(label='Demand Forecast')
ic = Transition(label='Inventory Check')
quant = Transition(label='Quantum Calc')
rp = Transition(label='Route Update')
sp = Transition(label='Shipment Plan')
ss = Transition(label='Supplier Sync')
cm = Transition(label='Contract Mod')
bv = Transition(label='Blockchain Verify')
ra = Transition(label='Risk Assess')
ssim = Transition(label='Scenario Sim')
fl = Transition(label='Feedback Loop')
ai = Transition(label='AI Adjust')
wa = Transition(label='Waste Audit')
rg = Transition(label='Report Generate')
sa = Transition(label='Stakeholder Alert')
cr = Transition(label='Compliance Review')

# Define the loop body for AI-adjusted scenario simulation
body = StrictPartialOrder(nodes=[ra, ssim, ai, wa, rg, sa])
body.order.add_edge(ra, ssim)
body.order.add_edge(ssim, ai)
body.order.add_edge(ai, wa)
body.order.add_edge(ai, rg)
body.order.add_edge(wa, rg)
body.order.add_edge(rg, sa)

# Define the loop: do Data Capture, then either exit or do the loop body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[dc, body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    loop,
    df, ic, quant,
    rp, sp,
    ss, cm,
    bv,
    cr
])

# Define the control-flow dependencies
root.order.add_edge(loop, df)
root.order.add_edge(df, ic)
root.order.add_edge(df, quant)
root.order.add_edge(ic, rp)
root.order.add_edge(ic, sp)
root.order.add_edge(quant, rp)
root.order.add_edge(quant, sp)
root.order.add_edge(rp, ss)
root.order.add_edge(rp, cm)
root.order.add_edge(sp, ss)
root.order.add_edge(sp, cm)
root.order.add_edge(ss, bv)
root.order.add_edge(cm, bv)
root.order.add_edge(bv, cr)
root.order.add_edge(cr, sa)