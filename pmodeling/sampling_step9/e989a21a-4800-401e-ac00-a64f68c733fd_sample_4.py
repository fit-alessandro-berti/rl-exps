import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
visual_inspect = Transition(label='Visual Inspect')
document_gather = Transition(label='Document Gather')
material_test = Transition(label='Material Test')
pigment_analyze = Transition(label='Pigment Analyze')
style_compare = Transition(label='Style Compare')
provenance_trace = Transition(label='Provenance Trace')
data_crosscheck = Transition(label='Data Crosscheck')
infrared_scan = Transition(label='Infrared Scan')
xray_fluoresce = Transition(label='Xray Fluoresce')
expert_consult = Transition(label='Expert Consult')
forger_detect = Transition(label='Forgery Detect')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
final_approval = Transition(label='Final Approval')
archive_store = Transition(label='Archive Store')

# Define silent transitions
skip = SilentTransition()

# Define loop and XOR nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, pigment_analyze, style_compare, provenance_trace, data_crosscheck])
xor = OperatorPOWL(operator=Operator.XOR, children=[infrared_scan, xray_fluoresce])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, forger_detect])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, stakeholder_review])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, archive_store])

# Define root node
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)

# Print the root node
print(root)