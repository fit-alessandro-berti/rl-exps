import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the loop nodes (repeated actions)
collection_loop = OperatorPOWL(operator=Operator.LOOP, children=[collection_survey, provenance_check, legal_review, scientific_test, material_analysis, ownership_audit, ethical_screening, condition_report, expert_consultation, transport_planning, secure_packing, customs_clearance, insurance_setup, exhibit_preparation, final_approval])

# Define the partial order
root = StrictPartialOrder(nodes=[collection_loop])

# Add the edges for the partial order
root.order.add_edge(collection_loop, collection_loop)

print(root)