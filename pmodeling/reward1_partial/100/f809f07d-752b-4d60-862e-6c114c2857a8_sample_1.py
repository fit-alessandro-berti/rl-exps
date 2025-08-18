import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the workflow steps
provenance_check_then_material_test = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_test])
archive_search_then_expert_review = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_review])
three_d_scanning_then_wear_analysis = OperatorPOWL(operator=Operator.XOR, children=[three_d_scanning, wear_analysis])
database_cross_then_law_consult = OperatorPOWL(operator=Operator.XOR, children=[database_cross, law_consult])
forgeries_detect_then_certification = OperatorPOWL(operator=Operator.XOR, children=[forgeries_detect, certification])
document_prep_then_client_brief = OperatorPOWL(operator=Operator.XOR, children=[document_prep, client_brief])
secure_storage_then_final_approval = OperatorPOWL(operator=Operator.XOR, children=[secure_storage, final_approval])

# Define the loop for the core process
core_process = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check_then_material_test,
                                                              archive_search_then_expert_review,
                                                              three_d_scanning_then_wear_analysis,
                                                              database_cross_then_law_consult,
                                                              forgeries_detect_then_certification,
                                                              document_prep_then_client_brief,
                                                              secure_storage_then_final_approval])

# Define the partial order
root = StrictPartialOrder(nodes=[core_process, risk_assessment])

# Define the dependencies
root.order.add_edge(core_process, risk_assessment)

# Print the result
print(root)