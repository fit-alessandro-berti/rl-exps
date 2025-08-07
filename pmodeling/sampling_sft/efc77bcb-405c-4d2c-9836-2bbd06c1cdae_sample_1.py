import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
dc = Transition(label='Data Capture')
df = Transition(label='Demand Forecast')
ic = Transition(label='Inventory Check')
ru = Transition(label='Route Update')
sp = Transition(label='Shipment Plan')
ss = Transition(label='Supplier Sync')
cm = Transition(label='Contract Mod')
bv = Transition(label='Blockchain Verify')
ra = Transition(label='Risk Assess')
ssim = Transition(label='Scenario Sim')
fl = Transition(label='Feedback Loop')
ia = Transition(label='AI Adjust')
wa = Transition(label='Waste Audit')
rg = Transition(label='Report Generate')
sa = Transition(label='Stakeholder Alert')
cr = Transition(label='Compliance Review')

# Build the loop body: Risk Assess -> Scenario Sim -> Feedback Loop -> AI Adjust
loop_body = StrictPartialOrder(nodes=[ra, ssim, fl, ia])
loop_body.order.add_edge(ra, ssim)
loop_body.order.add_edge(ssim, fl)
loop_body.order.add_edge(fl, ia)

# LOOP: do Risk Assess, then repeatedly do Scenario Sim, Feedback Loop, AI Adjust
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[ra, loop_body])

# Build the main workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    dc, df, ic, ru, sp, ss, cm, bv, risk_loop, wa, rg, sa, cr
])

# Add the control-flow edges
root.order.add_edge(dc, df)
root.order.add_edge(dc, ic)
root.order.add_edge(df, ru)
root.order.add_edge(ic, ru)
root.order.add_edge(ru, sp)
root.order.add_edge(sp, ss)
root.order.add_edge(ss, cm)
root.order.add_edge(cm, bv)
root.order.add_edge(bv, risk_loop)
root.order.add_edge(risk_loop, wa)
root.order.add_edge(wa, rg)
root.order.add_edge(rg, sa)
root.order.add_edge(sa, cr)

# Print the root model (optional)
print(root)