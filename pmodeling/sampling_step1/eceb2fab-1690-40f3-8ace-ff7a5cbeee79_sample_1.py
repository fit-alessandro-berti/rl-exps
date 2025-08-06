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

# Define the loop nodes
disassembly_loop = OperatorPOWL(operator=Operator.LOOP, children=[disassembly, surface_clean, structural_repair, reconstruction, finish_match])
material_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, stabilize_parts, documentation])
valuation_loop = OperatorPOWL(operator=Operator.LOOP, children=[valuation, market_analysis, target_outreach, delivery_prep, client_feedback])

# Define the root
root = StrictPartialOrder(nodes=[provenance_check, condition_scan, material_test_loop, disassembly_loop, quality_audit, valuation_loop])
root.order.add_edge(provenance_check, condition_scan)
root.order.add_edge(condition_scan, material_test_loop)
root.order.add_edge(material_test_loop, disassembly_loop)
root.order.add_edge(disassembly_loop, quality_audit)
root.order.add_edge(quality_audit, valuation_loop)