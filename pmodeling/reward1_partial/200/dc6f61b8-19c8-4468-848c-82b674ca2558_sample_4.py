root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Energy Partner'),
        Transition(label='Permit Filing'),
        Transition(label='Hydro Unit'),
        Transition(label='AI Setup'),
        Transition(label='Nutrient Plan'),
        Transition(label='System Install'),
        Transition(label='Crop Testing'),
        Transition(label='Data Analysis'),
        Transition(label='Community Meet'),
        Transition(label='Yield Adjust'),
        Transition(label='Carbon Audit'),
        Transition(label='Logistics Plan'),
        Transition(label='Quality Check'),
        Transition(label='Scale Review')
    ],
    order=[
        ('Site Survey', 'Energy Partner'),
        ('Energy Partner', 'Permit Filing'),
        ('Permit Filing', 'Hydro Unit'),
        ('Hydro Unit', 'AI Setup'),
        ('AI Setup', 'Nutrient Plan'),
        ('Nutrient Plan', 'System Install'),
        ('System Install', 'Crop Testing'),
        ('Crop Testing', 'Data Analysis'),
        ('Data Analysis', 'Community Meet'),
        ('Community Meet', 'Yield Adjust'),
        ('Yield Adjust', 'Carbon Audit'),
        ('Carbon Audit', 'Logistics Plan'),
        ('Logistics Plan', 'Quality Check'),
        ('Quality Check', 'Scale Review')
    ]
)