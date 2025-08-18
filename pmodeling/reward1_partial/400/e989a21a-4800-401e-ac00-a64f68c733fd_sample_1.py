import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[forgery_detect, stakeholder_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, stakeholder_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[data_crosscheck, stakeholder_review])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, stakeholder_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, stakeholder_review])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[archive_store, stakeholder_review])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, archive_store])

# Define the partial order
root = StrictPartialOrder(nodes=[
    visual_inspect, 
    document_gather, 
    material_test, 
    pigment_analyze, 
    style_compare, 
    provenance_trace, 
    xor1, 
    xor2, 
    xor3, 
    xor4, 
    xor5, 
    xor6, 
    xor7, 
    report_draft, 
    expert_consult, 
    stakeholder_review, 
    final_approval, 
    archive_store
])

# Define the dependencies
root.order.add_edge(visual_inspect, document_gather)
root.order.add_edge(visual_inspect, material_test)
root.order.add_edge(visual_inspect, pigment_analyze)
root.order.add_edge(visual_inspect, style_compare)
root.order.add_edge(visual_inspect, provenance_trace)
root.order.add_edge(document_gather, material_test)
root.order.add_edge(document_gather, pigment_analyze)
root.order.add_edge(document_gather, style_compare)
root.order.add_edge(document_gather, provenance_trace)
root.order.add_edge(material_test, xor1)
root.order.add_edge(pigment_analyze, xor2)
root.order.add_edge(style_compare, xor3)
root.order.add_edge(provenance_trace, xor4)
root.order.add_edge(xor1, xor5)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, report_draft)
root.order.add_edge(xor7, expert_consult)
root.order.add_edge(xor7, stakeholder_review)
root.order.add_edge(xor7, final_approval)
root.order.add_edge(xor7, archive_store)

print(root)