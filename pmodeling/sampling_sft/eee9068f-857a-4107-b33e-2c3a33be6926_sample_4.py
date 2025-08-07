import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake      = Transition(label='Artifact Intake')
provenance_check     = Transition(label='Provenance Check')
archive_search       = Transition(label='Archive Search')
expert_interview     = Transition(label='Expert Interview')
material_scan        = Transition(label='Material Scan')
age_analysis         = Transition(label='Age Analysis')
stylistic_review     = Transition(label='Stylistic Review')
context_mapping      = Transition(label='Context Mapping')
legal_clearance      = Transition(label='Legal Clearance')
data_compilation     = Transition(label='Data Compilation')
report_drafting      = Transition(label='Report Drafting')
peer_review          = Transition(label='Peer Review')
final_assessment     = Transition(label='Final Assessment')
acquisition_plan     = Transition(label='Acquisition Plan')
restoration_prep     = Transition(label='Restoration Prep')
documentation        = Transition(label='Documentation')
data_backup          = Transition(label='Data Backup')

# Build the loop body: Material Scan -> Age Analysis -> Stylistic Review -> Context Mapping
body_loop = StrictPartialOrder(nodes=[material_scan, age_analysis, stylistic_review, context_mapping])
body_loop.order.add_edge(material_scan, age_analysis)
body_loop.order.add_edge(age_analysis, stylistic_review)
body_loop.order.add_edge(stylistic_review, context_mapping)

# LOOP operator: do the body, then optionally repeat the body
loop = OperatorPOWL(operator=Operator.LOOP, children=[body_loop, body_loop])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    archive_search,
    expert_interview,
    legal_clearance,
    loop,
    data_compilation,
    report_drafting,
    peer_review,
    final_assessment,
    acquisition_plan,
    restoration_prep,
    documentation,
    data_backup
])

# Control‐flow edges
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, archive_search)
root.order.add_edge(provenance_check, expert_interview)
root.order.add_edge(archive_search, legal_clearance)
root.order.add_edge(expert_interview, legal_clearance)
root.order.add_edge(legal_clearance, loop)
root.order.add_edge(loop, data_compilation)
root.order.add_edge(data_compilation, report_drafting)
root.order.add_edge(report_drafting, peer_review)
root.order.add_edge(peer_review, final_assessment)
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(acquisition_plan, restoration_prep)
root.order.add_edge(acquisition_plan, documentation)
root.order.add_edge(acquisition_plan, data_backup)