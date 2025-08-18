root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Structural Audit'),
        Transition(label='Climate Design'),
        Transition(label='Lighting Setup'),
        Transition(label='Irrigation Plan'),
        Transition(label='Nutrient Mix'),
        Transition(label='Sensor Install'),
        Transition(label='AI Calibration'),
        Transition(label='Pest Scan'),
        Transition(label='Energy Audit'),
        Transition(label='Renewable Sync'),
        Transition(label='Data Modeling'),
        Transition(label='Staff Briefing'),
        Transition(label='Compliance Check'),
        Transition(label='Community Meet'),
        Transition(label='Yield Review'),
        Transition(label='Feedback Loop')
    ],
    order=[
        ('Site Survey', 'Structural Audit'),
        ('Structural Audit', 'Climate Design'),
        ('Climate Design', 'Lighting Setup'),
        ('Lighting Setup', 'Irrigation Plan'),
        ('Irrigation Plan', 'Nutrient Mix'),
        ('Nutrient Mix', 'Sensor Install'),
        ('Sensor Install', 'AI Calibration'),
        ('AI Calibration', 'Pest Scan'),
        ('Pest Scan', 'Energy Audit'),
        ('Energy Audit', 'Renewable Sync'),
        ('Renewable Sync', 'Data Modeling'),
        ('Data Modeling', 'Staff Briefing'),
        ('Staff Briefing', 'Compliance Check'),
        ('Compliance Check', 'Community Meet'),
        ('Community Meet', 'Yield Review'),
        ('Yield Review', 'Feedback Loop')
    ]
)