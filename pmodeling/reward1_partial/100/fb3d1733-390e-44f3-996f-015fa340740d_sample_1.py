import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[fabricate_gears, initial_assess])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[dial_restoration, initial_assess])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[repaint_markers, initial_assess])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[lubricate_bearings, initial_assess])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[calibrate_timing, initial_assess])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[polish_case, initial_assess])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[re_case_watch, initial_assess])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, initial_assess])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[document_process, initial_assess])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[package_product, initial_assess])

# Define the strict partial order
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10])
root.order.add_edge(initial_assess, xor)
root.order.add_edge(initial_assess, xor2)
root.order.add_edge(initial_assess, xor3)
root.order.add_edge(initial_assess, xor4)
root.order.add_edge(initial_assess, xor5)
root.order.add_edge(initial_assess, xor6)
root.order.add_edge(initial_assess, xor7)
root.order.add_edge(initial_assess, xor8)
root.order.add_edge(initial_assess, xor9)
root.order.add_edge(initial_assess, xor10)