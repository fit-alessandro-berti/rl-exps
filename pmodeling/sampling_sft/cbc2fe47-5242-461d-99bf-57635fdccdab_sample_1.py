import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake = Transition(label='Artifact Intake')
doc_check = Transition(label='Document Check')
prov_search = Transition(label='Provenance Search')
own_validate = Transition(label='Ownership Validate')
rad_test = Transition(label='Radiocarbon Test')
spec_scan = Transition(label='Spectroscopy Scan')
mat_analysis = Transition(label='Material Analysis')
style_assess = Transition(label='Style Assessment')
context_rev = Transition(label='Context Review')
expert_panel = Transition(label='Expert Panel')
report_draft = Transition(label='Report Draft')
quality_review = Transition(label='Quality Review')
catalog_entry = Transition(label='Catalog Entry')
insurance_setup = Transition(label='Insurance Setup')
archive_data = Transition(label='Archive Data')
reevaluation_trigger = Transition(label='Reevaluation Trigger')

# Build the core authentication branch
auth_branch = StrictPartialOrder(nodes=[
    intake, doc_check, prov_search, own_validate,
    rad_test, spec_scan, mat_analysis,
    style_assess, context_rev, expert_panel,
    report_draft, quality_review
])
auth_branch.order.add_edge(intake, doc_check)
auth_branch.order.add_edge(doc_check, prov_search)
auth_branch.order.add_edge(doc_check, own_validate)
auth_branch.order.add_edge(prov_search, rad_test)
auth_branch.order.add_edge(own_validate, rad_test)
auth_branch.order.add_edge(rad_test, spec_scan)
auth_branch.order.add_edge(rad_test, mat_analysis)
auth_branch.order.add_edge(spec_scan, style_assess)
auth_branch.order.add_edge(mat_analysis, style_assess)
auth_branch.order.add_edge(style_assess, context_rev)
auth_branch.order.add_edge(context_rev, expert_panel)
auth_branch.order.add_edge(expert_panel, report_draft)
auth_branch.order.add_edge(report_draft, quality_review)

# Loop for periodic re-evaluation
loop = OperatorPOWL(operator=Operator.LOOP, children=[reevaluation_trigger, auth_branch])

# Assemble the final root process
root = StrictPartialOrder(nodes=[
    intake, doc_check, prov_search, own_validate,
    rad_test, spec_scan, mat_analysis,
    style_assess, context_rev, expert_panel,
    report_draft, quality_review,
    catalog_entry, insurance_setup, archive_data
])
root.order.add_edge(intake, doc_check)
root.order.add_edge(doc_check, prov_search)
root.order.add_edge(doc_check, own_validate)
root.order.add_edge(prov_search, rad_test)
root.order.add_edge(own_validate, rad_test)
root.order.add_edge(rad_test, spec_scan)
root.order.add_edge(rad_test, mat_analysis)
root.order.add_edge(spec_scan, style_assess)
root.order.add_edge(mat_analysis, style_assess)
root.order.add_edge(style_assess, context_rev)
root.order.add_edge(context_rev, expert_panel)
root.order.add_edge(expert_panel, report_draft)
root.order.add_edge(report_draft, quality_review)
root.order.add_edge(quality_review, catalog_entry)
root.order.add_edge(quality_review, insurance_setup)
root.order.add_edge(quality_review, archive_data)
root.order.add_edge(archive_data, reevaluation_trigger)

# Optional: add the periodic re-evaluation loop
root.order.add_edge(catalog_entry, loop)

print(root)