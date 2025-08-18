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
forgeries_detect = Transition(label='Forgery Detect')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
final_approval = Transition(label='Final Approval')
archive_store = Transition(label='Archive Store')

# Define silent transitions
skip = SilentTransition()

# Define process tree nodes and their relationships
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, stakeholder_review])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[infrared_scan, xray_fluoresce])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[data_crosscheck, final_approval])
xor = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
root = StrictPartialOrder(nodes=[visual_inspect, document_gather, material_test, pigment_analyze, style_compare, provenance_trace, loop1, loop2, loop3, xor])
root.order.add_edge(visual_inspect, document_gather)
root.order.add_edge(document_gather, material_test)
root.order.add_edge(material_test, pigment_analyze)
root.order.add_edge(pigment_analyze, style_compare)
root.order.add_edge(style_compare, provenance_trace)
root.order.add_edge(provenance_trace, loop1)
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, loop1)
root.order.add_edge(loop3, loop2)
root.order.add_edge(xor, archive_store)

# Return the root node of the POWL model
return root