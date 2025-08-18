root = StrictPartialOrder(
    nodes=[
        Transition(label='Inquiry Intake'),
        Transition(label='Consultation Call'),
        Transition(label='Concept Draft'),
        Transition(label='Feedback Loop'),
        Transition(label='Contract Setup'),
        Transition(label='Artist Match'),
        Transition(label='Material Sourcing'),
        Transition(label='Ethics Review'),
        Transition(label='Progress Check'),
        Transition(label='Milestone Approve'),
        Transition(label='Quality Audit'),
        Transition(label='Copyright Transfer'),
        Transition(label='Packaging Plan'),
        Transition(label='Shipping Arrange'),
        Transition(label='Post Delivery'),
        Transition(label='Client Survey')
    ],
    order={
        'Inquiry Intake': 'Consultation Call',
        'Consultation Call': 'Concept Draft',
        'Concept Draft': 'Feedback Loop',
        'Feedback Loop': 'Contract Setup',
        'Contract Setup': 'Artist Match',
        'Artist Match': 'Material Sourcing',
        'Material Sourcing': 'Ethics Review',
        'Ethics Review': 'Progress Check',
        'Progress Check': 'Milestone Approve',
        'Milestone Approve': 'Quality Audit',
        'Quality Audit': 'Copyright Transfer',
        'Copyright Transfer': 'Packaging Plan',
        'Packaging Plan': 'Shipping Arrange',
        'Shipping Arrange': 'Post Delivery',
        'Post Delivery': 'Client Survey'
    }
)