root = StrictPartialOrder(
    nodes=[
        Transition(label='Data Ingestion'),
        Transition(label='Quantum Setup'),
        Transition(label='Route Optimize'),
        Transition(label='Demand Forecast'),
        Transition(label='Scenario Simulate'),
        Transition(label='Risk Assess'),
        Transition(label='Anomaly Detect'),
        Transition(label='Supplier Sync'),
        Transition(label='Quantum Communicate'),
        Transition(label='Inventory Adjust'),
        Transition(label='Procurement Plan'),
        Transition(label='Performance Track'),
        Transition(label='Feedback Loop'),
        Transition(label='Decision Automate'),
        Transition(label='Cost Analyze'),
        Transition(label='Network Adapt')
    ],
    order=[
        ('Data Ingestion', 'Quantum Setup'),
        ('Quantum Setup', 'Route Optimize'),
        ('Route Optimize', 'Demand Forecast'),
        ('Demand Forecast', 'Scenario Simulate'),
        ('Scenario Simulate', 'Risk Assess'),
        ('Risk Assess', 'Anomaly Detect'),
        ('Anomaly Detect', 'Supplier Sync'),
        ('Supplier Sync', 'Quantum Communicate'),
        ('Quantum Communicate', 'Inventory Adjust'),
        ('Inventory Adjust', 'Procurement Plan'),
        ('Procurement Plan', 'Performance Track'),
        ('Performance Track', 'Feedback Loop'),
        ('Feedback Loop', 'Decision Automate'),
        ('Decision Automate', 'Cost Analyze'),
        ('Cost Analyze', 'Network Adapt')
    ]
)