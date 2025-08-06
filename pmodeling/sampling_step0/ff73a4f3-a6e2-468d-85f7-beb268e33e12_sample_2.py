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
    order={
        ('Audit Artifacts', 'Interview Staff'): OperatorPOWL(operator=Operator.XOR),
        ('Interview Staff', 'Assess Risks'): OperatorPOWL(operator=Operator.XOR),
        ('Assess Risks', 'Plan Retrieval'): OperatorPOWL(operator=Operator.XOR),
        ('Plan Retrieval', 'Legal Review'): OperatorPOWL(operator=Operator.XOR),
        ('Legal Review', 'Security Check'): OperatorPOWL(operator=Operator.XOR),
        ('Security Check', 'Execute Recovery'): OperatorPOWL(operator=Operator.XOR),
        ('Execute Recovery', 'Validate Items'): OperatorPOWL(operator=Operator.XOR),
        ('Validate Items', 'Restore Function'): OperatorPOWL(operator=Operator.XOR),
        ('Restore Function', 'Update Systems'): OperatorPOWL(operator=Operator.XOR),
        ('Update Systems', 'Train Users'): OperatorPOWL(operator=Operator.XOR),
        ('Train Users', 'Document Findings'): OperatorPOWL(operator=Operator.XOR),
        ('Document Findings', 'Archive Records'): OperatorPOWL(operator=Operator.XOR),
        ('Archive Records', 'Review Lessons'): OperatorPOWL(operator=Operator.XOR),
        ('Review Lessons', 'Close Process'): OperatorPOWL(operator=Operator.XOR)
    }
)