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
        ('Weather Check', 'Crop Selection'),
        ('Soil Testing', 'Crop Selection'),
        ('Crop Selection', 'Resource Assign'),
        ('Crop Selection', 'Irrigation Adjust'),
        ('Crop Selection', 'Pest Scan'),
        ('Crop Selection', 'Nutrient Mix'),
        ('Crop Selection', 'Growth Monitor'),
        ('Growth Monitor', 'Community Poll'),
        ('Community Poll', 'Schedule Update'),
        ('Schedule Update', 'Harvest Plan'),
        ('Harvest Plan', 'Waste Sort'),
        ('Harvest Plan', 'Yield Report')
    ]
)