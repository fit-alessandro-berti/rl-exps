import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the loop nodes
loop_material_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, botanical_harvest, extraction_phase])
loop_accord_blending = OperatorPOWL(operator=Operator.LOOP, children=[accord_blending, olfactory_testing, aging_process])
loop_stability_check = OperatorPOWL(operator=Operator.LOOP, children=[stability_check, sensory_panel])
loop_label_design = OperatorPOWL(operator=Operator.LOOP, children=[label_design, bottle_crafting])
loop_batch_mixing = OperatorPOWL(operator=Operator.LOOP, children=[batch_mixing, quality_review])
loop_inventory_update = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update, market_launch])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_material_sourcing, loop_accord_blending, loop_stability_check, loop_label_design, loop_batch_mixing, loop_inventory_update])
root.order.add_edge(loop_material_sourcing, loop_accord_blending)
root.order.add_edge(loop_accord_blending, loop_stability_check)
root.order.add_edge(loop_stability_check, loop_label_design)
root.order.add_edge(loop_label_design, loop_batch_mixing)
root.order.add_edge(loop_batch_mixing, loop_inventory_update)

# Print the root POWL model
print(root)