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

# Define the process steps
provenance_check_node = OperatorPOWL(operator=Operator.AND, children=[provenance_check, material_test])
archive_search_node = OperatorPOWL(operator=Operator.AND, children=[archive_search, expert_review])
database_cross_node = OperatorPOWL(operator=Operator.AND, children=[database_cross, law_consult])
forgeries_detect_node = OperatorPOWL(operator=Operator.AND, children=[forgeries_detect, risk_assessment])
document_prep_node = OperatorPOWL(operator=Operator.AND, children=[document_prep, client_brief])
secure_storage_node = OperatorPOWL(operator=Operator.AND, children=[secure_storage, final_approval])

# Define the partial order
root = StrictPartialOrder(nodes=[
    provenance_check_node,
    archive_search_node,
    database_cross_node,
    forgeries_detect_node,
    document_prep_node,
    secure_storage_node
])

# Define the partial order edges
root.order.add_edge(provenance_check_node, archive_search_node)
root.order.add_edge(archive_search_node, database_cross_node)
root.order.add_edge(database_cross_node, forgeries_detect_node)
root.order.add_edge(forgeries_detect_node, document_prep_node)
root.order.add_edge(document_prep_node, secure_storage_node)