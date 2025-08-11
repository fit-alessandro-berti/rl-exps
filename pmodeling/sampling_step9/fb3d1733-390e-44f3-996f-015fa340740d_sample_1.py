import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for no-operation
skip = SilentTransition()

# Define the loop for gear fabrication
loop_fabricate_gears = OperatorPOWL(operator=Operator.LOOP, children=[fabricate_gears, skip])

# Define the exclusive choice for dial restoration
xor_dial_restoration = OperatorPOWL(operator=Operator.XOR, children=[dial_restoration, skip])

# Define the loop for quality testing
loop_quality_testing = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, skip])

# Define the loop for document process
loop_document_process = OperatorPOWL(operator=Operator.LOOP, children=[document_process, skip])

# Define the loop for packaging product
loop_package_product = OperatorPOWL(operator=Operator.LOOP, children=[package_product, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[initial_assess, disassemble_parts, ultrasonic_clean, inspect_components, fabricate_gears, loop_fabricate_gears, dial_restoration, xor_dial_restoration, reassemble_movement, lubricate_bearings, calibrate_timing, polish_case, re_case_watch, quality_testing, loop_quality_testing, document_process, loop_document_process, package_product, loop_package_product])
root.order.add_edge(initial_assess, disassemble_parts)
root.order.add_edge(disassemble_parts, ultrasonic_clean)
root.order.add_edge(ultrasonic_clean, inspect_components)
root.order.add_edge(inspect_components, fabricate_gears)
root.order.add_edge(fabricate_gears, loop_fabricate_gears)
root.order.add_edge(loop_fabricate_gears, dial_restoration)
root.order.add_edge(dial_restoration, xor_dial_restoration)
root.order.add_edge(xor_dial_restoration, reassemble_movement)
root.order.add_edge(reassemble_movement, lubricate_bearings)
root.order.add_edge(lubricate_bearings, calibrate_timing)
root.order.add_edge(calibrate_timing, polish_case)
root.order.add_edge(polish_case, re_case_watch)
root.order.add_edge(re_case_watch, quality_testing)
root.order.add_edge(quality_testing, loop_quality_testing)
root.order.add_edge(loop_quality_testing, document_process)
root.order.add_edge(document_process, loop_document_process)
root.order.add_edge(loop_document_process, package_product)
root.order.add_edge(package_product, loop_package_product)