root = StrictPartialOrder(
    nodes=[
        Transition(label='Sensor Setup'),
        Transition(label='Data Collection'),
        Transition(label='Weather Check'),
        Transition(label='Soil Testing'),
        Transition(label='Crop Selection'),
        Transition(label='Resource Assign'),
        Transition(label='Irrigation Adjust'),
        Transition(label='Pest Scan'),
        Transition(label='Nutrient Mix'),
        Transition(label='Growth Monitor'),
        Transition(label='Community Poll'),
        Transition(label='Schedule Update'),
        Transition(label='Harvest Plan'),
        Transition(label='Waste Sort'),
        Transition(label='Yield Report')
    ],
    order=[
        ('Sensor Setup', 'Data Collection'),
        ('Data Collection', 'Weather Check'),
        ('Data Collection', 'Soil Testing'),
        ('Data Collection', 'Crop Selection'),
        ('Weather Check', 'Resource Assign'),
        ('Soil Testing', 'Resource Assign'),
        ('Crop Selection', 'Resource Assign'),
        ('Resource Assign', 'Irrigation Adjust'),
        ('Irrigation Adjust', 'Pest Scan'),
        ('Pest Scan', 'Nutrient Mix'),
        ('Nutrient Mix', 'Growth Monitor'),
        ('Growth Monitor', 'Community Poll'),
        ('Community Poll', 'Schedule Update'),
        ('Schedule Update', 'Harvest Plan'),
        ('Harvest Plan', 'Waste Sort'),
        ('Waste Sort', 'Yield Report')
    ]
)