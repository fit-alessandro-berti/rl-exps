import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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
skip = SilentTransition()

# Define the POWL model
loop_disassembly = OperatorPOWL(operator=Operator.LOOP, children=[disassembly, surface_clean, structural_repair])
loop_material_test = OperatorPOWL(operator=Operator.LOOP, children=[material_test, stabilize_parts])
xor_documentation = OperatorPOWL(operator=Operator.XOR, children=[documentation, skip])
xor_market_analysis = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])
xor_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[target_outreach, skip])

root = StrictPartialOrder(nodes=[loop_disassembly, loop_material_test, xor_documentation, xor_market_analysis, xor_target_outreach, quality_audit, valuation, client_feedback])
root.order.add_edge(loop_disassembly, xor_documentation)
root.order.add_edge(loop_material_test, xor_market_analysis)
root.order.add_edge(xor_documentation, xor_target_outreach)
root.order.add_edge(xor_market_analysis, xor_target_outreach)
root.order.add_edge(xor_target_outreach, quality_audit)
root.order.add_edge(quality_audit, valuation)
root.order.add_edge(valuation, client_feedback)

print(root)