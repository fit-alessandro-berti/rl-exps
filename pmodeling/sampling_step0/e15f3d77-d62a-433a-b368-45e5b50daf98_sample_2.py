root = StrictPartialOrder(
    nodes=[
        Transition(label='Gather Specs'),
        Transition(label='Adapt Design'),
        Transition(label='Source Parts'),
        Transition(label='Component Test'),
        Transition(label='Assemble Frame'),
        Transition(label='Install Firmware'),
        Transition(label='Calibrate Sensors'),
        Transition(label='Stress Test'),
        Transition(label='Flight Simulate'),
        Transition(label='Validate Battery'),
        Transition(label='Check Accuracy'),
        Transition(label='Package Units'),
        Transition(label='Create Manuals'),
        Transition(label='Ship Drones'),
        Transition(label='Collect Feedback')
    ],
    order=[
        (Transition(label='Gather Specs'), Transition(label='Adapt Design')),
        (Transition(label='Adapt Design'), Transition(label='Source Parts')),
        (Transition(label='Source Parts'), Transition(label='Component Test')),
        (Transition(label='Component Test'), Transition(label='Assemble Frame')),
        (Transition(label='Assemble Frame'), Transition(label='Install Firmware')),
        (Transition(label='Install Firmware'), Transition(label='Calibrate Sensors')),
        (Transition(label='Calibrate Sensors'), Transition(label='Stress Test')),
        (Transition(label='Stress Test'), Transition(label='Flight Simulate')),
        (Transition(label='Flight Simulate'), Transition(label='Validate Battery')),
        (Transition(label='Validate Battery'), Transition(label='Check Accuracy')),
        (Transition(label='Check Accuracy'), Transition(label='Package Units')),
        (Transition(label='Package Units'), Transition(label='Create Manuals')),
        (Transition(label='Create Manuals'), Transition(label='Ship Drones')),
        (Transition(label='Ship Drones'), Transition(label='Collect Feedback'))
    ]
)