import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the process structure
provenance_check_then_material_scan = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
wear_analysis_then_image_capture = OperatorPOWL(operator=Operator.XOR, children=[wear_analysis, image_capture])
pattern_match_then_ethics_review = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, ethics_review])
carbon_dating_then_restoration_eval = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, restoration_eval])
report_draft_then_stakeholder_review = OperatorPOWL(operator=Operator.XOR, children=[report_draft, stakeholder_review])
archive_data_then_condition_monitor = OperatorPOWL(operator=Operator.XOR, children=[archive_data, condition_monitor])
final_certification_then_exhibit_approve = OperatorPOWL(operator=Operator.XOR, children=[final_certification, exhibit_approve])

# Define the partial order
root = StrictPartialOrder(nodes=[
    provenance_check_then_material_scan,
    wear_analysis_then_image_capture,
    pattern_match_then_ethics_review,
    carbon_dating_then_restoration_eval,
    report_draft_then_stakeholder_review,
    archive_data_then_condition_monitor,
    final_certification_then_exhibit_approve
])

# Define dependencies
root.order.add_edge(provenance_check_then_material_scan, wear_analysis_then_image_capture)
root.order.add_edge(provenance_check_then_material_scan, pattern_match_then_ethics_review)
root.order.add_edge(provenance_check_then_material_scan, carbon_dating_then_restoration_eval)
root.order.add_edge(provenance_check_then_material_scan, report_draft_then_stakeholder_review)
root.order.add_edge(provenance_check_then_material_scan, archive_data_then_condition_monitor)
root.order.add_edge(provenance_check_then_material_scan, final_certification_then_exhibit_approve)
root.order.add_edge(wear_analysis_then_image_capture, pattern_match_then_ethics_review)
root.order.add_edge(wear_analysis_then_image_capture, carbon_dating_then_restoration_eval)
root.order.add_edge(wear_analysis_then_image_capture, report_draft_then_stakeholder_review)
root.order.add_edge(wear_analysis_then_image_capture, archive_data_then_condition_monitor)
root.order.add_edge(wear_analysis_then_image_capture, final_certification_then_exhibit_approve)
root.order.add_edge(pattern_match_then_ethics_review, carbon_dating_then_restoration_eval)
root.order.add_edge(pattern_match_then_ethics_review, report_draft_then_stakeholder_review)
root.order.add_edge(pattern_match_then_ethics_review, archive_data_then_condition_monitor)
root.order.add_edge(pattern_match_then_ethics_review, final_certification_then_exhibit_approve)
root.order.add_edge(carbon_dating_then_restoration_eval, report_draft_then_stakeholder_review)
root.order.add_edge(carbon_dating_then_restoration_eval, archive_data_then_condition_monitor)
root.order.add_edge(carbon_dating_then_restoration_eval, final_certification_then_exhibit_approve)
root.order.add_edge(report_draft_then_stakeholder_review, archive_data_then_condition_monitor)
root.order.add_edge(report_draft_then_stakeholder_review, final_certification_then_exhibit_approve)
root.order.add_edge(archive_data_then_condition_monitor, final_certification_then_exhibit_approve)

print(root)