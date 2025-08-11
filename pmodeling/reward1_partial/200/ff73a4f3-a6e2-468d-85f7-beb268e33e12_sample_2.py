root = StrictPartialOrder(
    nodes=[
        Transition(label='Audit Artifacts'),
        Transition(label='Interview Staff'),
        Transition(label='Assess Risks'),
        Transition(label='Plan Retrieval'),
        Transition(label='Legal Review'),
        Transition(label='Security Check'),
        Transition(label='Execute Recovery'),
        Transition(label='Validate Items'),
        Transition(label='Restore Function'),
        Transition(label='Update Systems'),
        Transition(label='Train Users'),
        Transition(label='Document Findings'),
        Transition(label='Archive Records'),
        Transition(label='Review Lessons'),
        Transition(label='Close Process')
    ],
    order=[
        ('Audit Artifacts', 'Interview Staff'),
        ('Interview Staff', 'Assess Risks'),
        ('Assess Risks', 'Plan Retrieval'),
        ('Plan Retrieval', 'Legal Review'),
        ('Legal Review', 'Security Check'),
        ('Security Check', 'Execute Recovery'),
        ('Execute Recovery', 'Validate Items'),
        ('Validate Items', 'Restore Function'),
        ('Restore Function', 'Update Systems'),
        ('Update Systems', 'Train Users'),
        ('Train Users', 'Document Findings'),
        ('Document Findings', 'Archive Records'),
        ('Archive Records', 'Review Lessons'),
        ('Review Lessons', 'Close Process')
    ]
)