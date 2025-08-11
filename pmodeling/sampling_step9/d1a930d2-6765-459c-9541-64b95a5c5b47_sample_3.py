import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[condition_check, material_test, style_compare, carbon_dating])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, digital_imaging, forgery_scan, expert_consult, historical_research, panel_review])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, final_approval])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop1)

# Print the root POWL model
print(root)