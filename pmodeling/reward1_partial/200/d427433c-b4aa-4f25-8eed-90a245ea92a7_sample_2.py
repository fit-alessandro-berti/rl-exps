root = StrictPartialOrder(
    nodes=[
        Transition(label='Milk Collection'),
        Transition(label='Quality Testing'),
        Transition(label='Milk Blending'),
        Transition(label='Starter Culture'),
        Transition(label='Fermentation Check'),
        Transition(label='Curd Cutting'),
        Transition(label='Whey Separation'),
        Transition(label='Molding Press'),
        Transition(label='Salting Stage'),
        Transition(label='Aging Control'),
        Transition(label='Packaging Design'),
        Transition(label='Cold Shipping'),
        Transition(label='Compliance Audit'),
        Transition(label='Blockchain Log'),
        Transition(label='Market Pricing'),
        Transition(label='Order Fulfillment'),
        Transition(label='Feedback Review')
    ],
    order={
        ('Milk Collection', 'Quality Testing'): None,
        ('Quality Testing', 'Milk Blending'): None,
        ('Milk Blending', 'Starter Culture'): None,
        ('Starter Culture', 'Fermentation Check'): None,
        ('Fermentation Check', 'Curd Cutting'): None,
        ('Curd Cutting', 'Whey Separation'): None,
        ('Whey Separation', 'Molding Press'): None,
        ('Molding Press', 'Salting Stage'): None,
        ('Salting Stage', 'Aging Control'): None,
        ('Aging Control', 'Packaging Design'): None,
        ('Packaging Design', 'Cold Shipping'): None,
        ('Cold Shipping', 'Compliance Audit'): None,
        ('Compliance Audit', 'Blockchain Log'): None,
        ('Blockchain Log', 'Market Pricing'): None,
        ('Market Pricing', 'Order Fulfillment'): None,
        ('Order Fulfillment', 'Feedback Review'): None
    }
)