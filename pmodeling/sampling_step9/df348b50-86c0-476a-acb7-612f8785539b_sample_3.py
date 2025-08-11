import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
material_sourcing = Transition(label='Material Sourcing')
botanical_harvest = Transition(label='Botanical Harvest')
extraction_phase = Transition(label='Extraction Phase')
accord_blending = Transition(label='Accord Blending')
olfactory_testing = Transition(label='Olfactory Testing')
aging_process = Transition(label='Aging Process')
stability_check = Transition(label='Stability Check')
sensory_panel = Transition(label='Sensory Panel')
label_design = Transition(label='Label Design')
bottle_crafting = Transition(label='Bottle Crafting')
batch_mixing = Transition(label='Batch Mixing')
quality_review = Transition(label='Quality Review')
packaging_final = Transition(label='Packaging Final')
inventory_update = Transition(label='Inventory Update')
market_launch = Transition(label='Market Launch')

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[batch_mixing, stability_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[sensory_panel, quality_review])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[label_design, bottle_crafting])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, botanical_harvest])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[extraction_phase, accord_blending])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[olfactory_testing, aging_process])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update, market_launch])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop5, loop6])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor1)