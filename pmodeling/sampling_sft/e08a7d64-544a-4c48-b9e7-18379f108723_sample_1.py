import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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
cs = Transition(label='Certification')
os = Transition(label='Owner Notify')
es = Transition(label='Exhibit Setup')
fa = Transition(label='Final Audit')

# Define the loop body: Insurance Quote -> Customs Clear -> Certification
loop_body = StrictPartialOrder(nodes=[iq, cc, cs])
loop_body.order.add_edge(iq, cc)
loop_body.order.add_edge(cc, cs)

# Loop operator: Risk Assess then either exit or execute the loop_body then Risk Assess again
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[ra, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[pc, mt, er, lv, risk_loop, ce, ds, cr, tp, cc, cs, os, es, fa])

# Sequential dependencies
root.order.add_edge(pc, mt)
root.order.add_edge(mt, er)
root.order.add_edge(er, lv)
root.order.add_edge(lv, risk_loop)
root.order.add_edge(risk_loop, ce)
root.order.add_edge(ce, ds)
root.order.add_edge(ds, cr)
root.order.add_edge(cr, tp)
root.order.add_edge(tp, cc)
root.order.add_edge(cc, cs)
root.order.add_edge(cs, os)
root.order.add_edge(os, es)
root.order.add_edge(es, fa)

# Final audit is concurrent with the final certification
root.order.add_edge(cs, fa)
root.order.add_edge(cs, fa)