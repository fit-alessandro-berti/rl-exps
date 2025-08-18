from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Material Sourcing'),
        Transition(label='Botanical Harvest'),
        Transition(label='Extraction Phase'),
        Transition(label='Accord Blending'),
        Transition(label='Olfactory Testing'),
        Transition(label='Aging Process'),
        Transition(label='Stability Check'),
        Transition(label='Sensory Panel'),
        Transition(label='Label Design'),
        Transition(label='Bottle Crafting'),
        Transition(label='Batch Mixing'),
        Transition(label='Quality Review'),
        Transition(label='Packaging Final'),
        Transition(label='Inventory Update'),
        Transition(label='Market Launch')
    ],
    order={
        'Material Sourcing': 'Botanical Harvest',
        'Botanical Harvest': 'Extraction Phase',
        'Extraction Phase': 'Accord Blending',
        'Accord Blending': 'Olfactory Testing',
        'Olfactory Testing': 'Aging Process',
        'Aging Process': 'Stability Check',
        'Stability Check': 'Sensory Panel',
        'Sensory Panel': 'Label Design',
        'Label Design': 'Bottle Crafting',
        'Bottle Crafting': 'Batch Mixing',
        'Batch Mixing': 'Quality Review',
        'Quality Review': 'Packaging Final',
        'Packaging Final': 'Inventory Update',
        'Inventory Update': 'Market Launch'
    }
)