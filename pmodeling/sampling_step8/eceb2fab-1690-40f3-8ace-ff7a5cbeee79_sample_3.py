import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
provenance_check = Transition(label='Provenance Check')
condition_scan = Transition(label='Condition Scan')
material_test = Transition(label='Material Test')
disassembly = Transition(label='Disassembly')
surface_clean = Transition(label='Surface Clean')
structural_repair = Transition(label='Structural Repair')
reconstruction = Transition(label='Reconstruction')
finish_match = Transition(label='Finish Match')
stabilize_parts = Transition(label='Stabilize Parts')
documentation = Transition(label='Documentation')
quality_audit = Transition(label='Quality Audit')
valuation = Transition(label='Valuation')
market_analysis = Transition(label='Market Analysis')
target_outreach = Transition(label='Target Outreach')
delivery_prep = Transition(label='Delivery Prep')
client_feedback = Transition(label='Client Feedback')

# Define the process
xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, condition_scan])
xor = OperatorPOWL(operator=Operator.XOR, children=[material_test, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[disassembly, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[surface_clean, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[structural_repair, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[finish_match, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[documentation, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[valuation, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[target_outreach, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[client_feedback, xor])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, xor)