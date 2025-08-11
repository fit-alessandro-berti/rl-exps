import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forgeries_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define silent transitions
skip = SilentTransition()

# Define loop and XOR nodes
loop_artifact = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, condition_check, material_test, style_compare, carbon_dating])
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, digital_imaging, forgeries_scan])

loop_document = OperatorPOWL(operator=Operator.LOOP, children=[document_review, expert_consult, historical_research])
xor_document = OperatorPOWL(operator=Operator.XOR, children=[panel_review, report_draft])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_artifact, xor_artifact, loop_document, xor_document, catalog_entry])

# Define the order between nodes
root.order.add_edge(loop_artifact, xor_artifact)
root.order.add_edge(loop_document, xor_document)
root.order.add_edge(xor_artifact, xor_document)
root.order.add_edge(xor_document, catalog_entry)

print(root)