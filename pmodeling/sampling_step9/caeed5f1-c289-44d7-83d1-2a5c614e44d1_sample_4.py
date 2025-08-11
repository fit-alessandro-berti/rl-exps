import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
client_meet = Transition(label='Client Meet')
vision_capture = Transition(label='Vision Capture')
concept_draft = Transition(label='Concept Draft')
feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[concept_draft, SilentTransition()])
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

# Define partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[vision_capture, feedback_loop])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, quality_review, technical_check])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, packaging_prep, logistics_plan])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[secure_transport, installation_set])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[client_support, archival_record])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)

# Print the root
print(root)