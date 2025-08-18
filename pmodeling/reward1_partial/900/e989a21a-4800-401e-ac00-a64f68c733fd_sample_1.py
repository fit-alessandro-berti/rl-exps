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

# Multi-step process model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, pigment_analyze, style_compare])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_trace, data_crosscheck, infrared_scan, xray_fluoresce, expert_consult, forgery_detect])
xor = OperatorPOWL(operator=Operator.XOR, children=[report_draft, stakeholder_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, archive_store])
root = StrictPartialOrder(nodes=[visual_inspect, document_gather, loop1, loop2, xor, xor2])
root.order.add_edge(visual_inspect, document_gather)
root.order.add_edge(document_gather, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, final_approval)
root.order.add_edge(xor2, archive_store)

print(root)