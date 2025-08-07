import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forgery_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define the silent transition for skipping
skip = SilentTransition()

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[condition_check, material_test, style_compare, carbon_dating])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[document_review, provenance_check, digital_imaging, forgery_scan])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, historical_research])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[panel_review, report_draft])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, catalog_entry])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, artifact_intake])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor1, xor2, xor3])

# Define the dependencies
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor1)
root.order.add_edge(loop3, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)

# Print the root POWL model
print(root)