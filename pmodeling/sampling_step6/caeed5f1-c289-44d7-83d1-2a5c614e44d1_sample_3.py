import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order (workflow)
root = StrictPartialOrder(nodes=[
    client_meet,
    vision_capture,
    concept_draft,
    feedback_loop,
    material_sourcing,
    vendor_selection,
    artisan_assign,
    prototype_build,
    quality_review,
    technical_check,
    final_approval,
    packaging_prep,
    logistics_plan,
    secure_transport,
    installation_set,
    client_support,
    archival_record
])

# Add dependencies between transitions if necessary
# For example, if client meet leads to vision capture:
# root.order.add_edge(client_meet, vision_capture)

# Print or return the root to use it further in your process
print(root)