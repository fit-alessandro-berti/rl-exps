root = StrictPartialOrder(
    nodes=[
        Transition(label='Verify Artwork'),
        Transition(label='Analyze Provenance'),
        Transition(label='Set Reserve'),
        Transition(label='Activate Auction'),
        Transition(label='Monitor Bids'),
        Transition(label='Adjust Pricing'),
        Transition(label='Enable Fractional'),
        Transition(label='Validate Bidders'),
        Transition(label='Resolve Disputes'),
        Transition(label='Distribute Royalties'),
        Transition(label='Promote Auction'),
        Transition(label='Process Payments'),
        Transition(label='Confirm Ownership'),
        Transition(label='Arrange Shipping'),
        Transition(label='Track Delivery'),
        Transition(label='Report Analytics'),
        SilentTransition()
    ],
    order={
        'Verify Artwork': ['Analyze Provenance'],
        'Analyze Provenance': ['Set Reserve'],
        'Set Reserve': ['Activate Auction'],
        'Activate Auction': ['Monitor Bids'],
        'Monitor Bids': ['Adjust Pricing'],
        'Adjust Pricing': ['Enable Fractional'],
        'Enable Fractional': ['Validate Bidders'],
        'Validate Bidders': ['Resolve Disputes'],
        'Resolve Disputes': ['Distribute Royalties'],
        'Distribute Royalties': ['Promote Auction'],
        'Promote Auction': ['Process Payments'],
        'Process Payments': ['Confirm Ownership'],
        'Confirm Ownership': ['Arrange Shipping'],
        'Arrange Shipping': ['Track Delivery'],
        'Track Delivery': ['Report Analytics'],
        'Report Analytics': []
    }
)