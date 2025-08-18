import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

discover_item = Transition(label='Discover Item')
document_find = Transition(label='Document Find')
initial_survey = Transition(label='Initial Survey')
image_capture = Transition(label='Image Capture')
material_testing = Transition(label='Material Testing')
style_compare = Transition(label='Style Compare')
expert_consult = Transition(label='Expert Consult')
provenance_check = Transition(label='Provenance Check')
ownership_verify = Transition(label='Ownership Verify')
legal_review = Transition(label='Legal Review')
risk_assess = Transition(label='Risk Assess')
conservation_plan = Transition(label='Conservation Plan')
certification = Transition(label='Certification')
secure_transfer = Transition(label='Secure Transfer')
dispute_resolve = Transition(label='Dispute Resolve')
final_archive = Transition(label='Final Archive')

skip = SilentTransition()
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[certification, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[secure_transfer, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[dispute_resolve, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[final_archive, skip])

root = StrictPartialOrder(nodes=[
    discover_item, document_find, initial_survey, image_capture, material_testing, style_compare, expert_consult, xor1,
    xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9
])

root.order.add_edge(discover_item, document_find)
root.order.add_edge(document_find, initial_survey)
root.order.add_edge(initial_survey, image_capture)
root.order.add_edge(image_capture, material_testing)
root.order.add_edge(material_testing, style_compare)
root.order.add_edge(style_compare, expert_consult)
root.order.add_edge(expert_consult, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, final_archive)