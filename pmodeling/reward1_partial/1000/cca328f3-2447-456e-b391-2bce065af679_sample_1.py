import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
style_compare = Transition(label='Style Compare')
digital_capture = Transition(label='Digital Capture')
expert_review = Transition(label='Expert Review')
database_search = Transition(label='Database Search')
legal_audit = Transition(label='Legal Audit')
cultural_assess = Transition(label='Cultural Assess')
data_synthesis = Transition(label='Data Synthesis')
report_draft = Transition(label='Report Draft')
archival_store = Transition(label='Archival Store')
display_approve = Transition(label='Display Approve')
lender_notify = Transition(label='Lender Notify')
investigation_flag = Transition(label='Investigation Flag')

# Define silent transitions (no operation)
skip = SilentTransition()

# Define process tree structure
loop_material_scan = OperatorPOWL(operator=Operator.LOOP, children=[material_scan])
xor_expert_review = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
xor_database_search = OperatorPOWL(operator=Operator.XOR, children=[database_search, skip])
xor_legal_audit = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])
xor_cultural_assess = OperatorPOWL(operator=Operator.XOR, children=[cultural_assess, skip])
xor_data_synthesis = OperatorPOWL(operator=Operator.XOR, children=[data_synthesis, skip])
xor_report_draft = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
xor_archival_store = OperatorPOWL(operator=Operator.XOR, children=[archival_store, skip])
xor_display_approve = OperatorPOWL(operator=Operator.XOR, children=[display_approve, skip])
xor_lender_notify = OperatorPOWL(operator=Operator.XOR, children=[lender_notify, skip])
xor_investigation_flag = OperatorPOWL(operator=Operator.XOR, children=[investigation_flag, skip])

# Define root process tree
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    loop_material_scan,
    xor_expert_review,
    xor_database_search,
    xor_legal_audit,
    xor_cultural_assess,
    data_synthesis,
    xor_report_draft,
    xor_archival_store,
    xor_display_approve,
    xor_lender_notify,
    xor_investigation_flag
])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, loop_material_scan)
root.order.add_edge(loop_material_scan, xor_expert_review)
root.order.add_edge(xor_expert_review, xor_database_search)
root.order.add_edge(xor_database_search, xor_legal_audit)
root.order.add_edge(xor_legal_audit, xor_cultural_assess)
root.order.add_edge(xor_cultural_assess, data_synthesis)
root.order.add_edge(data_synthesis, xor_report_draft)
root.order.add_edge(xor_report_draft, xor_archival_store)
root.order.add_edge(xor_archival_store, xor_display_approve)
root.order.add_edge(xor_display_approve, xor_lender_notify)
root.order.add_edge(xor_lender_notify, xor_investigation_flag)