import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, archive_search, expert_review])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, three_d_scanning, wear_analysis])
database_loop = OperatorPOWL(operator=Operator.LOOP, children=[database_cross, law_consult, forgeries_detect])
final_loop = OperatorPOWL(operator=Operator.LOOP, children=[certification, document_prep, client_brief, secure_storage, risk_assessment, final_approval])

# Define the XOR choice between two loops
xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, material_loop, database_loop, final_loop])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(provenance_loop, xor)
root.order.add_edge(material_loop, xor)
root.order.add_edge(database_loop, xor)
root.order.add_edge(final_loop, xor)

# Print the root POWL model
print(root)