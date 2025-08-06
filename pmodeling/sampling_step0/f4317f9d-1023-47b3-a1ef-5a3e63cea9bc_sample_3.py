root = StrictPartialOrder(
    nodes=[
        Transition(label='Provenance Check'),
        Transition(label='Material Scan'),
        Transition(label='Style Compare'),
        Transition(label='AI Imaging'),
        Transition(label='Chemical Test'),
        Transition(label='Aging Verify'),
        Transition(label='Record Match'),
        Transition(label='Database Query'),
        Transition(label='Panel Review'),
        Transition(label='Forgery Risk'),
        Transition(label='Market Value'),
        Transition(label='Report Draft'),
        Transition(label='Certification'),
        Transition(label='Approval Stage'),
        Transition(label='Secure Packing'),
        Transition(label='Transport Prep'),
        Transition(label='Exit')
    ],
    order=[
        (Transition(label='Provenance Check'), Transition(label='Material Scan')),
        (Transition(label='Material Scan'), Transition(label='Style Compare')),
        (Transition(label='Style Compare'), Transition(label='AI Imaging')),
        (Transition(label='AI Imaging'), Transition(label='Chemical Test')),
        (Transition(label='Chemical Test'), Transition(label='Aging Verify')),
        (Transition(label='Aging Verify'), Transition(label='Record Match')),
        (Transition(label='Record Match'), Transition(label='Database Query')),
        (Transition(label='Database Query'), Transition(label='Panel Review')),
        (Transition(label='Panel Review'), Transition(label='Forgery Risk')),
        (Transition(label='Forgery Risk'), Transition(label='Market Value')),
        (Transition(label='Market Value'), Transition(label='Report Draft')),
        (Transition(label='Report Draft'), Transition(label='Certification')),
        (Transition(label='Certification'), Transition(label='Approval Stage')),
        (Transition(label='Approval Stage'), Transition(label='Secure Packing')),
        (Transition(label='Secure Packing'), Transition(label='Transport Prep')),
        (Transition(label='Transport Prep'), Transition(label='Exit'))
    ]
)