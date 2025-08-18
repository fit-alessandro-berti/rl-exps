root = StrictPartialOrder(
    nodes=[
        Transition(label='Milk Sourcing'),
        Transition(label='Culture Selection'),
        Transition(label='Milk Pasteurize'),
        Transition(label='Curd Formation'),
        Transition(label='Whey Separation'),
        Transition(label='Mold Inoculate'),
        Transition(label='Cheese Pressing'),
        Transition(label='Aging Setup'),
        Transition(label='Humidity Control'),
        Transition(label='Flavor Testing'),
        Transition(label='Packaging Design'),
        Transition(label='Label Approval'),
        Transition(label='Order Forecast'),
        Transition(label='Regulation Audit'),
        Transition(label='Waste Recycling'),
        Transition(label='Market Delivery'),
        Transition(label='Customer Feedback')
    ],
    order=[
        ('Milk Sourcing', 'Culture Selection'),
        ('Culture Selection', 'Milk Pasteurize'),
        ('Milk Pasteurize', 'Curd Formation'),
        ('Curd Formation', 'Whey Separation'),
        ('Whey Separation', 'Mold Inoculate'),
        ('Mold Inoculate', 'Cheese Pressing'),
        ('Cheese Pressing', 'Aging Setup'),
        ('Aging Setup', 'Humidity Control'),
        ('Humidity Control', 'Flavor Testing'),
        ('Flavor Testing', 'Packaging Design'),
        ('Packaging Design', 'Label Approval'),
        ('Label Approval', 'Order Forecast'),
        ('Order Forecast', 'Regulation Audit'),
        ('Regulation Audit', 'Waste Recycling'),
        ('Waste Recycling', 'Market Delivery'),
        ('Market Delivery', 'Customer Feedback')
    ]
)