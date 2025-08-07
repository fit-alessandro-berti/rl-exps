import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop for material test
material_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, skip])

# Define XOR for quality audit and valuation
xor_quality_audit_valuation = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, valuation])

# Define loop for target outreach and delivery prep
target_outreach_delivery_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[target_outreach, delivery_prep])

# Define XOR for market analysis and client feedback
xor_market_analysis_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, client_feedback])

# Define root process
root = StrictPartialOrder(nodes=[provenance_check, condition_scan, material_test_loop, disassembly, surface_clean, structural_repair, reconstruction, finish_match, stabilize_parts, documentation, xor_quality_audit_valuation, target_outreach_delivery_prep_loop, xor_market_analysis_client_feedback])
root.order.add_edge(provenance_check, condition_scan)
root.order.add_edge(condition_scan, material_test_loop)
root.order.add_edge(material_test_loop, disassembly)
root.order.add_edge(disassembly, surface_clean)
root.order.add_edge(surface_clean, structural_repair)
root.order.add_edge(structural_repair, reconstruction)
root.order.add_edge(reconstruction, finish_match)
root.order.add_edge(finish_match, stabilize_parts)
root.order.add_edge(stabilize_parts, documentation)
root.order.add_edge(documentation, xor_quality_audit_valuation)
root.order.add_edge(xor_quality_audit_valuation, target_outreach_delivery_prep_loop)
root.order.add_edge(target_outreach_delivery_prep_loop, xor_market_analysis_client_feedback)
root.order.add_edge(xor_market_analysis_client_feedback, material_test_loop)

# Print root
print(root)