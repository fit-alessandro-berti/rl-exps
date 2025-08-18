import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define POWL transitions
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

# Define POWL operators
partial_order = StrictPartialOrder(nodes=[
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

# Define edges in the partial order
partial_order.order.add_edge(artifact_intake, document_check)
partial_order.order.add_edge(document_check, provenance_search)
partial_order.order.add_edge(provenance_search, ownership_validate)
partial_order.order.add_edge(ownership_validate, radiocarbon_test)
partial_order.order.add_edge(radiocarbon_test, spectroscopy_scan)
partial_order.order.add_edge(spectroscopy_scan, material_analysis)
partial_order.order.add_edge(material_analysis, style_assessment)
partial_order.order.add_edge(style_assessment, context_review)
partial_order.order.add_edge(context_review, expert_panel)
partial_order.order.add_edge(expert_panel, report_draft)
partial_order.order.add_edge(report_draft, quality_review)
partial_order.order.add_edge(quality_review, catalog_entry)
partial_order.order.add_edge(catalog_entry, insurance_setup)
partial_order.order.add_edge(insurance_setup, archive_data)
partial_order.order.add_edge(archive_data, reevaluation_trigger)

# Define 'root' as the partial order
root = partial_order