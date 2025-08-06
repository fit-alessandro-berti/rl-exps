root = StrictPartialOrder(
    nodes=[
        Transition(label='Ingredient Sourcing'),
        Transition(label='Quality Testing'),
        Transition(label='Scent Blending'),
        Transition(label='Micro Batch'),
        Transition(label='Sensory Panel'),
        Transition(label='Formula Adjust'),
        Transition(label='Safety Review'),
        Transition(label='Sustainability Check'),
        Transition(label='Packaging Design'),
        Transition(label='Prototype Creation'),
        Transition(label='Client Feedback'),
        Transition(label='Label Approval'),
        Transition(label='Final Production'),
        Transition(label='Marketing Plan'),
        Transition(label='Distribution Prep'),
        Transition(label='Sales Launch'),
        Transition(label='Niche Luxury Market')
    ],
    order={
        'Ingredient Sourcing': 'Quality Testing',
        'Quality Testing': 'Scent Blending',
        'Scent Blending': 'Micro Batch',
        'Micro Batch': 'Sensory Panel',
        'Sensory Panel': 'Formula Adjust',
        'Formula Adjust': 'Safety Review',
        'Safety Review': 'Sustainability Check',
        'Sustainability Check': 'Packaging Design',
        'Packaging Design': 'Prototype Creation',
        'Prototype Creation': 'Client Feedback',
        'Client Feedback': 'Label Approval',
        'Label Approval': 'Final Production',
        'Final Production': 'Marketing Plan',
        'Marketing Plan': 'Distribution Prep',
        'Distribution Prep': 'Sales Launch',
        'Sales Launch': 'Niche Luxury Market'
    }
)