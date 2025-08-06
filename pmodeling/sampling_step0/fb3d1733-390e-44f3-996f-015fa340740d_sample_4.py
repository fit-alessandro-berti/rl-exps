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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[fabricate_gears, initial_assess])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[repaint_markers, inspect_components])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[dial_restoration, ultrasonic_clean])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[reassemble_movement, lubricate_bearings])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[calibrate_timing, polish_case])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[re_case_watch, quality_testing])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[document_process, package_product])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])

root = StrictPartialOrder(nodes=[loop1])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop1, xor6)
root.order.add_edge(loop1, xor7)