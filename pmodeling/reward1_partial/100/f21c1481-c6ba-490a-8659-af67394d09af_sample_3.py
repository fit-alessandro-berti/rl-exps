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

# Define the partial order structure
root = StrictPartialOrder(nodes=[collection_survey, provenance_check, legal_review, scientific_test, material_analysis, ownership_audit, ethical_screening, condition_report, expert_consultation, transport_planning, secure_packing, customs_clearance, insurance_setup, exhibit_preparation, final_approval])

# Define the dependencies between activities
root.order.add_edge(collection_survey, provenance_check)
root.order.add_edge(collection_survey, legal_review)
root.order.add_edge(provenance_check, scientific_test)
root.order.add_edge(provenance_check, material_analysis)
root.order.add_edge(legal_review, ownership_audit)
root.order.add_edge(legal_review, ethical_screening)
root.order.add_edge(scientific_test, condition_report)
root.order.add_edge(material_analysis, condition_report)
root.order.add_edge(ownership_audit, expert_consultation)
root.order.add_edge(ethical_screening, expert_consultation)
root.order.add_edge(condition_report, transport_planning)
root.order.add_edge(condition_report, customs_clearance)
root.order.add_edge(condition_report, insurance_setup)
root.order.add_edge(expert_consultation, exhibit_preparation)
root.order.add_edge(exhibit_preparation, final_approval)

# Print the root POWL model
print(root)