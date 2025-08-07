import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
expert_interview = Transition(label='Expert Interview')
material_scan = Transition(label='Material Scan')
age_analysis = Transition(label='Age Analysis')
stylistic_review = Transition(label='Stylistic Review')
context_mapping = Transition(label='Context Mapping')
legal_clearance = Transition(label='Legal Clearance')
data_compilation = Transition(label='Data Compilation')
report_drafting = Transition(label='Report Drafting')
peer_review = Transition(label='Peer Review')
final_assessment = Transition(label='Final Assessment')
acquisition_plan = Transition(label='Acquisition Plan')
restoration_prep = Transition(label='Restoration Prep')
documentation = Transition(label='Documentation')
data_backup = Transition(label='Data Backup')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    archive_search,
    expert_interview,
    material_scan,
    age_analysis,
    stylistic_review,
    context_mapping,
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

# Define the POWL model dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, archive_search)
root.order.add_edge(archive_search, expert_interview)
root.order.add_edge(expert_interview, material_scan)
root.order.add_edge(material_scan, age_analysis)
root.order.add_edge(age_analysis, stylistic_review)
root.order.add_edge(stylistic_review, context_mapping)
root.order.add_edge(context_mapping, legal_clearance)
root.order.add_edge(legal_clearance, data_compilation)
root.order.add_edge(data_compilation, report_drafting)
root.order.add_edge(report_drafting, peer_review)
root.order.add_edge(peer_review, final_assessment)
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(acquisition_plan, restoration_prep)
root.order.add_edge(restoration_prep, documentation)
root.order.add_edge(documentation, data_backup)

# Print the final POWL model
print(root)