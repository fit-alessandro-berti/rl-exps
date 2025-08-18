root = StrictPartialOrder(
    nodes=[
        Transition(label='Artifact Intake'),
        Transition(label='Document Check'),
        Transition(label='Provenance Search'),
        Transition(label='Ownership Validate'),
        Transition(label='Radiocarbon Test'),
        Transition(label='Spectroscopy Scan'),
        Transition(label='Material Analysis'),
        Transition(label='Style Assessment'),
        Transition(label='Context Review'),
        Transition(label='Expert Panel'),
        Transition(label='Report Draft'),
        Transition(label='Quality Review'),
        Transition(label='Catalog Entry'),
        Transition(label='Insurance Setup'),
        Transition(label='Archive Data'),
        Transition(label='Reevaluation Trigger')
    ],
    order={
        ('Artifact Intake', 'Document Check'): None,
        ('Document Check', 'Provenance Search'): None,
        ('Provenance Search', 'Ownership Validate'): None,
        ('Ownership Validate', 'Radiocarbon Test'): None,
        ('Radiocarbon Test', 'Spectroscopy Scan'): None,
        ('Spectroscopy Scan', 'Material Analysis'): None,
        ('Material Analysis', 'Style Assessment'): None,
        ('Style Assessment', 'Context Review'): None,
        ('Context Review', 'Expert Panel'): None,
        ('Expert Panel', 'Report Draft'): None,
        ('Report Draft', 'Quality Review'): None,
        ('Quality Review', 'Catalog Entry'): None,
        ('Catalog Entry', 'Insurance Setup'): None,
        ('Insurance Setup', 'Archive Data'): None,
        ('Archive Data', 'Reevaluation Trigger'): None
    }
)