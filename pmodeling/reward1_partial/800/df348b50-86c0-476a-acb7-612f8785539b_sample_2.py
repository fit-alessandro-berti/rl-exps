import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for the crafting process
crafting_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    material_sourcing,
    botanical_harvest,
    extraction_phase,
    accord_blending,
    olfactory_testing,
    aging_process,
    stability_check,
    sensory_panel,
    label_design,
    bottle_crafting,
    batch_mixing,
    quality_review,
    packaging_final
])

# Define the process tree for the entire perfume crafting
root = StrictPartialOrder(nodes=[crafting_loop])
root.order.add_edge(crafting_loop, inventory_update)
root.order.add_edge(inventory_update, market_launch)

print(root)