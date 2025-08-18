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

# Define the partial order
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

# Define dependencies between activities
root.order.add_edge(collection_survey, provenance_check)
root.order.add_edge(provenance_check, legal_review)
root.order.add_edge(legal_review, scientific_test)
root.order.add_edge(scientific_test, material_analysis)
root.order.add_edge(material_analysis, ownership_audit)
root.order.add_edge(ownership_audit, ethical_screening)
root.order.add_edge(ethical_screening, condition_report)
root.order.add_edge(condition_report, expert_consultation)
root.order.add_edge(expert_consultation, transport_planning)
root.order.add_edge(transport_planning, secure_packing)
root.order.add_edge(secure_packing, customs_clearance)
root.order.add_edge(customs_clearance, insurance_setup)
root.order.add_edge(insurance_setup, exhibit_preparation)
root.order.add_edge(exhibit_preparation, final_approval)

# Save the final result in the variable 'root'