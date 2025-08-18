from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the relationships between activities
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, radiocarbon_check, provenance_search, expert_consult, microscope_exam, infrared_scan, legal_verify])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, digital_catalog, ownership_audit, restoration_plan])
xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval, authentication_cert])

# Create the partial order
root = StrictPartialOrder(nodes=[artifact_intake, visual_scan, loop1, loop2, xor])
root.order.add_edge(artifact_intake, visual_scan)
root.order.add_edge(artifact_intake, loop1)
root.order.add_edge(artifact_intake, loop2)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)

print(root)