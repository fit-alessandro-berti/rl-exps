import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
visual_inspect = Transition(label='Visual Inspect')
document_gather = Transition(label='Document Gather')
material_test = Transition(label='Material Test')
pigment_analyze = Transition(label='Pigment Analyze')
style_compare = Transition(label='Style Compare')
provenance_trace = Transition(label='Provenance Trace')
data_crosscheck = Transition(label='Data Crosscheck')
infrared_scan = Transition(label='Infrared Scan')
xray_fluoresce = Transition(label='Xray Fluoresce')
expert_consult = Transition(label='Expert Consult')
forgery_detect = Transition(label='Forgery Detect')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
final_approval = Transition(label='Final Approval')
archive_store = Transition(label='Archive Store')

# Define the silent transitions
skip = SilentTransition()

# Define the loop and XOR operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, stakeholder_review])
xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval, archive_store])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root model
print(root)