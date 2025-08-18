root = StrictPartialOrder(
    nodes=[
        Transition(label='Material Sourcing'),
        Transition(label='Artisan Vetting'),
        Transition(label='Sample Review'),
        Transition(label='Design Finalize'),
        Transition(label='Batch Scheduling'),
        Transition(label='Quality Check'),
        Transition(label='Custom Packaging'),
        Transition(label='Demand Forecast'),
        Transition(label='Price Adjust'),
        Transition(label='Inventory Sync'),
        Transition(label='Order Processing'),
        Transition(label='Craft Coordination'),
        Transition(label='Shipment Plan'),
        Transition(label='Market Analysis'),
        Transition(label='Feedback Loop'),
        Transition(label='Trend Monitor')
    ],
    order=[
        ('Material Sourcing', 'Artisan Vetting'),
        ('Artisan Vetting', 'Sample Review'),
        ('Sample Review', 'Design Finalize'),
        ('Design Finalize', 'Batch Scheduling'),
        ('Batch Scheduling', 'Quality Check'),
        ('Quality Check', 'Custom Packaging'),
        ('Custom Packaging', 'Demand Forecast'),
        ('Demand Forecast', 'Price Adjust'),
        ('Price Adjust', 'Inventory Sync'),
        ('Inventory Sync', 'Order Processing'),
        ('Order Processing', 'Craft Coordination'),
        ('Craft Coordination', 'Shipment Plan'),
        ('Shipment Plan', 'Market Analysis'),
        ('Market Analysis', 'Feedback Loop'),
        ('Feedback Loop', 'Trend Monitor')
    ]
)