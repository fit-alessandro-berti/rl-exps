root = StrictPartialOrder(
    nodes=[
        Transition(label='Artifact Intake'),
        Transition(label='Condition Check'),
        Transition(label='Material Test'),
        Transition(label='Style Compare'),
        Transition(label='Carbon Dating'),
        Transition(label='Document Review'),
        Transition(label='Provenance Check'),
        Transition(label='Digital Imaging'),
        Transition(label='Forgery Scan'),
        Transition(label='Expert Consult'),
        Transition(label='Historical Research'),
        Transition(label='Panel Review'),
        Transition(label='Report Draft'),
        Transition(label='Final Approval'),
        Transition(label='Catalog Entry')
    ],
    order=[
        ('Artifact Intake', 'Condition Check'),
        ('Condition Check', 'Material Test'),
        ('Material Test', 'Style Compare'),
        ('Style Compare', 'Carbon Dating'),
        ('Document Review', 'Provenance Check'),
        ('Provenance Check', 'Digital Imaging'),
        ('Digital Imaging', 'Forgery Scan'),
        ('Forgery Scan', 'Expert Consult'),
        ('Expert Consult', 'Historical Research'),
        ('Historical Research', 'Panel Review'),
        ('Panel Review', 'Report Draft'),
        ('Report Draft', 'Final Approval'),
        ('Final Approval', 'Catalog Entry')
    ]
)