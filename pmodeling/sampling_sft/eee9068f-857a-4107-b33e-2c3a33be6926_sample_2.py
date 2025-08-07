import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake     = Transition(label='Artifact Intake')
provenance_check    = Transition(label='Provenance Check')
archive_search      = Transition(label='Archive Search')
expert_interview    = Transition(label='Expert Interview')
material_scan       = Transition(label='Material Scan')
age_analysis        = Transition(label='Age Analysis')
stylistic_review    = Transition(label='Stylistic Review')
context_mapping     = Transition(label='Context Mapping')
legal_clearance     = Transition(label='Legal Clearance')
data_compilation    = Transition(label='Data Compilation')
report_drafting     = Transition(label='Report Drafting')
peer_review         = Transition(label='Peer Review')
final_assessment    = Transition(label='Final Assessment')
acquisition_plan    = Transition(label='Acquisition Plan')
restoration_prep    = Transition(label='Restoration Prep')
documentation       = Transition(label='Documentation')
data_backup         = Transition(label='Data Backup')

# Build the loop for iterative stylistic and context analysis
stylo_context_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[stylistic_review, context_mapping]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    archive_search,
    expert_interview,
    material_scan,
    age_analysis,
    stylo_context_loop,
    legal_clearance,
    data_compilation,
    report_drafting,
    peer_review,
    final_assessment,
    acquisition_plan,
    restoration_prep,
    documentation,
    data_backup
])

# Define the control-flow dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, archive_search)
root.order.add_edge(provenance_check, expert_interview)
root.order.add_edge(archive_search, stylo_context_loop)
root.order.add_edge(expert_interview, stylo_context_loop)
root.order.add_edge(stylo_context_loop, legal_clearance)
root.order.add_edge(legal_clearance, data_compilation)
root.order.add_edge(data_compilation, report_drafting)
root.order.add_edge(report_drafting, peer_review)
root.order.add_edge(peer_review, final_assessment)
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(acquisition_plan, restoration_prep)
root.order.add_edge(acquisition_plan, documentation)
root.order.add_edge(acquisition_plan, data_backup)