root = StrictPartialOrder(
    nodes=[
        Transition(label='Component Sourcing'),
        Transition(label='Frame Assembly'),
        Transition(label='Motor Installation'),
        Transition(label='Sensor Mounting'),
        Transition(label='Wiring Setup'),
        Transition(label='Firmware Upload'),
        Transition(label='AI Module'),
        Transition(label='Calibration Phase'),
        Transition(label='Stress Testing'),
        Transition(label='Flight Simulation'),
        Transition(label='Pattern Adjustment'),
        Transition(label='Quality Inspect'),
        Transition(label='Compliance Check'),
        Transition(label='Packaging Final'),
        Transition(label='Delivery Setup')
    ],
    order={
        ('Component Sourcing', 'Frame Assembly'): (),
        ('Frame Assembly', 'Motor Installation'): (),
        ('Motor Installation', 'Sensor Mounting'): (),
        ('Sensor Mounting', 'Wiring Setup'): (),
        ('Wiring Setup', 'Firmware Upload'): (),
        ('Firmware Upload', 'AI Module'): (),
        ('AI Module', 'Calibration Phase'): (),
        ('Calibration Phase', 'Stress Testing'): (),
        ('Stress Testing', 'Flight Simulation'): (),
        ('Flight Simulation', 'Pattern Adjustment'): (),
        ('Pattern Adjustment', 'Quality Inspect'): (),
        ('Quality Inspect', 'Compliance Check'): (),
        ('Compliance Check', 'Packaging Final'): (),
        ('Packaging Final', 'Delivery Setup'): ()
    }
)