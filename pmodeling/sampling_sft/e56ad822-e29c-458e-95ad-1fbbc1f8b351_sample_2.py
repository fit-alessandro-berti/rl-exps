import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
submit = Transition(label='Submit Artifact')
initial = Transition(label='Initial Review')
prov = Transition(label='Provenance Check')
mat_scan = Transition(label='Material Scan')
context = Transition(label='Context Analysis')
expert = Transition(label='Expert Panel')
ai_pattern = Transition(label='AI Pattern')
digital = Transition(label='Digital Fingerprint')
legal = Transition(label='Legal Audit')
ethics = Transition(label='Ethics Review')
fraud = Transition(label='Fraud Detection')
blockchain = Transition(label='Blockchain Log')
certify = Transition(label='Certification')
notify = Transition(label='Owner Notify')
archive = Transition(label='Archive Data')
storage = Transition(label='Secure Storage')

# Build the loop body for continuous AI-pattern and blockchain logging
body = StrictPartialOrder(nodes=[ai_pattern, blockchain])
body.order.add_edge(ai_pattern, blockchain)

# Loop: do Initial Review, then optionally do Provenance Check -> Material Scan -> Context Analysis
# followed by Expert Panel, then the loop body (AI-pattern & blockchain), and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[initial, body])

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    submit,
    loop,
    prov,
    mat_scan,
    context,
    expert,
    digital,
    legal,
    ethics,
    fraud,
    certify,
    notify,
    archive,
    storage
])

# Define the control-flow edges
root.order.add_edge(submit, loop)
root.order.add_edge(loop, prov)
root.order.add_edge(prov, mat_scan)
root.order.add_edge(mat_scan, context)
root.order.add_edge(context, expert)
root.order.add_edge(expert, digital)
root.order.add_edge(digital, legal)
root.order.add_edge(legal, ethics)
root.order.add_edge(ethics, fraud)
root.order.add_edge(fraud, certify)
root.order.add_edge(certify, notify)
root.order.add_edge(notify, archive)
root.order.add_edge(archive, storage)