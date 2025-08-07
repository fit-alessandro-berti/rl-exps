import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the POWL model
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

# Define the partial order
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

# Add dependencies between transitions
root.order.add_edge(artifact_intake, document_check)
root.order.add_edge(artifact_intake, provenance_search)
root.order.add_edge(artifact_intake, ownership_validate)
root.order.add_edge(radiocarbon_test, report_draft)
root.order.add_edge(spectroscopy_scan, report_draft)
root.order.add_edge(material_analysis, report_draft)
root.order.add_edge(style_assessment, report_draft)
root.order.add_edge(context_review, report_draft)
root.order.add_edge(expert_panel, report_draft)
root.order.add_edge(report_draft, quality_review)
root.order.add_edge(quality_review, catalog_entry)
root.order.add_edge(quality_review, insurance_setup)
root.order.add_edge(archive_data, reevaluation_trigger)

# Now, 'root' contains the POWL model for the described process