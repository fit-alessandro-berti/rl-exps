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
    order={
        ('Provenance Check', 'Material Scan'): None,
        ('Material Scan', 'Radiocarbon Test'): None,
        ('Radiocarbon Test', 'Stylistic Review'): None,
        ('Stylistic Review', 'Expert Consult'): None,
        ('Expert Consult', 'Document Audit'): None,
        ('Document Audit', 'Legal Verify'): None,
        ('Legal Verify', 'Condition Report'): None,
        ('Condition Report', 'Discrepancy Flag'): None,
        ('Discrepancy Flag', 'Re-examination'): None,
        ('Re-examination', 'Alternative Source'): None,
        ('Alternative Source', 'Acquisition Vote'): None,
        ('Acquisition Vote', 'Catalog Entry'): None,
        ('Catalog Entry', 'Exhibit Plan'): None,
        ('Exhibit Plan', 'Final Approval'): None
    }
)