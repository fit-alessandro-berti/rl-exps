import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the sequence of activities
provenance_sequence = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, condition_scan, material_test])
disassembly_sequence = OperatorPOWL(operator=Operator.LOOP, children=[disassembly, surface_clean, structural_repair])
reconstruction_sequence = OperatorPOWL(operator=Operator.LOOP, children=[reconstruction, finish_match, stabilize_parts, documentation])
quality_sequence = OperatorPOWL(operator=Operator.LOOP, children=[quality_audit, valuation, market_analysis, target_outreach, delivery_prep])
feedback_sequence = OperatorPOWL(operator=Operator.LOOP, children=[feedback_sequence])

# Define the overall workflow
root = StrictPartialOrder(nodes=[provenance_sequence, disassembly_sequence, reconstruction_sequence, quality_sequence, feedback_sequence])
root.order.add_edge(provenance_sequence, disassembly_sequence)
root.order.add_edge(disassembly_sequence, reconstruction_sequence)
root.order.add_edge(reconstruction_sequence, quality_sequence)
root.order.add_edge(quality_sequence, feedback_sequence)