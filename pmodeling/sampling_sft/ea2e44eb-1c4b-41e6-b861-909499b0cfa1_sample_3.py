import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

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

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    archive_search,
    expert_consult,
    material_scan,
    3d_imaging,
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

# Intake -> Provenance
root.order.add_edge(artifact_intake, provenance_check)

# Provenance -> Archive Search / Expert Consult
root.order.add_edge(provenance_check, archive_search)
root.order.add_edge(provenance_check, expert_consult)

# Archive Search -> Database Query
root.order.add_edge(archive_search, database_query)

# Expert Consult -> Stylistic Match
root.order.add_edge(expert_consult, stylistic_match)

# Material Scan -> 3D Imaging
root.order.add_edge(material_scan, 3d_imaging)

# All investigations (Archive Search, Expert Consult, Database Query, Stylistic Match, Material Scan, 3D Imaging) converge to Panel Review
for investigation in [archive_search, expert_consult, database_query, stylistic_match, material_scan, 3d_imaging]:
    root.order.add_edge(investigation, panel_review)

# Panel Review -> Certify Report
root.order.add_edge(panel_review, certify_report)

# Certify Report -> Condition Assess
root.order.add_edge(certify_report, condition_assess)

# Condition Assess -> Storage Plan
root.order.add_edge(condition_assess, storage_plan)

# Storage Plan -> Catalog Entry
root.order.add_edge(storage_plan, catalog_entry)

# Catalog Entry -> Display Prep / Loan Arrange
root.order.add_edge(catalog_entry, display_prep)
root.order.add_edge(catalog_entry, loan_arrange)

# Display Prep -> Monitor Setup
root.order.add_edge(display_prep, monitor_setup)

# Loan Arrange -> Monitor Setup
root.order.add_edge(loan_arrange, monitor_setup)

# Monitor Setup -> Repeat (optional) or end
skip = pm4py.objects.powl.obj.SilentTransition()
monitor_loop = pm4py.objects.powl.obj.OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_setup, skip]
)

# Add the loop edge
root.order.add_edge(catalog_entry, monitor_loop)
root.order.add_edge(monitor_loop, display_prep)
root.order.add_edge(monitor_loop, loan_arrange)