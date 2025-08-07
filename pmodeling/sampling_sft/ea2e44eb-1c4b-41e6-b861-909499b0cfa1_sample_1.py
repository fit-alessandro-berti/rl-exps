import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
artifact_intake    = Transition(label='Artifact Intake')
provenance_check   = Transition(label='Provenance Check')
archive_search     = Transition(label='Archive Search')
expert_consult     = Transition(label='Expert Consult')
material_scan      = Transition(label='Material Scan')
3d_imaging         = Transition(label='3D Imaging')
stylistic_match    = Transition(label='Stylistic Match')
database_query     = Transition(label='Database Query')
panel_review       = Transition(label='Panel Review')
certify_report     = Transition(label='Certify Report')
condition_assess   = Transition(label='Condition Assess')
storage_plan       = Transition(label='Storage Plan')
catalog_entry      = Transition(label='Catalog Entry')
display_prep       = Transition(label='Display Prep')
loan_arrange       = Transition(label='Loan Arrange')
monitor_setup      = Transition(label='Monitor Setup')

# Build the parallel scientific analysis partial order
analysis = StrictPartialOrder(nodes=[
    material_scan, 3d_imaging, stylistic_match, database_query
])
# no edges => they are concurrent

# Build the parallel provenance research partial order
provenance = StrictPartialOrder(nodes=[
    provenance_check, archive_search, expert_consult
])
# no edges => they are concurrent

# Build the choice for either loan or display preparation
choice_display_loan = OperatorPOWL(
    operator=Operator.XOR,
    children=[display_prep, loan_arrange]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance,
    analysis,
    panel_review,
    certify_report,
    condition_assess,
    storage_plan,
    catalog_entry,
    choice_display_loan,
    monitor_setup
])

# Define the control-flow dependencies
root.order.add_edge(artifact_intake, provenance)
root.order.add_edge(artifact_intake, analysis)

root.order.add_edge(provenance, panel_review)
root.order.add_edge(analysis, panel_review)

root.order.add_edge(panel_review, certify_report)
root.order.add_edge(panel_review, condition_assess)
root.order.add_edge(panel_review, storage_plan)
root.order.add_edge(panel_review, catalog_entry)

root.order.add_edge(certify_report, choice_display_loan)
root.order.add_edge(condition_assess, choice_display_loan)
root.order.add_edge(storage_plan, choice_display_loan)
root.order.add_edge(catalog_entry, choice_display_loan)

root.order.add_edge(choice_display_loan, monitor_setup)