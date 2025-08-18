import pm4py
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

# Define the relationships
artifact_intake -> provenance_check
provenance_check -> archive_search
provenance_check -> expert_consult
archive_search -> material_scan
archive_search -> stylistic_match
expert_consult -> material_scan
expert_consult -> stylistic_match
material_scan -> three_d_imaging
stylistic_match -> database_query
database_query -> panel_review
panel_review -> certify_report
panel_review -> condition_assess
certify_report -> storage_plan
certify_report -> catalog_entry
certify_report -> display_prep
certify_report -> loan_arrange
condition_assess -> monitor_setup

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, archive_search, expert_consult, material_scan, three_d_imaging, stylistic_match, database_query, panel_review, certify_report, condition_assess, storage_plan, catalog_entry, display_prep, loan_arrange, monitor_setup])