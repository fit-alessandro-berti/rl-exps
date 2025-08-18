root = StrictPartialOrder(
    nodes=[
        Transition(label='Provenance Check'),
        Transition(label='Specimen Sampling'),
        Transition(label='Spectroscopy Test'),
        Transition(label='Radiocarbon Date'),
        Transition(label='Material Analysis'),
        Transition(label='Forensic Review'),
        Transition(label='Expert Consult'),
        Transition(label='Legal Verify'),
        Transition(label='Ownership Audit'),
        Transition(label='Risk Assess'),
        Transition(label='Insurance Quote'),
        Transition(label='Condition Report'),
        Transition(label='Documentation'),
        Transition(label='Committee Review'),
        Transition(label='Final Approval')
    ],
    order=[
        (Transition(label='Provenance Check'), Transition(label='Specimen Sampling')),
        (Transition(label='Specimen Sampling'), Transition(label='Spectroscopy Test')),
        (Transition(label='Specimen Sampling'), Transition(label='Radiocarbon Date')),
        (Transition(label='Specimen Sampling'), Transition(label='Material Analysis')),
        (Transition(label='Specimen Sampling'), Transition(label='Forensic Review')),
        (Transition(label='Specimen Sampling'), Transition(label='Expert Consult')),
        (Transition(label='Specimen Sampling'), Transition(label='Legal Verify')),
        (Transition(label='Specimen Sampling'), Transition(label='Ownership Audit')),
        (Transition(label='Specimen Sampling'), Transition(label='Risk Assess')),
        (Transition(label='Specimen Sampling'), Transition(label='Insurance Quote')),
        (Transition(label='Specimen Sampling'), Transition(label='Condition Report')),
        (Transition(label='Specimen Sampling'), Transition(label='Documentation')),
        (Transition(label='Specimen Sampling'), Transition(label='Committee Review')),
        (Transition(label='Specimen Sampling'), Transition(label='Final Approval'))
    ]
)