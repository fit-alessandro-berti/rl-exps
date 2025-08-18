root = StrictPartialOrder(
    nodes=[
        Transition(label='Artifact Intake'),
        Transition(label='Visual Scan'),
        Transition(label='Material Test'),
        Transition(label='Radiocarbon Check'),
        Transition(label='Provenance Search'),
        Transition(label='Archive Review'),
        Transition(label='Expert Consult'),
        Transition(label='Microscope Exam'),
        Transition(label='Infrared Scan'),
        Transition(label='Legal Verify'),
        Transition(label='Condition Report'),
        Transition(label='Digital Catalog'),
        Transition(label='Ownership Audit'),
        Transition(label='Restoration Plan'),
        Transition(label='Final Approval'),
        Transition(label='Authentication Cert')
    ],
    order=[
        ('Artifact Intake', 'Visual Scan'),
        ('Visual Scan', 'Material Test'),
        ('Material Test', 'Radiocarbon Check'),
        ('Radiocarbon Check', 'Provenance Search'),
        ('Provenance Search', 'Archive Review'),
        ('Archive Review', 'Expert Consult'),
        ('Expert Consult', 'Microscope Exam'),
        ('Microscope Exam', 'Infrared Scan'),
        ('Infrared Scan', 'Legal Verify'),
        ('Legal Verify', 'Condition Report'),
        ('Condition Report', 'Digital Catalog'),
        ('Digital Catalog', 'Ownership Audit'),
        ('Ownership Audit', 'Restoration Plan'),
        ('Restoration Plan', 'Final Approval'),
        ('Final Approval', 'Authentication Cert')
    ]
)