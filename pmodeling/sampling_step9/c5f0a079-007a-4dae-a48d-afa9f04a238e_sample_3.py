import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
loop_provenance_check = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
loop_material_scan = OperatorPOWL(operator=Operator.LOOP, children=[material_scan])
xor_wear_analysis = OperatorPOWL(operator=Operator.XOR, children=[wear_analysis, skip])
xor_image_capture = OperatorPOWL(operator=Operator.XOR, children=[image_capture, skip])
xor_pattern_match = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, skip])
xor_ownership_verify = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, skip])
xor_ethics_review = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, skip])
xor_carbon_dating = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, skip])
xor_restoration_eval = OperatorPOWL(operator=Operator.XOR, children=[restoration_eval, skip])
xor_report_draft = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
xor_stakeholder_review = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_review, skip])
xor_archive_data = OperatorPOWL(operator=Operator.XOR, children=[archive_data, skip])
xor_exhibit_approve = OperatorPOWL(operator=Operator.XOR, children=[exhibit_approve, skip])
xor_condition_monitor = OperatorPOWL(operator=Operator.XOR, children=[condition_monitor, skip])
xor_final_certification = OperatorPOWL(operator=Operator.XOR, children=[final_certification, skip])

root = StrictPartialOrder(nodes=[
    loop_provenance_check,
    loop_material_scan,
    xor_wear_analysis,
    xor_image_capture,
    xor_pattern_match,
    xor_ownership_verify,
    xor_ethics_review,
    xor_carbon_dating,
    xor_restoration_eval,
    xor_report_draft,
    xor_stakeholder_review,
    xor_archive_data,
    xor_exhibit_approve,
    xor_condition_monitor,
    xor_final_certification
])
root.order.add_edge(loop_provenance_check, xor_wear_analysis)
root.order.add_edge(loop_provenance_check, xor_image_capture)
root.order.add_edge(loop_provenance_check, xor_pattern_match)
root.order.add_edge(loop_provenance_check, xor_ownership_verify)
root.order.add_edge(loop_provenance_check, xor_ethics_review)
root.order.add_edge(loop_provenance_check, xor_carbon_dating)
root.order.add_edge(loop_provenance_check, xor_restoration_eval)
root.order.add_edge(loop_provenance_check, xor_report_draft)
root.order.add_edge(loop_provenance_check, xor_stakeholder_review)
root.order.add_edge(loop_provenance_check, xor_archive_data)
root.order.add_edge(loop_provenance_check, xor_exhibit_approve)
root.order.add_edge(loop_provenance_check, xor_condition_monitor)
root.order.add_edge(loop_provenance_check, xor_final_certification)
root.order.add_edge(loop_material_scan, xor_wear_analysis)
root.order.add_edge(loop_material_scan, xor_image_capture)
root.order.add_edge(loop_material_scan, xor_pattern_match)
root.order.add_edge(loop_material_scan, xor_ownership_verify)
root.order.add_edge(loop_material_scan, xor_ethics_review)
root.order.add_edge(loop_material_scan, xor_carbon_dating)
root.order.add_edge(loop_material_scan, xor_restoration_eval)
root.order.add_edge(loop_material_scan, xor_report_draft)
root.order.add_edge(loop_material_scan, xor_stakeholder_review)
root.order.add_edge(loop_material_scan, xor_archive_data)
root.order.add_edge(loop_material_scan, xor_exhibit_approve)
root.order.add_edge(loop_material_scan, xor_condition_monitor)
root.order.add_edge(loop_material_scan, xor_final_certification)