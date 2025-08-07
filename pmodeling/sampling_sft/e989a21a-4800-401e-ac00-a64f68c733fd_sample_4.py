import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
visual_inspect   = Transition(label='Visual Inspect')
document_gather  = Transition(label='Document Gather')
material_test    = Transition(label='Material Test')
pigment_analyze  = Transition(label='Pigment Analyze')
style_compare    = Transition(label='Style Compare')
expert_consult   = Transition(label='Expert Consult')
forgery_detect   = Transition(label='Forgery Detect')
data_crosscheck  = Transition(label='Data Crosscheck')
infrared_scan    = Transition(label='Infrared Scan')
xray_fluoresce   = Transition(label='Xray Fluoresce')
provenance_trace = Transition(label='Provenance Trace')
report_draft     = Transition(label='Report Draft')
stakeholder_rev  = Transition(label='Stakeholder Review')
final_approval   = Transition(label='Final Approval')
archive_store    = Transition(label='Archive Store')

# Build the loop for iterative expert consultation and forgery detection
loop_body = StrictPartialOrder(nodes=[expert_consult, forgery_detect])
loop_body.order.add_edge(expert_consult, forgery_detect)
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, data_crosscheck])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    visual_inspect,
    document_gather,
    material_test,
    pigment_analyze,
    style_compare,
    provenance_trace,
    expert_loop,
    infrared_scan,
    xray_fluoresce,
    report_draft,
    stakeholder_rev,
    final_approval,
    archive_store
])

# Add edges defining the control-flow dependencies
root.order.add_edge(visual_inspect, document_gather)
root.order.add_edge(document_gather, material_test)
root.order.add_edge(material_test, pigment_analyze)
root.order.add_edge(pigment_analyze, style_compare)
root.order.add_edge(style_compare, provenance_trace)
root.order.add_edge(provenance_trace, expert_loop)
root.order.add_edge(expert_loop, infrared_scan)
root.order.add_edge(expert_loop, xray_fluoresce)
root.order.add_edge(infrared_scan, report_draft)
root.order.add_edge(xray_fluoresce, report_draft)
root.order.add_edge(report_draft, stakeholder_rev)
root.order.add_edge(stakeholder_rev, final_approval)
root.order.add_edge(final_approval, archive_store)