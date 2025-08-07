import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
artifact_receipt      = Transition(label='Artifact Receipt')
initial_inspection    = Transition(label='Initial Inspection')
material_testing      = Transition(label='Material Testing')
provenance_check      = Transition(label='Provenance Check')
digital_imaging       = Transition(label='Digital Imaging')
database_search       = Transition(label='Database Search')
expert_consult        = Transition(label='Expert Consult')
legal_review          = Transition(label='Legal Review')
cultural_audit        = Transition(label='Cultural Audit')
condition_report      = Transition(label='Condition Report')
risk_assessment       = Transition(label='Risk Assessment')
insurance_setup       = Transition(label='Insurance Setup')
transport_plan        = Transition(label='Transport Plan')
final_certification   = Transition(label='Final Certification')
archive_entry         = Transition(label='Archive Entry')
publication_prep      = Transition(label='Publication Prep')

# Build the loop for expert consultations: repeat Expert Consult then optionally Legal Review
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert_consult, legal_review]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    artifact_receipt,
    initial_inspection,
    material_testing,
    provenance_check,
    digital_imaging,
    database_search,
    expert_loop,
    cultural_audit,
    condition_report,
    risk_assessment,
    insurance_setup,
    transport_plan,
    final_certification,
    archive_entry,
    publication_prep
])

# Define the control-flow edges
root.order.add_edge(artifact_receipt, initial_inspection)
root.order.add_edge(initial_inspection, material_testing)
root.order.add_edge(material_testing, provenance_check)
root.order.add_edge(provenance_check, digital_imaging)
root.order.add_edge(digital_imaging, database_search)
root.order.add_edge(database_search, expert_loop)
root.order.add_edge(expert_loop, cultural_audit)
root.order.add_edge(cultural_audit, condition_report)
root.order.add_edge(condition_report, risk_assessment)
root.order.add_edge(risk_assessment, insurance_setup)
root.order.add_edge(insurance_setup, transport_plan)
root.order.add_edge(transport_plan, final_certification)
root.order.add_edge(final_certification, archive_entry)
root.order.add_edge(archive_entry, publication_prep)