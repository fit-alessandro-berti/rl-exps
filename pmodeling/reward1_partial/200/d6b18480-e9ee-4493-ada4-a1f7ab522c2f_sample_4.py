root = StrictPartialOrder(
    nodes=[
        Transition(label='Material Sourcing'),
        Transition(label='Forager Dispatch'),
        Transition(label='Authenticity Check'),
        Transition(label='Batch Scheduling'),
        Transition(label='Artisan Allocation'),
        Transition(label='Craft Assembly'),
        Transition(label='Quality Inspection'),
        Transition(label='Blockchain Update'),
        Transition(label='Demand Forecast'),
        Transition(label='Price Adjustment'),
        Transition(label='Compliance Review'),
        Transition(label='Logistics Planning'),
        Transition(label='Distributor Sync'),
        Transition(label='Customer Feedback'),
        Transition(label='Product Refinement'),
        Transition(label='Reputation Audit'),
        Transition(label='Seasonal Review')
    ],
    order=[
        ('Material Sourcing', 'Forager Dispatch'),
        ('Forager Dispatch', 'Authenticity Check'),
        ('Authenticity Check', 'Batch Scheduling'),
        ('Batch Scheduling', 'Artisan Allocation'),
        ('Artisan Allocation', 'Craft Assembly'),
        ('Craft Assembly', 'Quality Inspection'),
        ('Quality Inspection', 'Blockchain Update'),
        ('Blockchain Update', 'Demand Forecast'),
        ('Demand Forecast', 'Price Adjustment'),
        ('Price Adjustment', 'Compliance Review'),
        ('Compliance Review', 'Logistics Planning'),
        ('Logistics Planning', 'Distributor Sync'),
        ('Distributor Sync', 'Customer Feedback'),
        ('Customer Feedback', 'Product Refinement'),
        ('Product Refinement', 'Reputation Audit'),
        ('Reputation Audit', 'Seasonal Review')
    ]
)