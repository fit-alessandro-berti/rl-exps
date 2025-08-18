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

# Define loop for legal verify and ownership audit
legal_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, ownership_audit])

# Define XOR for material test and visual scan
xor = OperatorPOWL(operator=Operator.XOR, children=[material_test, visual_scan])

# Define XOR for microscope exam and infrared scan
xor2 = OperatorPOWL(operator=Operator.XOR, children=[microscope_exam, infrared_scan])

# Define XOR for condition report and digital catalog
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, digital_catalog])

# Define XOR for restoration plan and final approval
xor4 = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, final_approval])

# Define root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, radiocarbon_check, provenance_search, archive_review, expert_consult, xor, xor2, xor3, xor4, legal_audit_loop, authentication_cert])
root.order.add_edge(artifact_intake, radiocarbon_check)
root.order.add_edge(artifact_intake, provenance_search)
root.order.add_edge(artifact_intake, archive_review)
root.order.add_edge(artifact_intake, expert_consult)
root.order.add_edge(radiocarbon_check, provenance_search)
root.order.add_edge(provenance_search, archive_review)
root.order.add_edge(archive_review, expert_consult)
root.order.add_edge(expert_consult, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, legal_audit_loop)
root.order.add_edge(legal_audit_loop, authentication_cert)