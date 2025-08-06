import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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
inventory_update = Transition(label='Inventory Update')
market_launch = Transition(label='Market Launch')

# Define the loop for the aging process
loop_aging = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[aging_process])

# Define the exclusive choices
choice_stability = OperatorPOWL(operator=OperatorPOWL.XOR, children=[stability_check, sensory_panel])
choice_mixing = OperatorPOWL(operator=OperatorPOWL.XOR, children=[batch_mixing, quality_review])

# Define the final branching
choice_launch = OperatorPOWL(operator=OperatorPOWL.XOR, children=[packaging_final, market_launch])

# Define the partial order
root = StrictPartialOrder(nodes=[material_sourcing, botanical_harvest, extraction_phase, accord_blending, olfactory_testing, loop_aging, choice_stability, choice_mixing, choice_launch, inventory_update])

# Define the dependencies
root.order.add_edge(material_sourcing, botanical_harvest)
root.order.add_edge(botanical_harvest, extraction_phase)
root.order.add_edge(extraction_phase, accord_blending)
root.order.add_edge(accord_blending, olfactory_testing)
root.order.add_edge(olfactory_testing, loop_aging)
root.order.add_edge(loop_aging, choice_stability)
root.order.add_edge(choice_stability, choice_mixing)
root.order.add_edge(choice_mixing, choice_launch)
root.order.add_edge(choice_launch, inventory_update)

print(root)