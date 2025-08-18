root = StrictPartialOrder(
    nodes=[
        Transition(label='Inspect Item'),
        Transition(label='Verify Provenance'),
        Transition(label='Document Condition'),
        Transition(label='Disassemble Parts'),
        Transition(label='Clean Components'),
        Transition(label='Analyze Damage'),
        Transition(label='Select Materials'),
        Transition(label='Perform Repairs'),
        Transition(label='Match Finishes'),
        Transition(label='Apply Treatments'),
        Transition(label='Reassemble Item'),
        Transition(label='Quality Check'),
        Transition(label='Photograph Results'),
        Transition(label='Update Archive'),
        Transition(label='Client Review'),
        Transition(label='Finalize Report')
    ],
    order=[
        (Transition(label='Inspect Item'), Transition(label='Verify Provenance')),
        (Transition(label='Verify Provenance'), Transition(label='Document Condition')),
        (Transition(label='Document Condition'), Transition(label='Disassemble Parts')),
        (Transition(label='Disassemble Parts'), Transition(label='Clean Components')),
        (Transition(label='Clean Components'), Transition(label='Analyze Damage')),
        (Transition(label='Analyze Damage'), Transition(label='Select Materials')),
        (Transition(label='Select Materials'), Transition(label='Perform Repairs')),
        (Transition(label='Perform Repairs'), Transition(label='Match Finishes')),
        (Transition(label='Match Finishes'), Transition(label='Apply Treatments')),
        (Transition(label='Apply Treatments'), Transition(label='Reassemble Item')),
        (Transition(label='Reassemble Item'), Transition(label='Quality Check')),
        (Transition(label='Quality Check'), Transition(label='Photograph Results')),
        (Transition(label='Photograph Results'), Transition(label='Update Archive')),
        (Transition(label='Update Archive'), Transition(label='Client Review')),
        (Transition(label='Client Review'), Transition(label='Finalize Report'))
    ]
)