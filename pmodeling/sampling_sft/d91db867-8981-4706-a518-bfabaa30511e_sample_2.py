import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
provenance = Transition(label='Provenance Check')
material = Transition(label='Material Scan')
context = Transition(label='Context Review')
expert = Transition(label='Expert Consult')
image = Transition(label='Image Capture')
condition = Transition(label='Condition Test')
forgery = Transition(label='Forgery Risk')
registry = Transition(label='Registry Crosscheck')
legal = Transition(label='Legal Verify')
ethics = Transition(label='Ethics Review')
report = Transition(label='Report Draft')
certificate = Transition(label='Certificate Issue')
archive = Transition(label='Digital Archive')
setup = Transition(label='Transfer Setup')
approval = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    provenance, material, context, expert,
    image, condition, forgery,
    registry, legal, ethics,
    report, certificate, archive, setup, approval
])

# Initial provenance research must complete before material analysis
root.order.add_edge(provenance, material)

# After material analysis, context review can start in parallel
root.order.add_edge(material, context)

# Context review then triggers expert consultation
root.order.add_edge(context, expert)

# Expert consultation can proceed in parallel with image capture
root.order.add_edge(expert, image)

# Image capture then proceeds to condition testing
root.order.add_edge(image, condition)

# Condition testing then triggers forgery risk evaluation
root.order.add_edge(condition, forgery)

# Following forgery risk, crosscheck with international registries
root.order.add_edge(forgery, registry)

# After registry crosscheck, legal compliance can be verified
root.order.add_edge(registry, legal)

# Legal verify then proceeds to ethics review
root.order.add_edge(legal, ethics)

# Ethics review then triggers report drafting
root.order.add_edge(ethics, report)

# Report drafting then proceeds to certificate issuance
root.order.add_edge(report, certificate)

# Issuance then triggers digital archival
root.order.add_edge(certificate, archive)

# Archival then proceeds to transfer setup
root.order.add_edge(archive, setup)

# Finally, transfer setup can proceed in parallel with final approval
root.order.add_edge(setup, approval)

# Note: No explicit loop or concurrency is needed here, as all activities are sequential.