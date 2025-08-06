root = StrictPartialOrder(
    nodes=[
        Transition('Data Capture'),
        Transition('Quantum Calc'),
        Transition('Demand Forecast'),
        Transition('Inventory Check'),
        Transition('Route Update'),
        Transition('Shipment Plan'),
        Transition('Supplier Sync'),
        Transition('Contract Mod'),
        Transition('Blockchain Verify'),
        Transition('Risk Assess'),
        Transition('Scenario Sim'),
        Transition('Feedback Loop'),
        Transition('AI Adjust'),
        Transition('Waste Audit'),
        Transition('Report Generate'),
        Transition('Stakeholder Alert'),
        Transition('Compliance Review')
    ],
    order=[
        ('Data Capture', 'Quantum Calc'),
        ('Quantum Calc', 'Demand Forecast'),
        ('Demand Forecast', 'Inventory Check'),
        ('Inventory Check', 'Route Update'),
        ('Route Update', 'Shipment Plan'),
        ('Shipment Plan', 'Supplier Sync'),
        ('Supplier Sync', 'Contract Mod'),
        ('Contract Mod', 'Blockchain Verify'),
        ('Blockchain Verify', 'Risk Assess'),
        ('Risk Assess', 'Scenario Sim'),
        ('Scenario Sim', 'Feedback Loop'),
        ('Feedback Loop', 'AI Adjust'),
        ('AI Adjust', 'Waste Audit'),
        ('Waste Audit', 'Report Generate'),
        ('Report Generate', 'Stakeholder Alert'),
        ('Stakeholder Alert', 'Compliance Review')
    ]
)