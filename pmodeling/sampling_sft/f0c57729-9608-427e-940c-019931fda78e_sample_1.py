import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
inquiry = Transition(label='Inquiry Intake')
consultation = Transition(label='Consultation Call')
concept = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Loop')
contract = Transition(label='Contract Setup')
artist_match = Transition(label='Artist Match')
material = Transition(label='Material Sourcing')
ethics = Transition(label='Ethics Review')
progress = Transition(label='Progress Check')
milestone = Transition(label='Milestone Approve')
quality = Transition(label='Quality Audit')
copyright = Transition(label='Copyright Transfer')
packaging = Transition(label='Packaging Plan')
shipping = Transition(label='Shipping Arrange')
delivery = Transition(label='Post Delivery')
survey = Transition(label='Client Survey')

# Build the partial order
root = StrictPartialOrder(nodes=[
    inquiry, consultation, concept, feedback,
    contract, artist_match, material, ethics,
    progress, milestone, quality, copyright,
    packaging, shipping, delivery, survey
])

# Define the control-flow dependencies
# 1. Inquiry to Consultation
root.order.add_edge(inquiry, consultation)

# 2. Consultation to Concept Draft
root.order.add_edge(consultation, concept)

# 3. Concept Draft to Feedback Loop
root.order.add_edge(concept, feedback)

# 4. Feedback Loop to Contract Setup
root.order.add_edge(feedback, contract)

# 5. Contract Setup to Artist Match
root.order.add_edge(contract, artist_match)

# 6. Artist Match to Material Sourcing
root.order.add_edge(artist_match, material)

# 7. Material Sourcing to Ethics Review
root.order.add_edge(material, ethics)

# 8. Ethics Review to Progress Check
root.order.add_edge(ethics, progress)

# 9. Progress Check to Milestone Approve
root.order.add_edge(progress, milestone)

# 10. Milestone Approve to Quality Audit
root.order.add_edge(milestone, quality)

# 11. Quality Audit to Copyright Transfer
root.order.add_edge(quality, copyright)

# 12. Copyright Transfer to Packaging Plan
root.order.add_edge(copyright, packaging)

# 13. Packaging Plan to Shipping Arrange
root.order.add_edge(packaging, shipping)

# 14. Shipping Arrange to Post Delivery
root.order.add_edge(shipping, delivery)

# 15. Post Delivery to Client Survey
root.order.add_edge(delivery, survey)

# Finalize the partial order
root.order.finalize()