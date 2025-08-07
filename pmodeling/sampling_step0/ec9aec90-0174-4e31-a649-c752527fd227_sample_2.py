root = StrictPartialOrder(
    nodes=[
        Transition(label='Assess Artifact'),
        Transition(label='Verify Provenance'),
        Transition(label='Analyze Condition'),
        Transition(label='Plan Conservation'),
        Transition(label='Clean Surface'),
        Transition(label='Stabilize Structure'),
        Transition(label='Source Materials'),
        Transition(label='Fabricate Parts'),
        Transition(label='Perform Repairs'),
        Transition(label='Apply Patina'),
        Transition(label='Match Colors'),
        Transition(label='Document Process'),
        Transition(label='Review Quality'),
        Transition(label='Obtain Approval'),
        Transition(label='Package Securely'),
        Transition(label='Arrange Transport')
    ],
    order={
        'Assess Artifact': 'Verify Provenance',
        'Verify Provenance': 'Analyze Condition',
        'Analyze Condition': 'Plan Conservation',
        'Plan Conservation': 'Clean Surface',
        'Clean Surface': 'Stabilize Structure',
        'Stabilize Structure': 'Source Materials',
        'Source Materials': 'Fabricate Parts',
        'Fabricate Parts': 'Perform Repairs',
        'Perform Repairs': 'Apply Patina',
        'Apply Patina': 'Match Colors',
        'Match Colors': 'Document Process',
        'Document Process': 'Review Quality',
        'Review Quality': 'Obtain Approval',
        'Obtain Approval': 'Package Securely',
        'Package Securely': 'Arrange Transport'
    }
)