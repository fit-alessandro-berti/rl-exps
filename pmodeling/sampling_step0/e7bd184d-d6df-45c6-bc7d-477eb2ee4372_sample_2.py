root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Analysis'),
        Transition(label='Structure Check'),
        Transition(label='Enviro Design'),
        Transition(label='Hydro Setup'),
        Transition(label='Aeroponics Add'),
        Transition(label='Lighting Procure'),
        Transition(label='Water Recycle'),
        Transition(label='Rack Install'),
        Transition(label='Seed Select'),
        Transition(label='Germinate Seeds'),
        Transition(label='Nutrient Mix'),
        Transition(label='Staff Train'),
        Transition(label='Pest Control'),
        Transition(label='Pilot Crop'),
        Transition(label='Data Gather'),
        Transition(label='Yield Optimize')
    ],
    order=[
        ('Site Analysis', 'Structure Check'),
        ('Structure Check', 'Enviro Design'),
        ('Enviro Design', 'Hydro Setup'),
        ('Enviro Design', 'Aeroponics Add'),
        ('Hydro Setup', 'Lighting Procure'),
        ('Aeroponics Add', 'Lighting Procure'),
        ('Lighting Procure', 'Water Recycle'),
        ('Water Recycle', 'Rack Install'),
        ('Rack Install', 'Seed Select'),
        ('Seed Select', 'Germinate Seeds'),
        ('Germinate Seeds', 'Nutrient Mix'),
        ('Nutrient Mix', 'Staff Train'),
        ('Staff Train', 'Pest Control'),
        ('Pest Control', 'Pilot Crop'),
        ('Pilot Crop', 'Data Gather'),
        ('Data Gather', 'Yield Optimize')
    ]
)