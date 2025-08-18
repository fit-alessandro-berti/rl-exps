root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Design Layout'),
        Transition(label='Permits Check'),
        Transition(label='Foundation Prep'),
        Transition(label='Frame Assembly'),
        Transition(label='Hydro Setup'),
        Transition(label='Climate Setup'),
        Transition(label='Seed Selection'),
        Transition(label='Nutrient Mix'),
        Transition(label='System Calibration'),
        Transition(label='Pest Control'),
        Transition(label='Automation Link'),
        Transition(label='Staff Training'),
        Transition(label='Yield Tracking'),
        Transition(label='Distribution Plan')
    ],
    order=[
        ('Site Survey', 'Design Layout'),
        ('Design Layout', 'Permits Check'),
        ('Permits Check', 'Foundation Prep'),
        ('Foundation Prep', 'Frame Assembly'),
        ('Frame Assembly', 'Hydro Setup'),
        ('Hydro Setup', 'Climate Setup'),
        ('Climate Setup', 'Seed Selection'),
        ('Seed Selection', 'Nutrient Mix'),
        ('Nutrient Mix', 'System Calibration'),
        ('System Calibration', 'Pest Control'),
        ('Pest Control', 'Automation Link'),
        ('Automation Link', 'Staff Training'),
        ('Staff Training', 'Yield Tracking'),
        ('Yield Tracking', 'Distribution Plan')
    ]
)