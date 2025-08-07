import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    archive_search,
    expert_consult,
    material_scan,
    three_d_imaging,
    stylistic_match,
    database_query,
    panel_review,
    certify_report,
    condition_assess,
    storage_plan,
    catalog_entry,
    display_prep,
    loan_arrange,
    monitor_setup
])

# Establish dependencies between activities
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, archive_search)
root.order.add_edge(artifact_intake, expert_consult)
root.order.add_edge(artifact_intake, material_scan)
root.order.add_edge(artifact_intake, three_d_imaging)
root.order.add_edge(artifact_intake, stylistic_match)
root.order.add_edge(artifact_intake, database_query)
root.order.add_edge(provenance_check, panel_review)
root.order.add_edge(material_scan, panel_review)
root.order.add_edge(three_d_imaging, panel_review)
root.order.add_edge(stylistic_match, panel_review)
root.order.add_edge(database_query, panel_review)
root.order.add_edge(panel_review, certify_report)
root.order.add_edge(panel_review, condition_assess)
root.order.add_edge(panel_review, storage_plan)
root.order.add_edge(panel_review, catalog_entry)
root.order.add_edge(panel_review, display_prep)
root.order.add_edge(panel_review, loan_arrange)
root.order.add_edge(panel_review, monitor_setup)

# Save the final result in the variable 'root'
print("POWL model for the process defined:")
print(root)