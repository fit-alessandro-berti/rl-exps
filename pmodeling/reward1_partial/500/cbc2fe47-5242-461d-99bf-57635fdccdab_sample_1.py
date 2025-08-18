from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
document_check = Transition(label='Document Check')
provenance_search = Transition(label='Provenance Search')
ownership_validate = Transition(label='Ownership Validate')
radiocarbon_test = Transition(label='Radiocarbon Test')
spectroscopy_scan = Transition(label='Spectroscopy Scan')
material_analysis = Transition(label='Material Analysis')
style_assessment = Transition(label='Style Assessment')
context_review = Transition(label='Context Review')
expert_panel = Transition(label='Expert Panel')
report_draft = Transition(label='Report Draft')
quality_review = Transition(label='Quality Review')
catalog_entry = Transition(label='Catalog Entry')
insurance_setup = Transition(label='Insurance Setup')
archive_data = Transition(label='Archive Data')
reevaluation_trigger = Transition(label='Reevaluation Trigger')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    artifact_intake,
    document_check,
    provenance_search,
    ownership_validate,
    radiocarbon_test,
    spectroscopy_scan,
    material_analysis,
    style_assessment,
    context_review,
    expert_panel,
    report_draft,
    quality_review,
    catalog_entry,
    insurance_setup,
    archive_data,
    reevaluation_trigger
])

# Define the order of activities
root.order.add_edge(artifact_intake, document_check)
root.order.add_edge(artifact_intake, provenance_search)
root.order.add_edge(document_check, ownership_validate)
root.order.add_edge(ownership_validate, radiocarbon_test)
root.order.add_edge(radiocarbon_test, spectroscopy_scan)
root.order.add_edge(spectroscopy_scan, material_analysis)
root.order.add_edge(material_analysis, style_assessment)
root.order.add_edge(style_assessment, context_review)
root.order.add_edge(context_review, expert_panel)
root.order.add_edge(expert_panel, report_draft)
root.order.add_edge(report_draft, quality_review)
root.order.add_edge(quality_review, catalog_entry)
root.order.add_edge(catalog_entry, insurance_setup)
root.order.add_edge(insurance_setup, archive_data)
root.order.add_edge(archive_data, reevaluation_trigger)

# Print the POWL model
print(root)