import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
submit      = Transition(label='Submit Artifact')
initial     = Transition(label='Initial Review')
prov        = Transition(label='Provenance Check')
material    = Transition(label='Material Scan')
context     = Transition(label='Context Analysis')
expert      = Transition(label='Expert Panel')
ai          = Transition(label='AI Pattern')
digital     = Transition(label='Digital Fingerprint')
legal       = Transition(label='Legal Audit')
ethics      = Transition(label='Ethics Review')
fraud       = Transition(label='Fraud Detection')
blockchain  = Transition(label='Blockchain Log')
certify     = Transition(label='Certification')
owner       = Transition(label='Owner Notify')
archive     = Transition(label='Archive Data')
store       = Transition(label='Secure Storage')

# Loop for iterative AI pattern analysis (optional but useful)
skip = SilentTransition()
ai_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    submit, initial, prov, material, context, expert,
    ai_loop, digital, legal, ethics, fraud,
    blockchain, certify, owner, archive, store
])

# Define the control-flow dependencies
root.order.add_edge(submit, initial)
root.order.add_edge(initial, prov)
root.order.add_edge(initial, material)
root.order.add_edge(initial, context)
root.order.add_edge(prov, expert)
root.order.add_edge(material, ai_loop)
root.order.add_edge(context, ai_loop)
root.order.add_edge(ai_loop, digital)
root.order.add_edge(digital, legal)
root.order.add_edge(digital, ethics)
root.order.add_edge(digital, fraud)
root.order.add_edge(legal, blockchain)
root.order.add_edge(ethics, blockchain)
root.order.add_edge(fraud, blockchain)
root.order.add_edge(blockchain, certify)
root.order.add_edge(certify, owner)
root.order.add_edge(certify, archive)
root.order.add_edge(owner, store)
root.order.add_edge(archive, store)