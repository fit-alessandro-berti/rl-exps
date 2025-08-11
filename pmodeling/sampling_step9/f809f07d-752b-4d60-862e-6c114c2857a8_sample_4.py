import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_test = Transition(label='Material Test')
archive_search = Transition(label='Archive Search')
expert_review = Transition(label='Expert Review')
three_d_scanning = Transition(label='3D Scanning')
wear_analysis = Transition(label='Wear Analysis')
database_cross = Transition(label='Database Cross')
law_consult = Transition(label='Law Consult')
forgeries_detect = Transition(label='Forgery Detect')
certification = Transition(label='Certification')
document_prep = Transition(label='Document Prep')
client_brief = Transition(label='Client Brief')
secure_storage = Transition(label='Secure Storage')
risk_assessment = Transition(label='Risk Assessment')
final_approval = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_test])
xor_archive = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_review])
xor_3d = OperatorPOWL(operator=Operator.XOR, children=[three_d_scanning, wear_analysis])
xor_database = OperatorPOWL(operator=Operator.XOR, children=[database_cross, law_consult])
xor_forgeries = OperatorPOWL(operator=Operator.XOR, children=[forgeries_detect, risk_assessment])
xor_certification = OperatorPOWL(operator=Operator.XOR, children=[certification, document_prep])
xor_client_brief = OperatorPOWL(operator=Operator.XOR, children=[client_brief, secure_storage])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop_provenance, xor_archive, xor_3d, xor_database, xor_forgeries, xor_certification, xor_client_brief])
root.order.add_edge(loop_provenance, xor_archive)
root.order.add_edge(loop_provenance, xor_3d)
root.order.add_edge(loop_provenance, xor_database)
root.order.add_edge(loop_provenance, xor_forgeries)
root.order.add_edge(loop_provenance, xor_certification)
root.order.add_edge(loop_provenance, xor_client_brief)

# Print the root of the POWL model
print(root)