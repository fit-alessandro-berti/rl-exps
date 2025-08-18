import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
initial_assess = Transition(label='Initial Assess')
disassemble_parts = Transition(label='Disassemble Parts')
ultrasonic_clean = Transition(label='Ultrasonic Clean')
inspect_components = Transition(label='Inspect Components')
fabricate_gears = Transition(label='Fabricate Gears')
dial_restoration = Transition(label='Dial Restoration')
repaint_markers = Transition(label='Repaint Markers')
reassemble_movement = Transition(label='Reassemble Movement')
lubricate_bearings = Transition(label='Lubricate Bearings')
calibrate_timing = Transition(label='Calibrate Timing')
polish_case = Transition(label='Polish Case')
re_case_watch = Transition(label='Re-case Watch')
quality_testing = Transition(label='Quality Testing')
document_process = Transition(label='Document Process')
package_product = Transition(label='Package Product')

# Define the silent transitions
skip = SilentTransition()

# Define the operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[fabricate_gears, ultrasonic_clean, inspect_components, reassemble_movement, lubricate_bearings, calibrate_timing, polish_case, re_case_watch])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, document_process])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, package_product])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[initial_assess, disassemble_parts, loop, xor, xor2])
root.order.add_edge(initial_assess, disassemble_parts)
root.order.add_edge(disassemble_parts, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, package_product)

# Print the root POWL model
print(root)