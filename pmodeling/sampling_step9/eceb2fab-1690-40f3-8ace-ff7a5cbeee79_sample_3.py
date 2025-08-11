import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loop for restoration phases
loop = OperatorPOWL(operator=Operator.LOOP, children=[disassembly, surface_clean, material_test, structural_repair, reconstruction, finish_match, stabilize_parts, documentation])

# Define XOR for quality validation, market valuation, and targeted marketing
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, valuation, market_analysis, target_outreach])

# Define root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root POWL model
print(root)