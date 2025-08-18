root = StrictPartialOrder(
    nodes=[
        Transition(label='Initial Inspect'),
        Transition(label='Material Test'),
        Transition(label='Imaging Scan'),
        Transition(label='Historical Check'),
        Transition(label='Expert Consult'),
        Transition(label='Provenance Trace'),
        Transition(label='Forgery Detect'),
        Transition(label='Restoration Map'),
        Transition(label='Market Analyze'),
        Transition(label='Auction Review'),
        Transition(label='Value Assess'),
        Transition(label='Report Draft'),
        Transition(label='Board Review'),
        Transition(label='Certification'),
        Transition(label='Release Artifact'),
        Transition(label='Chain Custody')
    ],
    order={
        'Initial Inspect': 'Material Test',
        'Material Test': 'Imaging Scan',
        'Imaging Scan': 'Historical Check',
        'Historical Check': 'Expert Consult',
        'Expert Consult': 'Provenance Trace',
        'Provenance Trace': 'Forgery Detect',
        'Forgery Detect': 'Restoration Map',
        'Restoration Map': 'Market Analyze',
        'Market Analyze': 'Auction Review',
        'Auction Review': 'Value Assess',
        'Value Assess': 'Report Draft',
        'Report Draft': 'Board Review',
        'Board Review': 'Certification',
        'Certification': 'Release Artifact',
        'Release Artifact': 'Chain Custody'
    }
)