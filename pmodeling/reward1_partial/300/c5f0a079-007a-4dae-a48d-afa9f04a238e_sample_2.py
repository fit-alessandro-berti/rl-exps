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

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, wear_analysis, image_capture, pattern_match, ownership_verify, ethics_review, carbon_dating, restoration_eval])
provenance_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, skip])

report_draft_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, stakeholder_review, archive_data, exhibit_approve, condition_monitor, final_certification])
report_draft_xor = OperatorPOWL(operator=Operator.XOR, children=[report_draft_loop, skip])

root = StrictPartialOrder(nodes=[provenance_xor, report_draft_xor])
root.order.add_edge(provenance_xor, report_draft_xor)

print(root)