import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loop node for provenance search
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_review, expert_consult])

# Define exclusive choice for legal verification
legal_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])

# Define exclusive choice for visual scan and material test
visual_material_choice = OperatorPOWL(operator=Operator.XOR, children=[visual_scan, material_test])

# Define exclusive choice for radiocarbon check and provenance loop
radiocarbon_provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_check, provenance_loop])

# Define exclusive choice for microscope exam and infrared scan
microscope_infrared_choice = OperatorPOWL(operator=Operator.XOR, children=[microscope_exam, infrared_scan])

# Define exclusive choice for condition report and digital catalog
condition_catalog_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_report, digital_catalog])

# Define exclusive choice for ownership audit and restoration plan
ownership_restoration_choice = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, restoration_plan])

# Define exclusive choice for final approval and authentication cert
final_approval_choice = OperatorPOWL(operator=Operator.XOR, children=[final_approval, authentication_cert])

# Define root node with all activities and choices
root = StrictPartialOrder(nodes=[artifact_intake, visual_material_choice, radiocarbon_provenance_choice, microscope_infrared_choice, condition_catalog_choice, ownership_restoration_choice, legal_choice, final_approval_choice, authentication_cert])
root.order.add_edge(artifact_intake, visual_material_choice)
root.order.add_edge(artifact_intake, radiocarbon_provenance_choice)
root.order.add_edge(artifact_intake, microscope_infrared_choice)
root.order.add_edge(artifact_intake, condition_catalog_choice)
root.order.add_edge(artifact_intake, ownership_restoration_choice)
root.order.add_edge(artifact_intake, legal_choice)
root.order.add_edge(artifact_intake, final_approval_choice)
root.order.add_edge(artifact_intake, authentication_cert)
root.order.add_edge(visual_material_choice, radiocarbon_provenance_choice)
root.order.add_edge(radiocarbon_provenance_choice, microscope_infrared_choice)
root.order.add_edge(radiocarbon_provenance_choice, condition_catalog_choice)
root.order.add_edge(radiocarbon_provenance_choice, ownership_restoration_choice)
root.order.add_edge(radiocarbon_provenance_choice, legal_choice)
root.order.add_edge(radiocarbon_provenance_choice, final_approval_choice)
root.order.add_edge(radiocarbon_provenance_choice, authentication_cert)
root.order.add_edge(microscope_infrared_choice, condition_catalog_choice)
root.order.add_edge(microscope_infrared_choice, ownership_restoration_choice)
root.order.add_edge(microscope_infrared_choice, legal_choice)
root.order.add_edge(microscope_infrared_choice, final_approval_choice)
root.order.add_edge(microscope_infrared_choice, authentication_cert)
root.order.add_edge(condition_catalog_choice, ownership_restoration_choice)
root.order.add_edge(condition_catalog_choice, legal_choice)
root.order.add_edge(condition_catalog_choice, final_approval_choice)
root.order.add_edge(condition_catalog_choice, authentication_cert)
root.order.add_edge(ownership_restoration_choice, legal_choice)
root.order.add_edge(ownership_restoration_choice, final_approval_choice)
root.order.add_edge(ownership_restoration_choice, authentication_cert)
root.order.add_edge(legal_choice, final_approval_choice)
root.order.add_edge(legal_choice, authentication_cert)
root.order.add_edge(final_approval_choice, authentication_cert)

print(root)