import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control-flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[
    initial_inspection,
    material_testing,
    provenance_check,
    digital_imaging,
    database_search,
    expert_consult,
    legal_review,
    cultural_audit,
    condition_report,
    risk_assessment,
    insurance_setup,
    transport_plan
])

exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[
    final_certification,
    archive_entry,
    publication_prep
])

loop = OperatorPOWL(operator=Operator.LOOP, children=[
    exclusive_choice,
    exclusive_choice2
])

# Define the partial order
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, exclusive_choice)
root.order.add_edge(loop, exclusive_choice2)

# Print the root of the POWL model
print(root)