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

# Define the POWL model
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
xor_wear_analysis = OperatorPOWL(operator=Operator.XOR, children=[wear_analysis, skip])
xor_pattern_match = OperatorPOWL(operator=Operator.XOR, children=[pattern_match, skip])
xor_ownership = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, skip])
xor_ethics = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, skip])
xor_carbon = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, skip])
xor_restoration = OperatorPOWL(operator=Operator.XOR, children=[restoration_eval, skip])
xor_report = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
xor_stakeholder = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_review, skip])
xor_archive = OperatorPOWL(operator=Operator.XOR, children=[archive_data, skip])
xor_exhibit = OperatorPOWL(operator=Operator.XOR, children=[exhibit_approve, skip])
xor_condition = OperatorPOWL(operator=Operator.XOR, children=[condition_monitor, skip])
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_certification, skip])

root = StrictPartialOrder(nodes=[
    loop_provenance, xor_wear_analysis, xor_pattern_match, xor_ownership, xor_ethics, xor_carbon, xor_restoration,
    xor_report, xor_stakeholder, xor_archive, xor_exhibit, xor_condition, xor_final
])

# Define the partial order dependencies
root.order.add_edge(loop_provenance, xor_wear_analysis)
root.order.add_edge(xor_wear_analysis, xor_pattern_match)
root.order.add_edge(xor_pattern_match, xor_ownership)
root.order.add_edge(xor_ownership, xor_ethics)
root.order.add_edge(xor_ethics, xor_carbon)
root.order.add_edge(xor_carbon, xor_restoration)
root.order.add_edge(xor_restoration, xor_report)
root.order.add_edge(xor_report, xor_stakeholder)
root.order.add_edge(xor_stakeholder, xor_archive)
root.order.add_edge(xor_archive, xor_exhibit)
root.order.add_edge(xor_exhibit, xor_condition)
root.order.add_edge(xor_condition, xor_final)

print(root)