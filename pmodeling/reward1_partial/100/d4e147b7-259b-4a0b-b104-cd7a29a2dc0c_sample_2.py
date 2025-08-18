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
    order={
        ('Artifact Intake', 'Visual Scan'): 1,
        ('Visual Scan', 'Material Test'): 1,
        ('Material Test', 'Radiocarbon Check'): 1,
        ('Radiocarbon Check', 'Provenance Search'): 1,
        ('Provenance Search', 'Archive Review'): 1,
        ('Archive Review', 'Expert Consult'): 1,
        ('Expert Consult', 'Microscope Exam'): 1,
        ('Microscope Exam', 'Infrared Scan'): 1,
        ('Infrared Scan', 'Legal Verify'): 1,
        ('Legal Verify', 'Condition Report'): 1,
        ('Condition Report', 'Digital Catalog'): 1,
        ('Digital Catalog', 'Ownership Audit'): 1,
        ('Ownership Audit', 'Restoration Plan'): 1,
        ('Restoration Plan', 'Final Approval'): 1,
        ('Final Approval', 'Authentication Cert'): 1
    }
)