root = StrictPartialOrder(
    nodes=[
        Transition(label='Seed Selection'),
        Transition(label='Nutrient Mix'),
        Transition(label='Environment Setup'),
        Transition(label='Pest Scan'),
        Transition(label='Light Control'),
        Transition(label='Growth Monitor'),
        Transition(label='Water Cycle'),
        Transition(label='Air Quality'),
        Transition(label='Robotic Harvest'),
        Transition(label='Quality Check'),
        Transition(label='Data Logging'),
        Transition(label='Packaging'),
        Transition(label='Waste Sort'),
        Transition(label='Energy Audit'),
        Transition(label='Retail Sync')
    ],
    order={
        ('Seed Selection', 'Nutrient Mix'): OperatorPOWL(operator=Operator.XOR, children=[('Seed Selection', 'Environment Setup'), ('Nutrient Mix', 'Light Control')]),
        ('Environment Setup', 'Pest Scan'): OperatorPOWL(operator=Operator.XOR, children=[('Environment Setup', 'Growth Monitor'), ('Pest Scan', 'Water Cycle')]),
        ('Light Control', 'Growth Monitor'): OperatorPOWL(operator=Operator.XOR, children=[('Light Control', 'Air Quality'), ('Growth Monitor', 'Robotic Harvest')]),
        ('Water Cycle', 'Air Quality'): OperatorPOWL(operator=Operator.XOR, children=[('Water Cycle', 'Quality Check'), ('Air Quality', 'Data Logging')]),
        ('Growth Monitor', 'Robotic Harvest'): OperatorPOWL(operator=Operator.XOR, children=[('Growth Monitor', 'Quality Check'), ('Robotic Harvest', 'Data Logging')]),
        ('Air Quality', 'Quality Check'): OperatorPOWL(operator=Operator.XOR, children=[('Air Quality', 'Packaging'), ('Quality Check', 'Waste Sort')]),
        ('Water Cycle', 'Data Logging'): OperatorPOWL(operator=Operator.XOR, children=[('Water Cycle', 'Packaging'), ('Data Logging', 'Waste Sort')]),
        ('Robotic Harvest', 'Quality Check'): OperatorPOWL(operator=Operator.XOR, children=[('Robotic Harvest', 'Data Logging'), ('Quality Check', 'Waste Sort')]),
        ('Growth Monitor', 'Data Logging'): OperatorPOWL(operator=Operator.XOR, children=[('Growth Monitor', 'Quality Check'), ('Data Logging', 'Waste Sort')]),
        ('Quality Check', 'Packaging'): OperatorPOWL(operator=Operator.XOR, children=[('Quality Check', 'Waste Sort'), ('Packaging', 'Retail Sync')]),
        ('Waste Sort', 'Retail Sync'): OperatorPOWL(operator=Operator.XOR, children=[('Waste Sort', 'Energy Audit'), ('Retail Sync', 'Seed Selection')])
    }
)