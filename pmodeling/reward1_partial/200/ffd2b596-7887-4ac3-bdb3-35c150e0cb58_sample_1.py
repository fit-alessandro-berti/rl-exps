root = StrictPartialOrder(
    nodes=[
        Transition(label='Component Sourcing'),
        Transition(label='Sensor Calibrate'),
        Transition(label='Motor Assembly'),
        Transition(label='Frame Build'),
        Transition(label='Software Install'),
        Transition(label='Algorithm Tune'),
        Transition(label='Battery Integrate'),
        Transition(label='Signal Test'),
        Transition(label='Durability Check'),
        Transition(label='Flight Simulate'),
        Transition(label='Quality Inspect'),
        Transition(label='Compliance Review'),
        Transition(label='Packaging Prep'),
        Transition(label='Logistics Plan'),
        Transition(label='Client Feedback')
    ],
    order=[
        ('Component Sourcing', 'Sensor Calibrate'),
        ('Component Sourcing', 'Motor Assembly'),
        ('Sensor Calibrate', 'Frame Build'),
        ('Motor Assembly', 'Frame Build'),
        ('Frame Build', 'Software Install'),
        ('Software Install', 'Algorithm Tune'),
        ('Algorithm Tune', 'Battery Integrate'),
        ('Battery Integrate', 'Signal Test'),
        ('Signal Test', 'Durability Check'),
        ('Durability Check', 'Flight Simulate'),
        ('Flight Simulate', 'Quality Inspect'),
        ('Quality Inspect', 'Compliance Review'),
        ('Compliance Review', 'Packaging Prep'),
        ('Packaging Prep', 'Logistics Plan'),
        ('Logistics Plan', 'Client Feedback')
    ]
)