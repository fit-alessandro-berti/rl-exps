import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
provenance_check    = Transition(label='Provenance Check')
material_test       = Transition(label='Material Test')
archive_search      = Transition(label='Archive Search')
expert_review       = Transition(label='Expert Review')
database_cross      = Transition(label='Database Cross')
law_consult         = Transition(label='Law Consult')
forgeries_detect    = Transition(label='Forgery Detect')
wear_analysis       = Transition(label='Wear Analysis')
3d_scanning         = Transition(label='3D Scanning')
certification       = Transition(label='Certification')
document_prep       = Transition(label='Document Prep')
client_brief        = Transition(label='Client Brief')
secure_storage      = Transition(label='Secure Storage')
final_approval      = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    provenance_check, material_test, archive_search, expert_review,
    database_cross, law_consult, forgeries_detect, wear_analysis,
    3d_scanning, certification, document_prep, client_brief,
    secure_storage, final_approval
])

# Define the control-flow dependencies
root.order.add_edge(provenance_check, material_test)
root.order.add_edge(provenance_check, archive_search)
root.order.add_edge(provenance_check, expert_review)

root.order.add_edge(material_test, database_cross)
root.order.add_edge(material_test, forgeries_detect)

root.order.add_edge(archive_search, database_cross)
root.order.add_edge(archive_search, forgeries_detect)

root.order.add_edge(expert_review, database_cross)
root.order.add_edge(expert_review, forgeries_detect)

root.order.add_edge(database_cross, wear_analysis)
root.order.add_edge(forgeries_detect, wear_analysis)

root.order.add_edge(wear_analysis, 3d_scanning)

root.order.add_edge(3d_scanning, certification)

root.order.add_edge(certification, document_prep)
root.order.add_edge(certification, client_brief)

root.order.add_edge(document_prep, secure_storage)
root.order.add_edge(client_brief, secure_storage)

root.order.add_edge(secure_storage, final_approval)