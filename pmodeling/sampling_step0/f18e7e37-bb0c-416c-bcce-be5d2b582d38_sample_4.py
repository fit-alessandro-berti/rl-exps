root = StrictPartialOrder(
    nodes=[
        Transition(label='User Signup'),
        Transition(label='Preference Set'),
        Transition(label='Meal Select'),
        Transition(label='Schedule Delivery'),
        Transition(label='Supplier Match'),
        Transition(label='Inventory Check'),
        Transition(label='Ingredient Order'),
        Transition(label='Quality Inspect'),
        Transition(label='Meal Pack'),
        Transition(label='Route Plan'),
        Transition(label='Dispatch Kit'),
        Transition(label='Delivery Track'),
        Transition(label='Feedback Collect'),
        Transition(label='Data Analyze'),
        Transition(label='Plan Optimize')
    ],
    order={
        ('User Signup', 'Preference Set'): None,
        ('Preference Set', 'Meal Select'): None,
        ('Meal Select', 'Schedule Delivery'): None,
        ('Schedule Delivery', 'Supplier Match'): None,
        ('Supplier Match', 'Inventory Check'): None,
        ('Inventory Check', 'Ingredient Order'): None,
        ('Ingredient Order', 'Quality Inspect'): None,
        ('Quality Inspect', 'Meal Pack'): None,
        ('Meal Pack', 'Route Plan'): None,
        ('Route Plan', 'Dispatch Kit'): None,
        ('Dispatch Kit', 'Delivery Track'): None,
        ('Delivery Track', 'Feedback Collect'): None,
        ('Feedback Collect', 'Data Analyze'): None,
        ('Data Analyze', 'Plan Optimize'): None
    }
)