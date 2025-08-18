root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Analysis'),
        Transition(label='Structure Check'),
        Transition(label='Climate Setup'),
        Transition(label='Hydroponics Install'),
        Transition(label='Nutrient Mix'),
        Transition(label='Seed Select'),
        Transition(label='Light Schedule'),
        Transition(label='Irrigation Plan'),
        Transition(label='Health Monitor'),
        Transition(label='Pest Control'),
        Transition(label='Robotic Harvest'),
        Transition(label='Clean Packaging'),
        Transition(label='Distribution Plan'),
        Transition(label='Data Collection'),
        Transition(label='Cycle Feedback')
    ],
    order=[
        ('Site Analysis', 'Structure Check'),
        ('Structure Check', 'Climate Setup'),
        ('Climate Setup', 'Hydroponics Install'),
        ('Hydroponics Install', 'Nutrient Mix'),
        ('Nutrient Mix', 'Seed Select'),
        ('Seed Select', 'Light Schedule'),
        ('Light Schedule', 'Irrigation Plan'),
        ('Irrigation Plan', 'Health Monitor'),
        ('Health Monitor', 'Pest Control'),
        ('Pest Control', 'Robotic Harvest'),
        ('Robotic Harvest', 'Clean Packaging'),
        ('Clean Packaging', 'Distribution Plan'),
        ('Distribution Plan', 'Data Collection'),
        ('Data Collection', 'Cycle Feedback')
    ]
)