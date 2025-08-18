root = StrictPartialOrder(
    nodes=[
        Transition(label='Provenance Check'),
        Transition(label='Material Scan'),
        Transition(label='Radiocarbon Test'),
        Transition(label='Stylistic Review'),
        Transition(label='Expert Consult'),
        Transition(label='Document Audit'),
        Transition(label='Legal Verify'),
        Transition(label='Condition Report'),
        Transition(label='Discrepancy Flag'),
        Transition(label='Re-examination'),
        Transition(label='Alternative Source'),
        Transition(label='Acquisition Vote'),
        Transition(label='Catalog Entry'),
        Transition(label='Exhibit Plan'),
        Transition(label='Final Approval')
    ],
    order=[
        ('Provenance Check', 'Material Scan'),
        ('Material Scan', 'Radiocarbon Test'),
        ('Radiocarbon Test', 'Stylistic Review'),
        ('Stylistic Review', 'Expert Consult'),
        ('Expert Consult', 'Document Audit'),
        ('Document Audit', 'Legal Verify'),
        ('Legal Verify', 'Condition Report'),
        ('Condition Report', 'Discrepancy Flag'),
        ('Discrepancy Flag', 'Re-examination'),
        ('Re-examination', 'Alternative Source'),
        ('Alternative Source', 'Acquisition Vote'),
        ('Acquisition Vote', 'Catalog Entry'),
        ('Catalog Entry', 'Exhibit Plan'),
        ('Exhibit Plan', 'Final Approval')
    ]
)