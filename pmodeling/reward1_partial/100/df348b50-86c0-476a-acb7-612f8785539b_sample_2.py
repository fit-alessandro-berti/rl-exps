from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model structure
root = StrictPartialOrder(
    nodes=[
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
        packaging_final,
        inventory_update,
        market_launch
    ],
    order={
        material_sourcing: botanical_harvest,
        botanical_harvest: extraction_phase,
        extraction_phase: accord_blending,
        accord_blending: olfactory_testing,
        olfactory_testing: aging_process,
        aging_process: stability_check,
        stability_check: sensory_panel,
        sensory_panel: label_design,
        label_design: bottle_crafting,
        bottle_crafting: batch_mixing,
        batch_mixing: quality_review,
        quality_review: packaging_final,
        packaging_final: inventory_update,
        inventory_update: market_launch
    }
)

# Add any additional constraints or relationships as needed
# For example, if there is a specific order for certain activities:
# root.order.add_edge(extraction_phase, accord_blending)
# root.order.add_edge(accord_blending, olfactory_testing)

# Print the final POWL model
print(root)