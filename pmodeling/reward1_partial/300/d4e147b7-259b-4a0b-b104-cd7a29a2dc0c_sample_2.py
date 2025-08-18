import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
visual_scan = Transition(label='Visual Scan')
material_test = Transition(label='Material Test')
radiocarbon_check = Transition(label='Radiocarbon Check')
provenance_search = Transition(label='Provenance Search')
archive_review = Transition(label='Archive Review')
expert_consult = Transition(label='Expert Consult')
microscope_exam = Transition(label='Microscope Exam')
infrared_scan = Transition(label='Infrared Scan')
legal_verify = Transition(label='Legal Verify')
condition_report = Transition(label='Condition Report')
digital_catalog = Transition(label='Digital Catalog')
ownership_audit = Transition(label='Ownership Audit')
restoration_plan = Transition(label='Restoration Plan')
final_approval = Transition(label='Final Approval')
authentication_cert = Transition(label='Authentication Cert')

# Define transitions for silent activities (tau labels)
skip = SilentTransition()

# Define POWL models
visual_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[visual_scan])
material_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test])
radiocarbon_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_check])
provenance_search_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_search])
archive_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_review])
expert_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult])
microscope_exam_loop = OperatorPOWL(operator=Operator.LOOP, children=[microscope_exam])
infrared_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[infrared_scan])
legal_verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify])
condition_report_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_report])
digital_catalog_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_catalog])
ownership_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit])
restoration_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan])

# Define partial order and dependencies
root = StrictPartialOrder(nodes=[
    artifact_intake, visual_scan_loop, material_test_loop, radiocarbon_check_loop, provenance_search_loop,
    archive_review_loop, expert_consult_loop, microscope_exam_loop, infrared_scan_loop, legal_verify_loop,
    condition_report_loop, digital_catalog_loop, ownership_audit_loop, restoration_plan_loop,
    final_approval, authentication_cert
])

# Add dependencies between activities
root.order.add_edge(artifact_intake, visual_scan_loop)
root.order.add_edge(artifact_intake, material_test_loop)
root.order.add_edge(artifact_intake, radiocarbon_check_loop)
root.order.add_edge(artifact_intake, provenance_search_loop)
root.order.add_edge(artifact_intake, archive_review_loop)
root.order.add_edge(artifact_intake, expert_consult_loop)
root.order.add_edge(artifact_intake, microscope_exam_loop)
root.order.add_edge(artifact_intake, infrared_scan_loop)
root.order.add_edge(artifact_intake, legal_verify_loop)
root.order.add_edge(artifact_intake, condition_report_loop)
root.order.add_edge(artifact_intake, digital_catalog_loop)
root.order.add_edge(artifact_intake, ownership_audit_loop)
root.order.add_edge(artifact_intake, restoration_plan_loop)
root.order.add_edge(visual_scan_loop, final_approval)
root.order.add_edge(material_test_loop, final_approval)
root.order.add_edge(radiocarbon_check_loop, final_approval)
root.order.add_edge(provenance_search_loop, final_approval)
root.order.add_edge(archive_review_loop, final_approval)
root.order.add_edge(expert_consult_loop, final_approval)
root.order.add_edge(microscope_exam_loop, final_approval)
root.order.add_edge(infrared_scan_loop, final_approval)
root.order.add_edge(legal_verify_loop, final_approval)
root.order.add_edge(condition_report_loop, final_approval)
root.order.add_edge(digital_catalog_loop, final_approval)
root.order.add_edge(ownership_audit_loop, final_approval)
root.order.add_edge(restoration_plan_loop, final_approval)
root.order.add_edge(final_approval, authentication_cert)

# Print the POWL model
print(root)