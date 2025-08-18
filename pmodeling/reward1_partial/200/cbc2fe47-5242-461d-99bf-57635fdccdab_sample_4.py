from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the workflow
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_search, ownership_validate, radiocarbon_test, spectroscopy_scan, material_analysis])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[style_assessment, context_review, expert_panel])
xor = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[quality_review, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, insurance_setup])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[archive_data, reevaluation_trigger])

root = StrictPartialOrder(nodes=[artifact_intake, document_check, loop_1, loop_2, xor, xor_2, xor_3, xor_4])
root.order.add_edge(artifact_intake, document_check)
root.order.add_edge(document_check, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, xor)
root.order.add_edge(xor, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)