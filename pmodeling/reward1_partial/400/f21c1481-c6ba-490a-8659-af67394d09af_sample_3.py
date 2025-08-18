import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
collection_survey = Transition(label='Collection Survey')
provenance_check = Transition(label='Provenance Check')
legal_review = Transition(label='Legal Review')
scientific_test = Transition(label='Scientific Test')
material_analysis = Transition(label='Material Analysis')
ownership_audit = Transition(label='Ownership Audit')
ethical_screening = Transition(label='Ethical Screening')
condition_report = Transition(label='Condition Report')
expert_consultation = Transition(label='Expert Consultation')
transport_planning = Transition(label='Transport Planning')
secure_packing = Transition(label='Secure Packing')
customs_clearance = Transition(label='Customs Clearance')
insurance_setup = Transition(label='Insurance Setup')
exhibit_preparation = Transition(label='Exhibit Preparation')
final_approval = Transition(label='Final Approval')

# Define loops and XORs for the process
collection_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[collection_survey, provenance_check, legal_review])
scientific_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[scientific_test, material_analysis])
ownership_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit, ethical_screening, condition_report, expert_consultation])
transport_planning_loop = OperatorPOWL(operator=Operator.LOOP, children=[transport_planning, secure_packing, customs_clearance, insurance_setup])
exhibit_preparation_loop = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_preparation, final_approval])

# Define partial order
root = StrictPartialOrder(nodes=[collection_survey_loop, scientific_test_loop, ownership_audit_loop, transport_planning_loop, exhibit_preparation_loop])
root.order.add_edge(collection_survey_loop, scientific_test_loop)
root.order.add_edge(scientific_test_loop, ownership_audit_loop)
root.order.add_edge(ownership_audit_loop, transport_planning_loop)
root.order.add_edge(transport_planning_loop, exhibit_preparation_loop)