from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define partial order nodes
xor_provenance_material = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
xor_wear_image = OperatorPOWL(operator=Operator.XOR, children=[wear_analysis, image_capture])
xor_pattern_ownership = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, ownership_verify])
xor_ethics_restoration = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, restoration_eval])
xor_date_report = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, report_draft])
xor_stakeholder_archive = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_review, archive_data])
xor_exhibit_condition = OperatorPOWL(operator=Operator.XOR, children=[exhibit_approve, condition_monitor])
xor_final_certification = OperatorPOWL(operator=Operator.XOR, children=[final_certification])

# Define partial order
root = StrictPartialOrder(nodes=[xor_provenance_material, xor_wear_image, xor_pattern_ownership, xor_ethics_restoration, xor_date_report, xor_stakeholder_archive, xor_exhibit_condition, xor_final_certification])
root.order.add_edge(xor_provenance_material, xor_wear_image)
root.order.add_edge(xor_wear_image, xor_pattern_ownership)
root.order.add_edge(xor_pattern_ownership, xor_ethics_restoration)
root.order.add_edge(xor_ethics_restoration, xor_date_report)
root.order.add_edge(xor_date_report, xor_stakeholder_archive)
root.order.add_edge(xor_stakeholder_archive, xor_exhibit_condition)
root.order.add_edge(xor_exhibit_condition, xor_final_certification)