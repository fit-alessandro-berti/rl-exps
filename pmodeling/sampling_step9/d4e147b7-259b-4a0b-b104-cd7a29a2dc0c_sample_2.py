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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, visual_scan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, radiocarbon_check])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_search, archive_review])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, microscope_exam])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[infrared_scan, legal_verify])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, digital_catalog])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit, restoration_plan])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, authentication_cert])

# Define exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[loop8, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)