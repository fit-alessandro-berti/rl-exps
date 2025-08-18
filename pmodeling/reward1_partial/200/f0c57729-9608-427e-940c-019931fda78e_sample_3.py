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
        ('Inquiry Intake', 'Consultation Call'): None,
        ('Consultation Call', 'Concept Draft'): None,
        ('Concept Draft', 'Feedback Loop'): None,
        ('Feedback Loop', 'Contract Setup'): None,
        ('Contract Setup', 'Artist Match'): None,
        ('Artist Match', 'Material Sourcing'): None,
        ('Material Sourcing', 'Ethics Review'): None,
        ('Ethics Review', 'Progress Check'): None,
        ('Progress Check', 'Milestone Approve'): None,
        ('Milestone Approve', 'Quality Audit'): None,
        ('Quality Audit', 'Copyright Transfer'): None,
        ('Copyright Transfer', 'Packaging Plan'): None,
        ('Packaging Plan', 'Shipping Arrange'): None,
        ('Shipping Arrange', 'Post Delivery'): None,
        ('Post Delivery', 'Client Survey'): None
    }
)