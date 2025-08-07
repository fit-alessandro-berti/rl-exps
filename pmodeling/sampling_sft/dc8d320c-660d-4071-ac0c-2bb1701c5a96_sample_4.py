import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake       = Transition(label='Artifact Intake')
prov         = Transition(label='Provenance Check')
mat          = Transition(label='Material Testing')
hist         = Transition(label='Historical Review')
expert       = Transition(label='Expert Interview')
cond         = Transition(label='Condition Audit')
digital      = Transition(label='Digital Catalog')
forgery      = Transition(label='Forgery Detection')
legal        = Transition(label='Legal Compliance')
restoration  = Transition(label='Restoration Plan')
valuation    = Transition(label='Valuation Report')
market       = Transition(label='Market Analysis')
final        = Transition(label='Final Approval')
sale         = Transition(label='Sale Preparation')
notify       = Transition(label='Client Notification')

# Loop for expert interview and forgery detection
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert, forgery])

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake, prov, mat, hist, expert_loop,
    digital, legal, restoration,
    valuation, market, final,
    sale, notify
])

# Sequential edges
root.order.add_edge(intake, prov)
root.order.add_edge(prov, mat)
root.order.add_edge(mat, hist)
root.order.add_edge(hist, expert_loop)
root.order.add_edge(expert_loop, digital)
root.order.add_edge(digital, legal)
root.order.add_edge(legal, restoration)
root.order.add_edge(restoration, valuation)
root.order.add_edge(valuation, market)
root.order.add_edge(market, final)
root.order.add_edge(final, sale)
root.order.add_edge(sale, notify)