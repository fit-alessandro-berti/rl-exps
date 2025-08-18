root = StrictPartialOrder(
    nodes=[
        Transition(label='Seed Selection'),
        Transition(label='AI Prediction'),
        Transition(label='Automated Planting'),
        Transition(label='Sensor Calibration'),
        Transition(label='Environment Adjust'),
        Transition(label='Nutrient Dosing'),
        Transition(label='Hydroponic Flow'),
        Transition(label='Robotic Pruning'),
        Transition(label='Health Monitor'),
        Transition(label='Harvesting Ops'),
        Transition(label='Data Analysis'),
        Transition(label='Predictive Check'),
        Transition(label='Waste Composting'),
        Transition(label='Water Recycling'),
        Transition(label='Eco Packaging'),
        Transition(label='Carbon Tracking'),
        Transition(label='Logistics Dispatch')
    ],
    order=[
        ('Seed Selection', 'AI Prediction'),
        ('AI Prediction', 'Automated Planting'),
        ('Automated Planting', 'Sensor Calibration'),
        ('Sensor Calibration', 'Environment Adjust'),
        ('Environment Adjust', 'Nutrient Dosing'),
        ('Nutrient Dosing', 'Hydroponic Flow'),
        ('Hydroponic Flow', 'Robotic Pruning'),
        ('Robotic Pruning', 'Health Monitor'),
        ('Health Monitor', 'Harvesting Ops'),
        ('Harvesting Ops', 'Data Analysis'),
        ('Data Analysis', 'Predictive Check'),
        ('Predictive Check', 'Waste Composting'),
        ('Waste Composting', 'Water Recycling'),
        ('Water Recycling', 'Eco Packaging'),
        ('Eco Packaging', 'Carbon Tracking'),
        ('Carbon Tracking', 'Logistics Dispatch')
    ]
)