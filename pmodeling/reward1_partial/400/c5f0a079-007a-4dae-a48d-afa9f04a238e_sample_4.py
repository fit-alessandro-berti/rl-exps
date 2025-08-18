from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
wear_analysis = Transition(label='Wear Analysis')
image_capture = Transition(label='Image Capture')
pattern_match = Transition(label='Pattern Match')
ownership_verify = Transition(label='Ownership Verify')
ethics_review = Transition(label='Ethics Review')
carbon_dating = Transition(label='Carbon Dating')
restoration_eval = Transition(label='Restoration Eval')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
archive_data = Transition(label='Archive Data')
exhibit_approve = Transition(label='Exhibit Approve')
condition_monitor = Transition(label='Condition Monitor')
final_certification = Transition(label='Final Certification')

skip = SilentTransition()

provenance_check_to_material_scan = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
material_scan_to_wear_analysis = OperatorPOWL(operator=Operator.XOR, children=[material_scan, skip])
wear_analysis_to_image_capture = OperatorPOWL(operator=Operator.XOR, children=[wear_analysis, skip])
image_capture_to_pattern_match = OperatorPOWL(operator=Operator.XOR, children=[image_capture, skip])
pattern_match_to_ownership_verify = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, skip])
ownership_verify_to_ethics_review = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, skip])
ethics_review_to_carbon_dating = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, skip])
carbon_dating_to_restoration_eval = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, skip])
restoration_eval_to_report_draft = OperatorPOWL(operator=Operator.XOR, children=[restoration_eval, skip])
report_draft_to_stakeholder_review = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
stakeholder_review_to_archive_data = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_review, skip])
archive_data_to_exhibit_approve = OperatorPOWL(operator=Operator.XOR, children=[archive_data, skip])
exhibit_approve_to_condition_monitor = OperatorPOWL(operator=Operator.XOR, children=[exhibit_approve, skip])
condition_monitor_to_final_certification = OperatorPOWL(operator=Operator.XOR, children=[condition_monitor, skip])

root = StrictPartialOrder(nodes=[
    provenance_check_to_material_scan,
    material_scan_to_wear_analysis,
    wear_analysis_to_image_capture,
    image_capture_to_pattern_match,
    pattern_match_to_ownership_verify,
    ownership_verify_to_ethics_review,
    ethics_review_to_carbon_dating,
    carbon_dating_to_restoration_eval,
    restoration_eval_to_report_draft,
    report_draft_to_stakeholder_review,
    stakeholder_review_to_archive_data,
    archive_data_to_exhibit_approve,
    exhibit_approve_to_condition_monitor,
    condition_monitor_to_final_certification
])
root.order.add_edge(provenance_check_to_material_scan, material_scan_to_wear_analysis)
root.order.add_edge(material_scan_to_wear_analysis, wear_analysis_to_image_capture)
root.order.add_edge(wear_analysis_to_image_capture, image_capture_to_pattern_match)
root.order.add_edge(image_capture_to_pattern_match, pattern_match_to_ownership_verify)
root.order.add_edge(pattern_match_to_ownership_verify, ownership_verify_to_ethics_review)
root.order.add_edge(ownership_verify_to_ethics_review, ethics_review_to_carbon_dating)
root.order.add_edge(ethics_review_to_carbon_dating, carbon_dating_to_restoration_eval)
root.order.add_edge(carbon_dating_to_restoration_eval, restoration_eval_to_report_draft)
root.order.add_edge(restoration_eval_to_report_draft, report_draft_to_stakeholder_review)
root.order.add_edge(report_draft_to_stakeholder_review, stakeholder_review_to_archive_data)
root.order.add_edge(stakeholder_review_to_archive_data, archive_data_to_exhibit_approve)
root.order.add_edge(archive_data_to_exhibit_approve, exhibit_approve_to_condition_monitor)
root.order.add_edge(exhibit_approve_to_condition_monitor, condition_monitor_to_final_certification)

print(root)