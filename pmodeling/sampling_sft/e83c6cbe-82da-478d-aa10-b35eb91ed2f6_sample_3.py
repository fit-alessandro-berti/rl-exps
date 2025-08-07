import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
provenance = Transition(label='Provenance Check')
material = Transition(label='Material Testing')
stylistic = Transition(label='Stylistic Review')
expert = Transition(label='Expert Panel')
legal = Transition(label='Legal Clearance')
ethics = Transition(label='Ethics Audit')
insurance = Transition(label='Insurance Quote')
risk = Transition(label='Risk Assess')
digital = Transition(label='Digital Archive')
replica = Transition(label='Replica Build')
transport = Transition(label='Transport Prep')
final_review = Transition(label='Final Review')
catalog = Transition(label='Catalog Entry')
public_notice = Transition(label='Public Notice')
condition = Transition(label='Condition Report')

# Build the verification & authentication sub-process
verification = StrictPartialOrder(nodes=[
    provenance, material, stylistic, expert,
    legal, ethics, insurance, risk,
    digital, replica, transport, final_review
])
verification.order.add_edge(provenance, material)
verification.order.add_edge(material, stylistic)
verification.order.add_edge(stylistic, expert)
verification.order.add_edge(provenance, legal)
verification.order.add_edge(provenance, ethics)
verification.order.add_edge(legal, insurance)
verification.order.add_edge(insurance, risk)
verification.order.add_edge(risk, digital)
verification.order.add_edge(digital, replica)
verification.order.add_edge(digital, transport)
verification.order.add_edge(replica, final_review)
verification.order.add_edge(transport, final_review)

# Build the preparation & announcement sub-process
preparation = StrictPartialOrder(nodes=[
    catalog, public_notice, condition
])
preparation.order.add_edge(final_review, catalog)
preparation.order.add_edge(final_review, public_notice)
preparation.order.add_edge(catalog, condition)
preparation.order.add_edge(public_notice, condition)

# Final partial order: combine both sub-processes
root = StrictPartialOrder(nodes=[
    verification, preparation
])
root.order.add_edge(verification, preparation)

print(root)