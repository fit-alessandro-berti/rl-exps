from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the structure of the POWL model
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_test,
    archive_search,
    expert_review,
    three_d_scanning,
    wear_analysis,
    database_cross,
    law_consult,
    forgeries_detect,
    certification,
    document_prep,
    client_brief,
    secure_storage,
    risk_assessment,
    final_approval
])

# Add dependencies between nodes
root.order.add_edge(provenance_check, material_test)
root.order.add_edge(provenance_check, archive_search)
root.order.add_edge(provenance_check, expert_review)
root.order.add_edge(material_test, wear_analysis)
root.order.add_edge(archive_search, wear_analysis)
root.order.add_edge(expert_review, wear_analysis)
root.order.add_edge(wear_analysis, database_cross)
root.order.add_edge(database_cross, forgeries_detect)
root.order.add_edge(forgeries_detect, certification)
root.order.add_edge(certification, document_prep)
root.order.add_edge(document_prep, client_brief)
root.order.add_edge(client_brief, secure_storage)
root.order.add_edge(secure_storage, risk_assessment)
root.order.add_edge(risk_assessment, final_approval)

# Print the final POWL model
print(root)