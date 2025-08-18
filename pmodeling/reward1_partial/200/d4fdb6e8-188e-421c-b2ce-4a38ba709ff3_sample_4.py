from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the partial order
root = StrictPartialOrder(
    nodes=[artifact_receipt, initial_inspection, material_testing, provenance_check, digital_imaging, database_search,
           expert_consult, legal_review, cultural_audit, condition_report, risk_assessment, insurance_setup,
           transport_plan, final_certification, archive_entry, publication_prep],
    order={
        artifact_receipt: initial_inspection,
        initial_inspection: material_testing,
        initial_inspection: provenance_check,
        material_testing: digital_imaging,
        provenance_check: database_search,
        digital_imaging: expert_consult,
        database_search: legal_review,
        expert_consult: cultural_audit,
        legal_review: condition_report,
        cultural_audit: risk_assessment,
        condition_report: insurance_setup,
        insurance_setup: transport_plan,
        transport_plan: final_certification,
        final_certification: archive_entry,
        archive_entry: publication_prep
    }
)

# Ensure all nodes are connected to the root
for node in root.nodes:
    if node not in root.order:
        root.order[node] = root.nodes[0]

# Ensure the root node is the first node in the order
root.order = {root.nodes[0]: root.nodes[0]} | root.order<|fim_middle|>