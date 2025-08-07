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

# Define the partial order with dependencies
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

# Define dependencies if any (for example, collection_survey must be done before provenance_check)
root.order.add_edge(collection_survey, provenance_check)
# Add more dependencies as needed

# The root variable now holds the POWL model for the described process