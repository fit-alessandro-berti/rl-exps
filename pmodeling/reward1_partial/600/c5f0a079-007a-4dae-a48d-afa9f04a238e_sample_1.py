import pm4py
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

provenance_check_to_material_scan = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
material_scan_to_wear_analysis = OperatorPOWL(operator=Operator.XOR, children=[material_scan, wear_analysis])
wear_analysis_to_image_capture = OperatorPOWL(operator=Operator.XOR, children=[wear_analysis, image_capture])
image_capture_to_pattern_match = OperatorPOWL(operator=Operator.XOR, children=[image_capture, pattern_match])
pattern_match_to_ownership_verify = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, ownership_verify])
ownership_verify_to_ethics_review = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, ethics_review])
ethics_review_to_carbon_dating = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, carbon_dating])
carbon_dating_to_restoration_eval = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, restoration_eval])
restoration_eval_to_report_draft = OperatorPOWL(operator=Operator.XOR, children=[restoration_eval, report_draft])
report_draft_to_stakeholder_review = OperatorPOWL(operator=Operator.XOR, children=[report_draft, stakeholder_review])
stakeholder_review_to_archive_data = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_review, archive_data])
archive_data_to_exhibit_approve = OperatorPOWL(operator=Operator.XOR, children=[archive_data, exhibit_approve])
exhibit_approve_to_condition_monitor = OperatorPOWL(operator=Operator.XOR, children=[exhibit_approve, condition_monitor])
condition_monitor_to_final_certification = OperatorPOWL(operator=Operator.XOR, children=[condition_monitor, final_certification])

root = StrictPartialOrder(nodes=[
    provenance_check,
    material_scan,
    wear_analysis,
    image_capture,
    pattern_match,
    ownership_verify,
    ethics_review,
    carbon_dating,
    restoration_eval,
    report_draft,
    stakeholder_review,
    archive_data,
    exhibit_approve,
    condition_monitor,
    final_certification
])
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, wear_analysis)
root.order.add_edge(wear_analysis, image_capture)
root.order.add_edge(image_capture, pattern_match)
root.order.add_edge(pattern_match, ownership_verify)
root.order.add_edge(ownership_verify, ethics_review)
root.order.add_edge(ethics_review, carbon_dating)
root.order.add_edge(carbon_dating, restoration_eval)
root.order.add_edge(restoration_eval, report_draft)
root.order.add_edge(report_draft, stakeholder_review)
root.order.add_edge(stakeholder_review, archive_data)
root.order.add_edge(archive_data, exhibit_approve)
root.order.add_edge(exhibit_approve, condition_monitor)
root.order.add_edge(condition_monitor, final_certification)