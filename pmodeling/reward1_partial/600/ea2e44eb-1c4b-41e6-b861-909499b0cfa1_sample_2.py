import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define partial order
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

# Define order dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, archive_search)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(material_scan, archive_search)
root.order.add_edge(material_scan, expert_consult)
root.order.add_edge(three_d_imaging, archive_search)
root.order.add_edge(three_d_imaging, expert_consult)
root.order.add_edge(stylistic_match, database_query)
root.order.add_edge(panel_review, stylistic_match)
root.order.add_edge(panel_review, database_query)
root.order.add_edge(certify_report, panel_review)
root.order.add_edge(condition_assess, certify_report)
root.order.add_edge(storage_plan, certify_report)
root.order.add_edge(catalog_entry, certify_report)
root.order.add_edge(display_prep, certify_report)
root.order.add_edge(loan_arrange, certify_report)
root.order.add_edge(monitor_setup, certify_report)

# Print the root of the POWL model
print(root)