root = StrictPartialOrder(
    nodes=[
        Transition('Provenance Check'),
        Transition('Sample Collection'),
        Transition('Spectroscopy Test'),
        Transition('Carbon Dating'),
        Transition('Expert Review'),
        Transition('Legal Clearance'),
        Transition('Cultural Assessment'),
        Transition('Digital Scan'),
        Transition('Report Draft'),
        Transition('Stakeholder Meet'),
        Transition('Acquisition Vote'),
        Transition('Restoration Plan'),
        Transition('Condition Report'),
        Transition('Archival Entry'),
        Transition('Final Approval')
    ],
    order=[
        ('Provenance Check', 'Sample Collection'),
        ('Sample Collection', 'Spectroscopy Test'),
        ('Sample Collection', 'Carbon Dating'),
        ('Spectroscopy Test', 'Expert Review'),
        ('Carbon Dating', 'Expert Review'),
        ('Expert Review', 'Legal Clearance'),
        ('Legal Clearance', 'Cultural Assessment'),
        ('Cultural Assessment', 'Digital Scan'),
        ('Digital Scan', 'Report Draft'),
        ('Report Draft', 'Stakeholder Meet'),
        ('Stakeholder Meet', 'Acquisition Vote'),
        ('Acquisition Vote', 'Restoration Plan'),
        ('Restoration Plan', 'Condition Report'),
        ('Condition Report', 'Archival Entry'),
        ('Archival Entry', 'Final Approval')
    ]
)