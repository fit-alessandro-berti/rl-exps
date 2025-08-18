import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define silent transitions
skip = SilentTransition()

# Define the process
provenance_verification = OperatorPOWL(operator=Operator.XOR, children=[
    provenance_search,
    ownership_validate,
    skip
])

scientific_tests = OperatorPOWL(operator=Operator.XOR, children=[
    radiocarbon_test,
    spectroscopy_scan,
    material_analysis,
    skip
])

expert_panel_review = OperatorPOWL(operator=Operator.XOR, children=[
    style_assessment,
    context_review,
    skip
])

report_generation = OperatorPOWL(operator=Operator.XOR, children=[
    expert_panel,
    skip
])

quality_assessment = OperatorPOWL(operator=Operator.XOR, children=[
    report_generation,
    skip
])

workflow = StrictPartialOrder(nodes=[
    artifact_intake,
    document_check,
    provenance_verification,
    scientific_tests,
    expert_panel_review,
    report_generation,
    quality_assessment,
    catalog_entry,
    insurance_setup,
    archive_data,
    reevaluation_trigger
])

# Define the order of execution
workflow.order.add_edge(artifact_intake, document_check)
workflow.order.add_edge(artifact_intake, provenance_verification)
workflow.order.add_edge(artifact_intake, scientific_tests)
workflow.order.add_edge(document_check, provenance_verification)
workflow.order.add_edge(document_check, scientific_tests)
workflow.order.add_edge(provenance_verification, expert_panel_review)
workflow.order.add_edge(provenance_verification, quality_assessment)
workflow.order.add_edge(scientific_tests, expert_panel_review)
workflow.order.add_edge(scientific_tests, quality_assessment)
workflow.order.add_edge(expert_panel_review, report_generation)
workflow.order.add_edge(expert_panel_review, quality_assessment)
workflow.order.add_edge(report_generation, catalog_entry)
workflow.order.add_edge(report_generation, insurance_setup)
workflow.order.add_edge(report_generation, archive_data)
workflow.order.add_edge(quality_assessment, reevaluation_trigger)

root = workflow