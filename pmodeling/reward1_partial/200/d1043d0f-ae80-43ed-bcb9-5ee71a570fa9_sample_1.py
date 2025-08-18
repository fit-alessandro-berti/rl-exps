root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Env Analysis'),
        Transition(label='Module Design'),
        Transition(label='Seed Selection'),
        Transition(label='Nutrient Mix'),
        Transition(label='Climate Setup'),
        Transition(label='LED Install'),
        Transition(label='Sensor Deploy'),
        Transition(label='Pest Control'),
        Transition(label='Waste Recycle'),
        Transition(label='Hydro Test'),
        Transition(label='Staff Train'),
        Transition(label='Yield Forecast'),
        Transition(label='Market Plan'),
        Transition(label='Data Review')
    ],
    order=[
        ('Site Survey', 'Env Analysis'),
        ('Env Analysis', 'Module Design'),
        ('Module Design', 'Seed Selection'),
        ('Seed Selection', 'Nutrient Mix'),
        ('Nutrient Mix', 'Climate Setup'),
        ('Climate Setup', 'LED Install'),
        ('LED Install', 'Sensor Deploy'),
        ('Sensor Deploy', 'Pest Control'),
        ('Pest Control', 'Waste Recycle'),
        ('Waste Recycle', 'Hydro Test'),
        ('Hydro Test', 'Staff Train'),
        ('Staff Train', 'Yield Forecast'),
        ('Yield Forecast', 'Market Plan'),
        ('Market Plan', 'Data Review')
    ]
)