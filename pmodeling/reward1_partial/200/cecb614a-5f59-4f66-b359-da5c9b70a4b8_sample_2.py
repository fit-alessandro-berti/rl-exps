root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Load Testing'),
        Transition(label='Crop Selection'),
        Transition(label='Soil Prep'),
        Transition(label='Irrigation Setup'),
        Transition(label='Permits Acquire'),
        Transition(label='Supplier Outreach'),
        Transition(label='Planting Seedlings'),
        Transition(label='Pest Monitoring'),
        Transition(label='Nutrient Testing'),
        Transition(label='Waste Sorting'),
        Transition(label='Staff Training'),
        Transition(label='Community Meet'),
        Transition(label='Harvest Planning'),
        Transition(label='Market Launch'),
        Transition(label='Yield Tracking')
    ],
    order=[
        ('Site Survey', 'Load Testing'),
        ('Load Testing', 'Crop Selection'),
        ('Crop Selection', 'Soil Prep'),
        ('Soil Prep', 'Irrigation Setup'),
        ('Irrigation Setup', 'Permits Acquire'),
        ('Permits Acquire', 'Supplier Outreach'),
        ('Supplier Outreach', 'Planting Seedlings'),
        ('Planting Seedlings', 'Pest Monitoring'),
        ('Pest Monitoring', 'Nutrient Testing'),
        ('Nutrient Testing', 'Waste Sorting'),
        ('Waste Sorting', 'Staff Training'),
        ('Staff Training', 'Community Meet'),
        ('Community Meet', 'Harvest Planning'),
        ('Harvest Planning', 'Market Launch'),
        ('Market Launch', 'Yield Tracking')
    ]
)