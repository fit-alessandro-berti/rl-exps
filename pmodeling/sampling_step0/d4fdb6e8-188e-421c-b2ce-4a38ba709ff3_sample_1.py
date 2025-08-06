import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
artifact_receipt = Transition(label='Artifact Receipt')
initial_inspection = Transition(label='Initial Inspection')
material_testing = Transition(label='Material Testing')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
database_search = Transition(label='Database Search')
expert_consult = Transition(label='Expert Consult')
legal_review = Transition(label='Legal Review')
cultural_audit = Transition(label='Cultural Audit')
condition_report = Transition(label='Condition Report')
risk_assessment = Transition(label='Risk Assessment')
insurance_setup = Transition(label='Insurance Setup')
transport_plan = Transition(label='Transport Plan')
final_certification = Transition(label='Final Certification')
archive_entry = Transition(label='Archive Entry')
publication_prep = Transition(label='Publication Prep')

# Define the loop nodes
material_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_testing])
database_search_loop = OperatorPOWL(operator=Operator.LOOP, children=[database_search])
risk_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assessment])

# Define the choice nodes
artifact_receipt_choice = OperatorPOWL(operator=Operator.XOR, children=[artifact_receipt, initial_inspection])
material_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[material_testing_loop, cultural_audit])
database_search_choice = OperatorPOWL(operator=Operator.XOR, children=[database_search_loop, expert_consult])
legal_review_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_review, condition_report])
risk_assessment_choice = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment_loop, transport_plan])
insurance_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, final_certification])
publication_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[publication_prep, archive_entry])

# Define the root node
root = StrictPartialOrder(nodes=[artifact_receipt_choice, material_testing_choice, database_search_choice, legal_review_choice, risk_assessment_choice, insurance_setup_choice, publication_prep_choice])
root.order.add_edge(artifact_receipt_choice, material_testing_choice)
root.order.add_edge(material_testing_choice, database_search_choice)
root.order.add_edge(database_search_choice, legal_review_choice)
root.order.add_edge(legal_review_choice, risk_assessment_choice)
root.order.add_edge(risk_assessment_choice, insurance_setup_choice)
root.order.add_edge(insurance_setup_choice, publication_prep_choice)