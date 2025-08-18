import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

provenance_check = Transition(label='Provenance Check')
image_capture = Transition(label='Image Capture')
material_scan = Transition(label='Material Scan')
expert_review = Transition(label='Expert Review')
historical_cross = Transition(label='Historical Cross')
legal_verify = Transition(label='Legal Verify')
registry_search = Transition(label='Registry Search')
customs_clear = Transition(label='Customs Clear')
condition_assess = Transition(label='Condition Assess')
data_log = Transition(label='Data Log')
chain_custody = Transition(label='Chain Custody')
report_draft = Transition(label='Report Draft')
certification = Transition(label='Certification')
secure_archive = Transition(label='Secure Archive')
auction_prep = Transition(label='Auction Prep')

skip = SilentTransition()

provenance_check_to_image_capture = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, image_capture])
image_capture_to_material_scan = OperatorPOWL(operator=Operator.XOR, children=[image_capture, material_scan])
material_scan_to_expert_review = OperatorPOWL(operator=Operator.XOR, children=[material_scan, expert_review])
expert_review_to_historical_cross = OperatorPOWL(operator=Operator.XOR, children=[expert_review, historical_cross])
historical_cross_to_legal_verify = OperatorPOWL(operator=Operator.XOR, children=[historical_cross, legal_verify])
legal_verify_to_registry_search = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, registry_search])
registry_search_to_customs_clear = OperatorPOWL(operator=Operator.XOR, children=[registry_search, customs_clear])
customs_clear_to_condition_assess = OperatorPOWL(operator=Operator.XOR, children=[customs_clear, condition_assess])
condition_assess_to_data_log = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, data_log])
data_log_to_chain_custody = OperatorPOWL(operator=Operator.XOR, children=[data_log, chain_custody])
chain_custody_to_report_draft = OperatorPOWL(operator=Operator.XOR, children=[chain_custody, report_draft])
report_draft_to_certification = OperatorPOWL(operator=Operator.XOR, children=[report_draft, certification])
certification_to_secure_archive = OperatorPOWL(operator=Operator.XOR, children=[certification, secure_archive])
secure_archive_to_auction_prep = OperatorPOWL(operator=Operator.XOR, children=[secure_archive, auction_prep])

root = StrictPartialOrder(nodes=[
    provenance_check_to_image_capture,
    image_capture_to_material_scan,
    material_scan_to_expert_review,
    expert_review_to_historical_cross,
    historical_cross_to_legal_verify,
    legal_verify_to_registry_search,
    registry_search_to_customs_clear,
    customs_clear_to_condition_assess,
    condition_assess_to_data_log,
    data_log_to_chain_custody,
    chain_custody_to_report_draft,
    report_draft_to_certification,
    certification_to_secure_archive,
    secure_archive_to_auction_prep
])

root.order.add_edge(provenance_check_to_image_capture, image_capture_to_material_scan)
root.order.add_edge(image_capture_to_material_scan, material_scan_to_expert_review)
root.order.add_edge(material_scan_to_expert_review, expert_review_to_historical_cross)
root.order.add_edge(expert_review_to_historical_cross, historical_cross_to_legal_verify)
root.order.add_edge(historical_cross_to_legal_verify, legal_verify_to_registry_search)
root.order.add_edge(legal_verify_to_registry_search, registry_search_to_customs_clear)
root.order.add_edge(registry_search_to_customs_clear, customs_clear_to_condition_assess)
root.order.add_edge(customs_clear_to_condition_assess, condition_assess_to_data_log)
root.order.add_edge(condition_assess_to_data_log, data_log_to_chain_custody)
root.order.add_edge(data_log_to_chain_custody, chain_custody_to_report_draft)
root.order.add_edge(chain_custody_to_report_draft, report_draft_to_certification)
root.order.add_edge(report_draft_to_certification, certification_to_secure_archive)
root.order.add_edge(certification_to_secure_archive, secure_archive_to_auction_prep)