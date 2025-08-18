from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

# Define the activities
sourcing = Transition(label='Material Sourcing')
harvest = Transition(label='Botanical Harvest')
extraction = Transition(label='Extraction Phase')
blending = Transition(label='Accord Blending')
testing = Transition(label='Olfactory Testing')
aging = Transition(label='Aging Process')
stability_check = Transition(label='Stability Check')
sensory_panel = Transition(label='Sensory Panel')
label_design = Transition(label='Label Design')
bottle_crafting = Transition(label='Bottle Crafting')
batch_mixing = Transition(label='Batch Mixing')
quality_review = Transition(label='Quality Review')
packaging = Transition(label='Packaging Final')
launch = Transition(label='Market Launch')
inventory_update = Transition(label='Inventory Update')

# Define the workflow
root = StrictPartialOrder(nodes=[
    sourcing, harvest, extraction, blending, testing, aging, stability_check, sensory_panel, label_design, bottle_crafting, batch_mixing, quality_review, packaging, launch, inventory_update
])

# Define the workflow structure
root.order.add_edge(sourcing, harvest)
root.order.add_edge(harvest, extraction)
root.order.add_edge(extraction, blending)
root.order.add_edge(blending, testing)
root.order.add_edge(testing, aging)
root.order.add_edge(aging, stability_check)
root.order.add_edge(stability_check, sensory_panel)
root.order.add_edge(sensory_panel, label_design)
root.order.add_edge(label_design, bottle_crafting)
root.order.add_edge(bottle_crafting, batch_mixing)
root.order.add_edge(batch_mixing, quality_review)
root.order.add_edge(quality_review, packaging)
root.order.add_edge(packaging, launch)
root.order.add_edge(launch, inventory_update)

# Print the root POWL model
print(root)