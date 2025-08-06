import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choices
visual_scan_choice = OperatorPOWL(operator=Operator.XOR, children=[visual_scan, skip])
material_test_choice = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])
radiocarbon_check_choice = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_check, skip])
provenance_search_choice = OperatorPOWL(operator=Operator.XOR, children=[provenance_search, skip])
archive_review_choice = OperatorPOWL(operator=Operator.XOR, children=[archive_review, skip])
expert_consult_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
microscope_exam_choice = OperatorPOWL(operator=Operator.XOR, children=[microscope_exam, skip])
infrared_scan_choice = OperatorPOWL(operator=Operator.XOR, children=[infrared_scan, skip])
legal_verify_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
condition_report_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
digital_catalog_choice = OperatorPOWL(operator=Operator.XOR, children=[digital_catalog, skip])
ownership_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, skip])
restoration_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, skip])

# Define loops
artifact_intake_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake])
visual_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[visual_scan_choice])
material_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test_choice])
radiocarbon_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_check_choice])
provenance_search_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_search_choice])
archive_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_review_choice])
expert_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult_choice])
microscope_exam_loop = OperatorPOWL(operator=Operator.LOOP, children=[microscope_exam_choice])
infrared_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[infrared_scan_choice])
legal_verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify_choice])
condition_report_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_report_choice])
digital_catalog_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_catalog_choice])
ownership_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit_choice])
restoration_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan_choice])

# Define partial order
root = StrictPartialOrder(nodes=[artifact_intake_loop, visual_scan_loop, material_test_loop, radiocarbon_check_loop, provenance_search_loop, archive_review_loop, expert_consult_loop, microscope_exam_loop, infrared_scan_loop, legal_verify_loop, condition_report_loop, digital_catalog_loop, ownership_audit_loop, restoration_plan_loop, final_approval, authentication_cert])

# Define dependencies
root.order.add_edge(artifact_intake_loop, visual_scan_loop)
root.order.add_edge(visual_scan_loop, material_test_loop)
root.order.add_edge(material_test_loop, radiocarbon_check_loop)
root.order.add_edge(radiocarbon_check_loop, provenance_search_loop)
root.order.add_edge(provenance_search_loop, archive_review_loop)
root.order.add_edge(archive_review_loop, expert_consult_loop)
root.order.add_edge(expert_consult_loop, microscope_exam_loop)
root.order.add_edge(microscope_exam_loop, infrared_scan_loop)
root.order.add_edge(infrared_scan_loop, legal_verify_loop)
root.order.add_edge(legal_verify_loop, condition_report_loop)
root.order.add_edge(condition_report_loop, digital_catalog_loop)
root.order.add_edge(digital_catalog_loop, ownership_audit_loop)
root.order.add_edge(ownership_audit_loop, restoration_plan_loop)
root.order.add_edge(restoration_plan_loop, final_approval)
root.order.add_edge(final_approval, authentication_cert)

# Print the POWL model
print(root)