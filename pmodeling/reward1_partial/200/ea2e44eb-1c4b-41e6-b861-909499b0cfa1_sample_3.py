from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
expert_consult = Transition(label='Expert Consult')
material_scan = Transition(label='Material Scan')
three_d_imaging = Transition(label='3D Imaging')
stylistic_match = Transition(label='Stylistic Match')
database_query = Transition(label='Database Query')
panel_review = Transition(label='Panel Review')
certify_report = Transition(label='Certify Report')
condition_assess = Transition(label='Condition Assess')
storage_plan = Transition(label='Storage Plan')
catalog_entry = Transition(label='Catalog Entry')
display_prep = Transition(label='Display Prep')
loan_arrange = Transition(label='Loan Arrange')
monitor_setup = Transition(label='Monitor Setup')

# Define silent transitions
skip = SilentTransition()

# Define sub-processes and loops
provenance_sub_process = StrictPartialOrder(nodes=[provenance_check, archive_search, expert_consult, material_scan, three_d_imaging, stylistic_match, database_query, panel_review])
provenance_sub_process.order.add_edge(provenance_check, archive_search)
provenance_sub_process.order.add_edge(archive_search, expert_consult)
provenance_sub_process.order.add_edge(expert_consult, material_scan)
provenance_sub_process.order.add_edge(material_scan, three_d_imaging)
provenance_sub_process.order.add_edge(three_d_imaging, stylistic_match)
provenance_sub_process.order.add_edge(stylistic_match, database_query)
provenance_sub_process.order.add_edge(database_query, panel_review)

storage_sub_process = StrictPartialOrder(nodes=[storage_plan, catalog_entry, display_prep, loan_arrange])
storage_sub_process.order.add_edge(storage_plan, catalog_entry)
storage_sub_process.order.add_edge(catalog_entry, display_prep)
storage_sub_process.order.add_edge(display_prep, loan_arrange)

# Define the main process
root = StrictPartialOrder(nodes=[artifact_intake, provenance_sub_process, storage_sub_process, certify_report, condition_assess, monitor_setup])
root.order.add_edge(artifact_intake, provenance_sub_process)
root.order.add_edge(provenance_sub_process, storage_sub_process)
root.order.add_edge(storage_sub_process, certify_report)
root.order.add_edge(storage_sub_process, condition_assess)
root.order.add_edge(storage_sub_process, monitor_setup)