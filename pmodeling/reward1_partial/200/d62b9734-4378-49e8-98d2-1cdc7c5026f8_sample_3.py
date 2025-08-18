root = StrictPartialOrder(
    nodes=[
        Transition(label='Provenance Check'),
        Transition(label='Image Capture'),
        Transition(label='Material Scan'),
        Transition(label='Expert Review'),
        Transition(label='Historical Cross'),
        Transition(label='Legal Verify'),
        Transition(label='Registry Search'),
        Transition(label='Customs Clear'),
        Transition(label='Condition Assess'),
        Transition(label='Data Log'),
        Transition(label='Chain Custody'),
        Transition(label='Report Draft'),
        Transition(label='Certification'),
        Transition(label='Secure Archive'),
        Transition(label='Auction Prep')
    ],
    order=[
        ('Provenance Check', 'Image Capture'),
        ('Provenance Check', 'Material Scan'),
        ('Image Capture', 'Expert Review'),
        ('Material Scan', 'Expert Review'),
        ('Expert Review', 'Historical Cross'),
        ('Historical Cross', 'Legal Verify'),
        ('Legal Verify', 'Registry Search'),
        ('Registry Search', 'Customs Clear'),
        ('Customs Clear', 'Condition Assess'),
        ('Condition Assess', 'Data Log'),
        ('Data Log', 'Chain Custody'),
        ('Chain Custody', 'Report Draft'),
        ('Report Draft', 'Certification'),
        ('Certification', 'Secure Archive'),
        ('Secure Archive', 'Auction Prep')
    ]
)