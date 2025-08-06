import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the perfume crafting process
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

# Define the control flow
loop = OperatorPOWL(operator=Operator.LOOP, children=[accord_blending, stability_check])
xor = OperatorPOWL(operator=Operator.XOR, children=[label_design, bottle_crafting])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[batch_mixing, quality_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[sensory_panel, stability_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[packaging_final, market_launch])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, market_launch])

# Define the root node with all children
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, market_launch)

# Print the POWL model
print(root)