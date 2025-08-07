import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
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

# Define the partial order (POWL model)
root = StrictPartialOrder(nodes=[
    collection_survey,
    provenance_check,
    legal_review,
    scientific_test,
    material_analysis,
    ownership_audit,
    ethical_screening,
    condition_report,
    expert_consultation,
    transport_planning,
    secure_packing,
    customs_clearance,
    insurance_setup,
    exhibit_preparation,
    final_approval
])

# Add dependencies (if any) between the activities
# For example, if certain activities must be completed before others, add dependencies here
# root.order.add_edge(collection_survey, provenance_check)
# root.order.add_edge(collection_survey, legal_review)
# root.order.add_edge(collection_survey, scientific_test)
# root.order.add_edge(collection_survey, material_analysis)
# root.order.add_edge(collection_survey, ownership_audit)
# root.order.add_edge(collection_survey, ethical_screening)
# root.order.add_edge(collection_survey, condition_report)
# root.order.add_edge(collection_survey, expert_consultation)
# root.order.add_edge(collection_survey, transport_planning)
# root.order.add_edge(collection_survey, secure_packing)
# root.order.add_edge(collection_survey, customs_clearance)
# root.order.add_edge(collection_survey, insurance_setup)
# root.order.add_edge(collection_survey, exhibit_preparation)
# root.order.add_edge(collection_survey, final_approval)

# Print the final POWL model
print(root)