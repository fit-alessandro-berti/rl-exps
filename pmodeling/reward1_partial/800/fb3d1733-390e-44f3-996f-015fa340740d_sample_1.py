import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

xor1 = OperatorPOWL(operator=Operator.XOR, children=[fabricate_gears, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[repaint_markers, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[lubricate_bearings, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[disassemble_parts, ultrasonic_clean, inspect_components, xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[dial_restoration, xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[reassemble_movement, calibrate_timing, xor3])

root = StrictPartialOrder(nodes=[initial_assess, loop1, loop2, loop3, polish_case, re_case_watch, quality_testing, document_process, package_product])
root.order.add_edge(initial_assess, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, polish_case)
root.order.add_edge(polish_case, re_case_watch)
root.order.add_edge(re_case_watch, quality_testing)
root.order.add_edge(quality_testing, document_process)
root.order.add_edge(document_process, package_product)

print(root)