root = StrictPartialOrder(
    nodes=[
        Transition('Milk Sourcing'),
        Transition('Quality Testing'),
        Transition('Milk Pasteurize'),
        Transition('Curd Formation'),
        Transition('Whey Separation'),
        Transition('Press Cheese'),
        Transition('Salt Application'),
        Transition('Controlled Aging'),
        Transition('Sensory Check'),
        Transition('Batch Packaging'),
        Transition('Label Printing'),
        Transition('Cold Storage'),
        Transition('Logistics Plan'),
        Transition('Retail Delivery'),
        Transition('Feedback Review'),
        Transition('Demand Forecast'),
        Transition('Provenance Track')
    ],
    order=[
        ('Milk Sourcing', 'Quality Testing'),
        ('Quality Testing', 'Milk Pasteurize'),
        ('Milk Pasteurize', 'Curd Formation'),
        ('Curd Formation', 'Whey Separation'),
        ('Whey Separation', 'Press Cheese'),
        ('Press Cheese', 'Salt Application'),
        ('Salt Application', 'Controlled Aging'),
        ('Controlled Aging', 'Sensory Check'),
        ('Sensory Check', 'Batch Packaging'),
        ('Batch Packaging', 'Label Printing'),
        ('Label Printing', 'Cold Storage'),
        ('Cold Storage', 'Logistics Plan'),
        ('Logistics Plan', 'Retail Delivery'),
        ('Retail Delivery', 'Feedback Review'),
        ('Feedback Review', 'Demand Forecast'),
        ('Demand Forecast', 'Provenance Track')
    ]
)