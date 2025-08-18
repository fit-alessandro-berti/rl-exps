root = StrictPartialOrder(
    nodes=[
        Transition(label='Asset Intake'),
        Transition(label='Provenance Check'),
        Transition(label='Material Sampling'),
        Transition(label='Radiocarbon Test'),
        Transition(label='Style Compare'),
        Transition(label='Historical Search'),
        Transition(label='Expert Consult'),
        Transition(label='Condition Review'),
        Transition(label='Scientific Analysis'),
        Transition(label='Data Compilation'),
        Transition(label='Peer Review'),
        Transition(label='Report Draft'),
        Transition(label='Certification'),
        Transition(label='Digital Archive'),
        Transition(label='Client Delivery')
    ],
    order={
        'Asset Intake': 'Provenance Check',
        'Provenance Check': 'Material Sampling',
        'Material Sampling': 'Radiocarbon Test',
        'Radiocarbon Test': 'Style Compare',
        'Style Compare': 'Historical Search',
        'Historical Search': 'Expert Consult',
        'Expert Consult': 'Condition Review',
        'Condition Review': 'Scientific Analysis',
        'Scientific Analysis': 'Data Compilation',
        'Data Compilation': 'Peer Review',
        'Peer Review': 'Report Draft',
        'Report Draft': 'Certification',
        'Certification': 'Digital Archive',
        'Digital Archive': 'Client Delivery'
    }
)