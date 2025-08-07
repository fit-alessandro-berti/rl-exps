import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake    = Transition(label='Artifact Intake')
document_check     = Transition(label='Document Check')
provenance_search  = Transition(label='Provenance Search')
ownership_validate = Transition(label='Ownership Validate')
radiocarbon_test   = Transition(label='Radiocarbon Test')
spectroscopy_scan  = Transition(label='Spectroscopy Scan')
material_analysis  = Transition(label='Material Analysis')
style_assessment   = Transition(label='Style Assessment')
context_review     = Transition(label='Context Review')
expert_panel       = Transition(label='Expert Panel')
report_draft       = Transition(label='Report Draft')
quality_review     = Transition(label='Quality Review')
catalog_entry      = Transition(label='Catalog Entry')
insurance_setup    = Transition(label='Insurance Setup')
archive_data       = Transition(label='Archive Data')
reevaluation_trigger = Transition(label='Reevaluation Trigger')

# Define the reevaluation loop body (children of the LOOP operator)
reeval_body = StrictPartialOrder(nodes=[
    provenance_search, ownership_validate,
    radiocarbon_test, spectroscopy_scan, material_analysis,
    style_assessment, context_review,
    expert_panel
])
# No explicit order edges, they are assumed concurrent in the body

# Define the reevaluation loop: trigger after every other activity
loop = OperatorPOWL(operator=Operator.LOOP, children=[reevaluation_trigger, reeval_body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    artifact_intake, document_check,
    provenance_search, ownership_validate,
    radiocarbon_test, spectroscopy_scan, material_analysis,
    style_assessment, context_review,
    expert_panel,
    report_draft, quality_review,
    catalog_entry, insurance_setup,
    archive_data, loop
])

# Define the control-flow edges
root.order.add_edge(artifact_intake, document_check)
root.order.add_edge(document_check, provenance_search)
root.order.add_edge(document_check, ownership_validate)
root.order.add_edge(provenance_search, radiocarbon_test)
root.order.add_edge(provenance_search, spectroscopy_scan)
root.order.add_edge(provenance_search, material_analysis)
root.order.add_edge(ownership_validate, radiocarbon_test)
root.order.add_edge(ownership_validate, spectroscopy_scan)
root.order.add_edge(ownership_validate, material_analysis)
root.order.add_edge(radiocarbon_test, style_assessment)
root.order.add_edge(radiocarbon_test, context_review)
root.order.add_edge(spectroscopy_scan, style_assessment)
root.order.add_edge(spectroscopy_scan, context_review)
root.order.add_edge(material_analysis, style_assessment)
root.order.add_edge(material_analysis, context_review)
root.order.add_edge(style_assessment, expert_panel)
root.order.add_edge(context_review, expert_panel)
root.order.add_edge(expert_panel, report_draft)
root.order.add_edge(report_draft, quality_review)
root.order.add_edge(quality_review, catalog_entry)
root.order.add_edge(catalog_entry, insurance_setup)
root.order.add_edge(insurance_setup, archive_data)
root.order.add_edge(archive_data, loop)