import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Artifact Intake', 'Visual Scan', 'Material Test', 'Radiocarbon Check', 'Provenance Search', 'Archive Review', 'Expert Consult', 'Microscope Exam', 'Infrared Scan', 'Legal Verify', 'Condition Report', 'Digital Catalog', 'Ownership Audit', 'Restoration Plan', 'Final Approval', 'Authentication Cert']

# Create the POWL model
root = StrictPartialOrder()

# Define the nodes and transitions
for activity in activities:
    root.nodes.append(Transition(label=activity))

# Define the loops and choices
artifact_intake = root.nodes[0]
visual_scan = root.nodes[1]
material_test = root.nodes[2]
radiocarbon_check = root.nodes[3]
provenance_search = root.nodes[4]
archive_review = root.nodes[5]
expert_consult = root.nodes[6]
microscope_exam = root.nodes[7]
infrared_scan = root.nodes[8]
legal_verify = root.nodes[9]
condition_report = root.nodes[10]
digital_catalog = root.nodes[11]
ownership_audit = root.nodes[12]
restoration_plan = root.nodes[13]
final_approval = root.nodes[14]
authentication_cert = root.nodes[15]

# Define the loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[visual_scan, material_test, radiocarbon_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_search, archive_review, expert_consult])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[microscope_exam, infrared_scan, legal_verify])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, digital_catalog, ownership_audit])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan, final_approval, authentication_cert])

# Define the choices
choice1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, artifact_intake])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, choice1])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, choice2])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, choice3])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, choice4])

# Add the nodes and transitions to the POWL model
root.nodes.extend([loop1, loop2, loop3, loop4, loop5, choice1, choice2, choice3, choice4, choice5])
root.order.add_edge(artifact_intake, choice1)
root.order.add_edge(choice1, loop1)
root.order.add_edge(choice1, choice2)
root.order.add_edge(choice2, loop2)
root.order.add_edge(choice2, choice3)
root.order.add_edge(choice3, loop3)
root.order.add_edge(choice3, choice4)
root.order.add_edge(choice4, loop4)
root.order.add_edge(choice4, choice5)
root.order.add_edge(choice5, loop5)
root.order.add_edge(choice5, authentication_cert)

# Return the root node
return root