root = StrictPartialOrder(
    nodes=[
        Transition(label='Artifact Intake'),
        Transition(label='Preliminary Check'),
        Transition(label='Historical Review'),
        Transition(label='Chemical Test'),
        Transition(label='Provenance Audit'),
        Transition(label='Expert Panel'),
        Transition(label='Token Minting'),
        Transition(label='Legal Review'),
        Transition(label='Compliance Check'),
        Transition(label='Insurance Valuation'),
        Transition(label='Risk Assessment'),
        Transition(label='Packaging Prep'),
        Transition(label='Climate Control'),
        Transition(label='Transport Setup'),
        Transition(label='Final Approval')
    ],
    order={
        'Artifact Intake': 'Preliminary Check',
        'Preliminary Check': 'Historical Review',
        'Historical Review': 'Chemical Test',
        'Chemical Test': 'Provenance Audit',
        'Provenance Audit': 'Expert Panel',
        'Expert Panel': 'Token Minting',
        'Token Minting': 'Legal Review',
        'Legal Review': 'Compliance Check',
        'Compliance Check': 'Insurance Valuation',
        'Insurance Valuation': 'Risk Assessment',
        'Risk Assessment': 'Packaging Prep',
        'Packaging Prep': 'Climate Control',
        'Climate Control': 'Transport Setup',
        'Transport Setup': 'Final Approval'
    }
)