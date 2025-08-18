import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
client_meet = Transition(label='Client Meet')
vision_capture = Transition(label='Vision Capture')
concept_draft = Transition(label='Concept Draft')
feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Artistic Critique'), Transition(label='Technical Check')])
material_sourcing = Transition(label='Material Sourcing')
vendor_selection = Transition(label='Vendor Selection')
artisan_assign = Transition(label='Artisan Assign')
prototype_build = Transition(label='Prototype Build')
quality_review = Transition(label='Quality Review')
final_approval = Transition(label='Final Approval')
packaging_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
secure_transport = Transition(label='Secure Transport')
installation_set = Transition(label='Installation Set')
client_support = Transition(label='Client Support')
archival_record = Transition(label='Archival Record')

# Define loops and partial order
concept_loop = OperatorPOWL(operator=Operator.LOOP, children=[vision_capture, concept_draft, feedback_loop])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, vendor_selection, artisan_assign, prototype_build, quality_review, final_approval])
logistics_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, logistics_plan, secure_transport, installation_set, client_support, archival_record])

# Construct the POWL model
root = StrictPartialOrder(nodes=[concept_loop, material_loop, logistics_loop])

# Add dependencies
root.order.add_edge(concept_loop, material_loop)
root.order.add_edge(material_loop, logistics_loop)

print(root)