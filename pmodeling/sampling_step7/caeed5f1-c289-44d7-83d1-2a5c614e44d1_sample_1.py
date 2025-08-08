import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
client_meet = Transition(label='Client Meet')
vision_capture = Transition(label='Vision Capture')
concept_draft = Transition(label='Concept Draft')
feedback_loop = Transition(label='Feedback Loop')
material_sourcing = Transition(label='Material Sourcing')
vendor_selection = Transition(label='Vendor Selection')
artisan_assign = Transition(label='Artisan Assign')
prototype_build = Transition(label='Prototype Build')
quality_review = Transition(label='Quality Review')
technical_check = Transition(label='Technical Check')
final_approval = Transition(label='Final Approval')
packaging_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
secure_transport = Transition(label='Secure Transport')
installation_set = Transition(label='Installation Set')
client_support = Transition(label='Client Support')
archival_record = Transition(label='Archival Record')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    client_meet, vision_capture, concept_draft, feedback_loop, material_sourcing, vendor_selection, artisan_assign, prototype_build,
    quality_review, technical_check, final_approval, packaging_prep, logistics_plan, secure_transport, installation_set, client_support, archival_record
])

# Define the partial order dependencies
root.order.add_edge(client_meet, vision_capture)
root.order.add_edge(vision_capture, concept_draft)
root.order.add_edge(concept_draft, feedback_loop)
root.order.add_edge(feedback_loop, material_sourcing)
root.order.add_edge(material_sourcing, vendor_selection)
root.order.add_edge(vendor_selection, artisan_assign)
root.order.add_edge(artisan_assign, prototype_build)
root.order.add_edge(prototype_build, quality_review)
root.order.add_edge(quality_review, technical_check)
root.order.add_edge(technical_check, final_approval)
root.order.add_edge(final_approval, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, secure_transport)
root.order.add_edge(secure_transport, installation_set)
root.order.add_edge(installation_set, client_support)
root.order.add_edge(client_support, archival_record)

# Print the root of the POWL model
print(root)