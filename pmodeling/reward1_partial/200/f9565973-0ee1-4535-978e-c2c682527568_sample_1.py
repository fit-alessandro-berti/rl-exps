root = StrictPartialOrder(
    nodes=[
        Transition('Artifact Intake'),
        Transition('Initial Survey'),
        Transition('Material Test'),
        Transition('Historical Check'),
        Transition('Registry Search'),
        Transition('Owner Interview'),
        Transition('Condition Report'),
        Transition('Forgery Scan'),
        Transition('Digital Tagging'),
        Transition('Ledger Entry'),
        Transition('Expert Review'),
        Transition('Legal Verify'),
        Transition('Provenance Draft'),
        Transition('Client Approval'),
        Transition('Final Certificate'),
        Transition('Archive Storage')
    ],
    order=[
        ('Artifact Intake', 'Initial Survey'),
        ('Initial Survey', 'Material Test'),
        ('Material Test', 'Historical Check'),
        ('Historical Check', 'Registry Search'),
        ('Registry Search', 'Owner Interview'),
        ('Owner Interview', 'Condition Report'),
        ('Condition Report', 'Forgery Scan'),
        ('Forgery Scan', 'Digital Tagging'),
        ('Digital Tagging', 'Ledger Entry'),
        ('Ledger Entry', 'Expert Review'),
        ('Expert Review', 'Legal Verify'),
        ('Legal Verify', 'Provenance Draft'),
        ('Provenance Draft', 'Client Approval'),
        ('Client Approval', 'Final Certificate'),
        ('Final Certificate', 'Archive Storage')
    ]
)