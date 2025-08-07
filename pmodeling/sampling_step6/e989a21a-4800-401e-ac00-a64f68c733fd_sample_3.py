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

# Define the root POWL model as a strict partial order
root = StrictPartialOrder(nodes=[
    visual_inspect,
    document_gather,
    material_test,
    pigment_analyze,
    style_compare,
    provenance_trace,
    data_crosscheck,
    infrared_scan,
    xray_fluoresce,
    expert_consult,
    forgery_detect,
    report_draft,
    stakeholder_review,
    final_approval,
    archive_store
])

# Optionally, if there are any dependencies or connections between activities, you can add them here.
# For example, if 'Visual Inspect' needs to happen before 'Material Test':
# root.order.add_edge(visual_inspect, material_test)

# Now 'root' contains the POWL model for the described process.