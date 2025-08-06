import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
client_meet = Transition(label='Client Meet')
vision_capture = Transition(label='Vision Capture')
concept_draft = Transition(label='Concept Draft')
feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[concept_draft, client_meet])
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

# Define the loop for the artisan assignments
artisan_loop = OperatorPOWL(operator=Operator.LOOP, children=[artisan_assign, prototype_build, quality_review, technical_check, final_approval])

# Define the XOR for the concept draft and client meet
xor = OperatorPOWL(operator=Operator.XOR, children=[vision_capture, artisan_loop])

# Define the root
root = StrictPartialOrder(nodes=[xor, feedback_loop, material_sourcing, vendor_selection, packaging_prep, logistics_plan, secure_transport, installation_set, client_support, archival_record])
root.order.add_edge(xor, feedback_loop)
root.order.add_edge(xor, material_sourcing)
root.order.add_edge(xor, vendor_selection)
root.order.add_edge(xor, packaging_prep)
root.order.add_edge(xor, logistics_plan)
root.order.add_edge(xor, secure_transport)
root.order.add_edge(xor, installation_set)
root.order.add_edge(xor, client_support)
root.order.add_edge(xor, archival_record)