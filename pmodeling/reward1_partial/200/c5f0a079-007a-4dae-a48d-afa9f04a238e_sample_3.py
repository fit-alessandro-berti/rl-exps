import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define process tree structure
provenance_check_and_material_scan = OperatorPOWL(operator=Operator.OR, children=[provenance_check, material_scan])
wear_analysis_and_image_capture = OperatorPOWL(operator=Operator.OR, children=[wear_analysis, image_capture])
pattern_match_and_ownership_verify = OperatorPOWL(operator=Operator.OR, children=[pattern_match, ownership_verify])
ethics_review_and_carbon_dating = OperatorPOWL(operator=Operator.OR, children=[ethics_review, carbon_dating])
restoration_eval_and_report_draft = OperatorPOWL(operator=Operator.OR, children=[restoration_eval, report_draft])
stakeholder_review_and_archive_data = OperatorPOWL(operator=Operator.OR, children=[stakeholder_review, archive_data])
exhibit_approve_and_condition_monitor = OperatorPOWL(operator=Operator.OR, children=[exhibit_approve, condition_monitor])
final_certification_and_condition_monitor = OperatorPOWL(operator=Operator.OR, children=[final_certification, condition_monitor])

root = StrictPartialOrder(nodes=[
    provenance_check_and_material_scan,
    wear_analysis_and_image_capture,
    pattern_match_and_ownership_verify,
    ethics_review_and_carbon_dating,
    restoration_eval_and_report_draft,
    stakeholder_review_and_archive_data,
    exhibit_approve_and_condition_monitor,
    final_certification_and_condition_monitor
])
root.order.add_edge(provenance_check_and_material_scan, wear_analysis_and_image_capture)
root.order.add_edge(provenance_check_and_material_scan, pattern_match_and_ownership_verify)
root.order.add_edge(provenance_check_and_material_scan, ethics_review_and_carbon_dating)
root.order.add_edge(wear_analysis_and_image_capture, restoration_eval_and_report_draft)
root.order.add_edge(wear_analysis_and_image_capture, stakeholder_review_and_archive_data)
root.order.add_edge(pattern_match_and_ownership_verify, exhibit_approve_and_condition_monitor)
root.order.add_edge(pattern_match_and_ownership_verify, final_certification_and_condition_monitor)
root.order.add_edge(ethics_review_and_carbon_dating, restoration_eval_and_report_draft)
root.order.add_edge(ethics_review_and_carbon_dating, stakeholder_review_and_archive_data)
root.order.add_edge(restoration_eval_and_report_draft, exhibit_approve_and_condition_monitor)
root.order.add_edge(restoration_eval_and_report_draft, final_certification_and_condition_monitor)
root.order.add_edge(stakeholder_review_and_archive_data, exhibit_approve_and_condition_monitor)
root.order.add_edge(stakeholder_review_and_archive_data, final_certification_and_condition_monitor)
root.order.add_edge(exhibit_approve_and_condition_monitor, final_certification_and_condition_monitor)