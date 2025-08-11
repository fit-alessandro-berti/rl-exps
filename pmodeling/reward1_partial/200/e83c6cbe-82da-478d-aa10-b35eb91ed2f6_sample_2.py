root = StrictPartialOrder(
    nodes=[
        Transition(label='Provenance Check'),
        Transition(label='Material Testing'),
        Transition(label='Stylistic Review'),
        Transition(label='Expert Panel'),
        Transition(label='Legal Clearance'),
        Transition(label='Ethics Audit'),
        Transition(label='Insurance Quote'),
        Transition(label='Risk Assess'),
        Transition(label='Digital Archive'),
        Transition(label='Replica Build'),
        Transition(label='Transport Prep'),
        Transition(label='Final Review'),
        Transition(label='Catalog Entry'),
        Transition(label='Public Notice'),
        Transition(label='Condition Report')
    ],
    order=[
        ('Provenance Check', 'Material Testing'),
        ('Material Testing', 'Stylistic Review'),
        ('Stylistic Review', 'Expert Panel'),
        ('Expert Panel', 'Legal Clearance'),
        ('Legal Clearance', 'Ethics Audit'),
        ('Ethics Audit', 'Insurance Quote'),
        ('Insurance Quote', 'Risk Assess'),
        ('Risk Assess', 'Digital Archive'),
        ('Digital Archive', 'Replica Build'),
        ('Replica Build', 'Transport Prep'),
        ('Transport Prep', 'Final Review'),
        ('Final Review', 'Catalog Entry'),
        ('Catalog Entry', 'Public Notice'),
        ('Public Notice', 'Condition Report')
    ]
)