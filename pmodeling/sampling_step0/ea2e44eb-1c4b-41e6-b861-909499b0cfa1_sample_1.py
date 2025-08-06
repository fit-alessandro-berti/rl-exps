from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
root = StrictPartialOrder()

# Add the activities to the partial order
root.nodes.add(artifact_intake)
root.nodes.add(provenance_check)
root.nodes.add(archive_search)
root.nodes.add(expert_consult)
root.nodes.add(material_scan)
root.nodes.add(three_d_imaging)
root.nodes.add(stylistic_match)
root.nodes.add(database_query)
root.nodes.add(panel_review)
root.nodes.add(certify_report)
root.nodes.add(condition_assess)
root.nodes.add(storage_plan)
root.nodes.add(catalog_entry)
root.nodes.add(display_prep)
root.nodes.add(loan_arrange)
root.nodes.add(monitor_setup)

# Define the order of the activities
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, archive_search)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(archive_search, material_scan)
root.order.add_edge(archive_search, three_d_imaging)
root.order.add_edge(expert_consult, stylistic_match)
root.order.add_edge(expert_consult, database_query)
root.order.add_edge(material_scan, panel_review)
root.order.add_edge(three_d_imaging, panel_review)
root.order.add_edge(database_query, panel_review)
root.order.add_edge(panel_review, certify_report)
root.order.add_edge(panel_review, condition_assess)
root.order.add_edge(condition_assess, storage_plan)
root.order.add_edge(condition_assess, catalog_entry)
root.order.add_edge(condition_assess, display_prep)
root.order.add_edge(condition_assess, loan_arrange)
root.order.add_edge(condition_assess, monitor_setup)

# Print the root
print(root)