import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
mt = Transition(label='Material Testing')
er = Transition(label='Expert Review')
lv = Transition(label='Legal Verify')
ra = Transition(label='Risk Assess')
iq = Transition(label='Insurance Quote')
ce = Transition(label='Catalog Entry')
ds = Transition(label='Digital Scan')
cr = Transition(label='Condition Report')
tp = Transition(label='Transport Plan')
cc = Transition(label='Customs Clear')
cert = Transition(label='Certification')
os = Transition(label='Owner Notify')
ex = Transition(label='Exhibit Setup')
fa = Transition(label='Final Audit')

# Loop for iterative risk assessment, insurance quote, and condition report
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[ra, iq, cr])

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, mt, er, lv,
    risk_loop,
    ce, ds,
    tp, cc,
    cert, os, ex, fa
])

# Define the control-flow dependencies
root.order.add_edge(pc, mt)
root.order.add_edge(pc, er)
root.order.add_edge(pc, lv)

root.order.add_edge(mt, er)
root.order.add_edge(mt, lv)

root.order.add_edge(er, lv)

root.order.add_edge(mt, risk_loop)

root.order.add_edge(risk_loop, ce)
root.order.add_edge(risk_loop, ds)

root.order.add_edge(ce, dp)
root.order.add_edge(ds, dp)

root.order.add_edge(dp, tp)
root.order.add_edge(dp, cc)

root.order.add_edge(tp, cert)
root.order.add_edge(cc, cert)

root.order.add_edge(cert, os)
root.order.add_edge(cert, ex)

root.order.add_edge(os, fa)
root.order.add_edge(ex, fa)