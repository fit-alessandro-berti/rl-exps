root = StrictPartialOrder(
    nodes=[
        Transition(label='Artifact Intake'),
        Transition(label='Condition Check'),
        Transition(label='Provenance Research'),
        Transition(label='Scientific Testing'),
        Transition(label='Radiocarbon Dating'),
        Transition(label='Spectroscopy Scan'),
        Transition(label='Legal Clearance'),
        Transition(label='Heritage Compliance'),
        Transition(label='Digital Archiving'),
        Transition(label='Expert Review'),
        Transition(label='Committee Vote'),
        Transition(label='Acquisition Approval'),
        Transition(label='Conservation Plan'),
        Transition(label='Storage Setup'),
        Transition(label='Stakeholder Update')
    ],
    order=[
        ('Artifact Intake', 'Condition Check'),
        ('Condition Check', 'Provenance Research'),
        ('Provenance Research', 'Scientific Testing'),
        ('Scientific Testing', 'Radiocarbon Dating'),
        ('Radiocarbon Dating', 'Spectroscopy Scan'),
        ('Spectroscopy Scan', 'Legal Clearance'),
        ('Legal Clearance', 'Heritage Compliance'),
        ('Heritage Compliance', 'Digital Archiving'),
        ('Digital Archiving', 'Expert Review'),
        ('Expert Review', 'Committee Vote'),
        ('Committee Vote', 'Acquisition Approval'),
        ('Acquisition Approval', 'Conservation Plan'),
        ('Conservation Plan', 'Storage Setup'),
        ('Storage Setup', 'Stakeholder Update')
    ]
)