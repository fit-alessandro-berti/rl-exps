root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Analyze'),
        Transition(label='Soil Enhance'),
        Transition(label='Seed Select'),
        Transition(label='Plant Precise'),
        Transition(label='Sensor Deploy'),
        Transition(label='Climate Monitor'),
        Transition(label='Irrigate Adjust'),
        Transition(label='Nutrient Feed'),
        Transition(label='Pest Control'),
        Transition(label='Community Engage'),
        Transition(label='Feedback Collect'),
        Transition(label='Yield Harvest'),
        Transition(label='Waste Sort'),
        Transition(label='Compost Create'),
        Transition(label='Data Analyze'),
        Transition(label='Network Distribute')
    ],
    order={
        ('Site Analyze', 'Soil Enhance'): None,
        ('Site Analyze', 'Seed Select'): None,
        ('Site Analyze', 'Plant Precise'): None,
        ('Soil Enhance', 'Sensor Deploy'): None,
        ('Sensor Deploy', 'Climate Monitor'): None,
        ('Climate Monitor', 'Irrigate Adjust'): None,
        ('Climate Monitor', 'Nutrient Feed'): None,
        ('Climate Monitor', 'Pest Control'): None,
        ('Sensor Deploy', 'Community Engage'): None,
        ('Community Engage', 'Feedback Collect'): None,
        ('Feedback Collect', 'Yield Harvest'): None,
        ('Yield Harvest', 'Waste Sort'): None,
        ('Waste Sort', 'Compost Create'): None,
        ('Compost Create', 'Data Analyze'): None,
        ('Data Analyze', 'Network Distribute'): None
    }
)