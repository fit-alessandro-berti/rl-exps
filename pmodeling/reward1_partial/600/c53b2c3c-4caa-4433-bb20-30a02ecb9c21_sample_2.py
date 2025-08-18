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

# Initial process steps
process = StrictPartialOrder(nodes=[
    discover_item, document_find, initial_survey, image_capture, material_testing, style_compare, expert_consult,
    provenance_check, ownership_verify, legal_review, risk_assess, conservation_plan, certification, secure_transfer
])
process.order.add_edge(discover_item, document_find)
process.order.add_edge(document_find, initial_survey)
process.order.add_edge(initial_survey, image_capture)
process.order.add_edge(image_capture, material_testing)
process.order.add_edge(material_testing, style_compare)
process.order.add_edge(style_compare, expert_consult)
process.order.add_edge(expert_consult, provenance_check)
process.order.add_edge(provenance_check, ownership_verify)
process.order.add_edge(ownership_verify, legal_review)
process.order.add_edge(legal_review, risk_assess)
process.order.add_edge(risk_assess, conservation_plan)
process.order.add_edge(conservation_plan, certification)
process.order.add_edge(certification, secure_transfer)

# Dispute resolution and final archive steps
dispute_process = StrictPartialOrder(nodes=[
    dispute_resolve, final_archive
])
process.order.add_edge(secure_transfer, dispute_resolve)
process.order.add_edge(dispute_resolve, final_archive)

root = process