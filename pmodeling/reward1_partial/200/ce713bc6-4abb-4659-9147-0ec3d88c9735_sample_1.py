root = StrictPartialOrder(
    nodes=[
        Transition(label='Initial Inquiry'),
        Transition(label='Document Review'),
        Transition(label='Historical Research'),
        Transition(label='Material Sampling'),
        Transition(label='Forensic Testing'),
        Transition(label='Ownership Audit'),
        Transition(label='Legal Verification'),
        Transition(label='Ethical Screening'),
        Transition(label='Expert Consultation'),
        Transition(label='Cultural Assessment'),
        Transition(label='Condition Survey'),
        Transition(label='Provenance Mapping'),
        Transition(label='Risk Analysis'),
        Transition(label='Report Compilation'),
        Transition(label='Acquisition Approval'),
        Transition(label='Repatriation Review'),
        Transition(label='Archival Storage')
    ],
    order=[
        ('Initial Inquiry', 'Document Review'),
        ('Document Review', 'Historical Research'),
        ('Historical Research', 'Material Sampling'),
        ('Material Sampling', 'Forensic Testing'),
        ('Forensic Testing', 'Ownership Audit'),
        ('Ownership Audit', 'Legal Verification'),
        ('Legal Verification', 'Ethical Screening'),
        ('Ethical Screening', 'Expert Consultation'),
        ('Expert Consultation', 'Cultural Assessment'),
        ('Cultural Assessment', 'Condition Survey'),
        ('Condition Survey', 'Provenance Mapping'),
        ('Provenance Mapping', 'Risk Analysis'),
        ('Risk Analysis', 'Report Compilation'),
        ('Report Compilation', 'Acquisition Approval'),
        ('Acquisition Approval', 'Repatriation Review'),
        ('Repatriation Review', 'Archival Storage')
    ]
)