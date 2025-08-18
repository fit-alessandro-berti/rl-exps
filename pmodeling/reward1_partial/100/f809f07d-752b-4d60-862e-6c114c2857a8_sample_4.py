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
forger_detect = Transition(label='Forgery Detect')
certification = Transition(label='Certification')
document_prep = Transition(label='Document Prep')
client_brief = Transition(label='Client Brief')
secure_storage = Transition(label='Secure Storage')
risk_assessment = Transition(label='Risk Assessment')
final_approval = Transition(label='Final Approval')

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()

# Define the POWL model structure
# Provenance Check -> Material Test -> Archive Search -> Expert Review
provenance_check_to_material_test = OperatorPOWL(operator=Operator.PO, children=[provenance_check, material_test])
material_test_to_archive_search = OperatorPOWL(operator=Operator.PO, children=[material_test, archive_search])
archive_search_to_expert_review = OperatorPOWL(operator=Operator.PO, children=[archive_search, expert_review])

# Archive Search -> Law Consult -> Forger Detect
archive_search_to_law_consult = OperatorPOWL(operator=Operator.PO, children=[archive_search, law_consult])
law_consult_to_forger_detect = OperatorPOWL(operator=Operator.PO, children=[law_consult, forger_detect])

# Expert Review -> Database Cross -> Wear Analysis
expert_review_to_database_cross = OperatorPOWL(operator=Operator.PO, children=[expert_review, database_cross])
database_cross_to_wear_analysis = OperatorPOWL(operator=Operator.PO, children=[database_cross, wear_analysis])

# Database Cross -> Law Consult -> Forger Detect
database_cross_to_law_consult = OperatorPOWL(operator=Operator.PO, children=[database_cross, law_consult])
law_consult_to_forger_detect = OperatorPOWL(operator=Operator.PO, children=[law_consult, forger_detect])

# Forger Detect -> Law Consult -> Forger Detect (loop)
forger_detect_to_law_consult = OperatorPOWL(operator=Operator.PO, children=[forger_detect, law_consult])
law_consult_to_forger_detect_loop = OperatorPOWL(operator=Operator.LOOP, children=[law_consult, forger_detect])

# Law Consult -> Risk Assessment -> Final Approval
law_consult_to_risk_assessment = OperatorPOWL(operator=Operator.PO, children=[law_consult, risk_assessment])
risk_assessment_to_final_approval = OperatorPOWL(operator=Operator.PO, children=[risk_assessment, final_approval])

# Forger Detect -> Law Consult -> Forger Detect (loop) -> Risk Assessment -> Final Approval
forger_detect_to_law_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[forger_detect, law_consult])
law_consult_to_risk_assessment_loop = OperatorPOWL(operator=Operator.PO, children=[law_consult, risk_assessment])
risk_assessment_to_final_approval_loop = OperatorPOWL(operator=Operator.PO, children=[risk_assessment, final_approval])

# Define the StrictPartialOrder for the root
root = StrictPartialOrder(nodes=[
    provenance_check_to_material_test,
    material_test_to_archive_search,
    archive_search_to_expert_review,
    archive_search_to_law_consult,
    expert_review_to_database_cross,
    database_cross_to_wear_analysis,
    database_cross_to_law_consult,
    forger_detect_to_law_consult,
    law_consult_to_risk_assessment,
    risk_assessment_to_final_approval,
    forger_detect_to_law_consult_loop,
    law_consult_to_risk_assessment_loop,
    risk_assessment_to_final_approval_loop
])

# Add edges between nodes
root.order.add_edge(provenance_check_to_material_test, material_test_to_archive_search)
root.order.add_edge(material_test_to_archive_search, archive_search_to_expert_review)
root.order.add_edge(archive_search_to_law_consult, law_consult_to_forger_detect)
root.order.add_edge(expert_review_to_database_cross, database_cross_to_wear_analysis)
root.order.add_edge(database_cross_to_law_consult, law_consult_to_forger_detect)
root.order.add_edge(forger_detect_to_law_consult, law_consult_to_risk_assessment)
root.order.add_edge(law_consult_to_risk_assessment, risk_assessment_to_final_approval)
root.order.add_edge(forger_detect_to_law_consult_loop, law_consult_to_risk_assessment_loop)
root.order.add_edge(law_consult_to_risk_assessment_loop, risk_assessment_to_final_approval_loop)

# Print the root POWL model
print(root)