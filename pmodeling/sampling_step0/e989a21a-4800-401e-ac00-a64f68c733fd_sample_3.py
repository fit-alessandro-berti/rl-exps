import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_trace, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[data_crosscheck, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[infrared_scan, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[xray_fluoresce, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[forgery_detect, skip])

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, pigment_analyze, style_compare])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6])

# Define root node
root = StrictPartialOrder(nodes=[loop1, loop2, visual_inspect, document_gather, report_draft, stakeholder_review, final_approval, archive_store])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop1, xor6)
root.order.add_edge(loop2, visual_inspect)
root.order.add_edge(loop2, document_gather)
root.order.add_edge(loop2, report_draft)
root.order.add_edge(loop2, stakeholder_review)
root.order.add_edge(loop2, final_approval)
root.order.add_edge(loop2, archive_store)

return root