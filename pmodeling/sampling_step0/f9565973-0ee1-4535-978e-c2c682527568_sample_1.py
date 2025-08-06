root = StrictPartialOrder(
    nodes=[
        Transition(label='Artifact Intake'),
        Transition(label='Initial Survey'),
        Transition(label='Material Test'),
        Transition(label='Historical Check'),
        Transition(label='Registry Search'),
        Transition(label='Owner Interview'),
        Transition(label='Condition Report'),
        Transition(label='Forgery Scan'),
        Transition(label='Digital Tagging'),
        Transition(label='Ledger Entry'),
        Transition(label='Expert Review'),
        Transition(label='Legal Verify'),
        Transition(label='Provenance Draft'),
        Transition(label='Client Approval'),
        Transition(label='Final Certificate'),
        Transition(label='Archive Storage')
    ],
    order={
        ('Artifact Intake', 'Initial Survey'): None,
        ('Initial Survey', 'Material Test'): None,
        ('Material Test', 'Historical Check'): None,
        ('Historical Check', 'Registry Search'): None,
        ('Registry Search', 'Owner Interview'): None,
        ('Owner Interview', 'Condition Report'): None,
        ('Condition Report', 'Forgery Scan'): None,
        ('Forgery Scan', 'Digital Tagging'): None,
        ('Digital Tagging', 'Ledger Entry'): None,
        ('Ledger Entry', 'Expert Review'): None,
        ('Expert Review', 'Legal Verify'): None,
        ('Legal Verify', 'Provenance Draft'): None,
        ('Provenance Draft', 'Client Approval'): None,
        ('Client Approval', 'Final Certificate'): None,
        ('Final Certificate', 'Archive Storage'): None
    }
)