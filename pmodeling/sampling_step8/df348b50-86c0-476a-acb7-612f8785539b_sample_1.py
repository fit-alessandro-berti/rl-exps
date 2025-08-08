from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
market_launch = Transition(label='Market Launch')

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[stability_check, sensory_panel])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_review, packaging_final])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[batch_mixing, market_launch])
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, botanical_harvest, extraction_phase, accord_blending, olfactory_testing, aging_process, xor1])
root = StrictPartialOrder(nodes=[loop, xor2, xor3])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)

print(root)