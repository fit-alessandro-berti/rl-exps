root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Structural Audit'),
        Transition(label='Modular Design'),
        Transition(label='Hydroponic Setup'),
        Transition(label='Climate Config'),
        Transition(label='Nutrient Mix'),
        Transition(label='Pest Detect'),
        Transition(label='Lighting Setup'),
        Transition(label='Energy Audit'),
        Transition(label='Automation Install'),
        Transition(label='Staff Training'),
        Transition(label='Market Analysis'),
        Transition(label='Regulation Check'),
        Transition(label='Yield Monitor'),
        Transition(label='Waste Manage'),
        Transition(label='Data Analytics')
    ],
    order=[
        ('Site Survey', 'Structural Audit'),
        ('Structural Audit', 'Modular Design'),
        ('Modular Design', 'Hydroponic Setup'),
        ('Hydroponic Setup', 'Climate Config'),
        ('Climate Config', 'Nutrient Mix'),
        ('Nutrient Mix', 'Pest Detect'),
        ('Pest Detect', 'Lighting Setup'),
        ('Lighting Setup', 'Energy Audit'),
        ('Energy Audit', 'Automation Install'),
        ('Automation Install', 'Staff Training'),
        ('Staff Training', 'Market Analysis'),
        ('Market Analysis', 'Regulation Check'),
        ('Regulation Check', 'Yield Monitor'),
        ('Yield Monitor', 'Waste Manage'),
        ('Waste Manage', 'Data Analytics')
    ]
)