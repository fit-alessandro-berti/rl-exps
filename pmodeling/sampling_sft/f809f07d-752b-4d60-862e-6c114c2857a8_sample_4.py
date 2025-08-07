import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
provenance = Transition(label='Provenance Check')
material = Transition(label='Material Test')
archive = Transition(label='Archive Search')
expert = Transition(label='Expert Review')
risk = Transition(label='Risk Assessment')
db_cross = Transition(label='Database Cross')
law_consult = Transition(label='Law Consult')
forgery_detect = Transition(label='Forgery Detect')
final_approval = Transition(label='Final Approval')
3d_scan = Transition(label='3D Scanning')
wear = Transition(label='Wear Analysis')
certification = Transition(label='Certification')
doc_prep = Transition(label='Document Prep')
client_brief = Transition(label='Client Brief')
secure_storage = Transition(label='Secure Storage')

# Build the partial order
root = StrictPartialOrder(nodes=[
    provenance, material, archive, expert, risk,
    db_cross, law_consult, forgery_detect, final_approval,
    3d_scan, wear, certification, doc_prep, client_brief, secure_storage
])

# Define the control-flow dependencies
root.order.add_edge(provenance, material)
root.order.add_edge(provenance, archive)
root.order.add_edge(provenance, expert)
root.order.add_edge(provenance, risk)

root.order.add_edge(material, db_cross)
root.order.add_edge(archive, db_cross)
root.order.add_edge(expert, db_cross)
root.order.add_edge(risk, db_cross)

root.order.add_edge(db_cross, law_consult)
root.order.add_edge(law_consult, forgery_detect)

root.order.add_edge(forgery_detect, final_approval)

root.order.add_edge(3d_scan, wear)
root.order.add_edge(wear, certification)

root.order.add_edge(certification, doc_prep)
root.order.add_edge(doc_prep, client_brief)

root.order.add_edge(client_brief, secure_storage)

# Print the root model for verification
print(root)