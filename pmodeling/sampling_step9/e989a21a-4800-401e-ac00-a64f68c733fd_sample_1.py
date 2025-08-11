import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
forgery_detect = Transition(label='Forgery Detect')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
final_approval = Transition(label='Final Approval')
archive_store = Transition(label='Archive Store')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[pigment_analyze, style_compare])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_trace, data_crosscheck])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[infrared_scan, xray_fluoresce])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, forgery_detect])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, stakeholder_review])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[archive_store, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, xor1, xor2])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop3, xor1)
root.order.add_edge(loop4, xor1)
root.order.add_edge(loop5, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, final_approval)
root.order.add_edge(xor2, archive_store)

print(root)