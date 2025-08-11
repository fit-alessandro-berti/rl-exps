import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Provenance Check -> Material Test
provenance_to_material = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_test])

# Material Test -> Archive Search
material_to_archive = OperatorPOWL(operator=Operator.XOR, children=[material_test, archive_search])

# Archive Search -> Expert Review
archive_to_expert = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_review])

# Expert Review -> 3D Scanning
expert_to_3d = OperatorPOWL(operator=Operator.XOR, children=[expert_review, three_d_scanning])

# 3D Scanning -> Wear Analysis
three_d_to_wear = OperatorPOWL(operator=Operator.XOR, children=[three_d_scanning, wear_analysis])

# Wear Analysis -> Database Cross
wear_to_database = OperatorPOWL(operator=Operator.XOR, children=[wear_analysis, database_cross])

# Database Cross -> Law Consult
database_to_law = OperatorPOWL(operator=Operator.XOR, children=[database_cross, law_consult])

# Law Consult -> Forgeries Detect
law_to_forgeries = OperatorPOWL(operator=Operator.XOR, children=[law_consult, forgeries_detect])

# Forgeries Detect -> Certification
forgeries_to_cert = OperatorPOWL(operator=Operator.XOR, children=[forgeries_detect, certification])

# Certification -> Document Prep
cert_to_document = OperatorPOWL(operator=Operator.XOR, children=[certification, document_prep])

# Document Prep -> Client Brief
document_to_client = OperatorPOWL(operator=Operator.XOR, children=[document_prep, client_brief])

# Client Brief -> Secure Storage
client_to_secure = OperatorPOWL(operator=Operator.XOR, children=[client_brief, secure_storage])

# Secure Storage -> Risk Assessment
secure_to_risk = OperatorPOWL(operator=Operator.XOR, children=[secure_storage, risk_assessment])

# Risk Assessment -> Final Approval
risk_to_final = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, final_approval])

# Connect the nodes
root = StrictPartialOrder(nodes=[provenance_to_material, material_to_archive, archive_to_expert, expert_to_3d, three_d_to_wear, wear_to_database, database_to_law, law_to_forgeries, forgeries_to_cert, cert_to_document, document_to_client, client_to_secure, secure_to_risk, risk_to_final])
root.order.add_edge(provenance_to_material, material_to_archive)
root.order.add_edge(material_to_archive, archive_to_expert)
root.order.add_edge(archive_to_expert, expert_to_3d)
root.order.add_edge(expert_to_3d, three_d_to_wear)
root.order.add_edge(three_d_to_wear, wear_to_database)
root.order.add_edge(wear_to_database, database_to_law)
root.order.add_edge(database_to_law, law_to_forgeries)
root.order.add_edge(law_to_forgeries, forgeries_to_cert)
root.order.add_edge(forgeries_to_cert, cert_to_document)
root.order.add_edge(cert_to_document, document_to_client)
root.order.add_edge(document_to_client, client_to_secure)
root.order.add_edge(client_to_secure, secure_to_risk)
root.order.add_edge(secure_to_risk, risk_to_final)

print(root)