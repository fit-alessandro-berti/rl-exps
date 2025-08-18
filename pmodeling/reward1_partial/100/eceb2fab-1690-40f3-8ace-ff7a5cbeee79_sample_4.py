import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the exclusive choice for documenting authenticity and compliance
xor = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the loop for restoration phases
loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_repair, finish_match, stabilize_parts])

# Create the root POWL model
root = StrictPartialOrder(nodes=[provenance_check, condition_scan, material_test, disassembly, surface_clean, loop, xor])

# Add dependencies to the root POWL model
root.order.add_edge(provenance_check, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, disassembly)
root.order.add_edge(disassembly, surface_clean)
root.order.add_edge(surface_clean, loop)
root.order.add_edge(loop, xor)

print(root)