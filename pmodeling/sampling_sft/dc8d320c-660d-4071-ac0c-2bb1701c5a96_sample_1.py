import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ai = Transition(label='Artifact Intake')
pc = Transition(label='Provenance Check')
mt = Transition(label='Material Testing')
hr = Transition(label='Historical Review')
ei = Transition(label='Expert Interview')
ca = Transition(label='Condition Audit')
dc = Transition(label='Forgery Detection')
lc = Transition(label='Legal Compliance')
drp = Transition(label='Digital Catalog')
vr = Transition(label='Valuation Report')
ma = Transition(label='Market Analysis')
rp = Transition(label='Restoration Plan')
fa = Transition(label='Final Approval')
sp = Transition(label='Sale Preparation')
cn = Transition(label='Client Notification')

# Build the verification loop: do Material Testing, then either exit or do Forgery Detection, Historical Review, Expert Interview, Condition Audit, Legal Compliance, and repeat
verification_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[mt,
              OperatorPOWL(
                  operator=Operator.XOR,
                  children=[dc, hr, ei, ca, lc]
              )
              ]
)

# Build the overall process as a partial order
root = StrictPartialOrder(nodes=[ai, verification_loop, drp, vr, ma, rp, fa, sp, cn])
root.order.add_edge(ai, verification_loop)
root.order.add_edge(verification_loop, drp)
root.order.add_edge(drp, vr)
root.order.add_edge(vr, ma)
root.order.add_edge(ma, rp)
root.order.add_edge(rp, fa)
root.order.add_edge(fa, sp)
root.order.add_edge(sp, cn)