root = StrictPartialOrder(
    nodes=[
        Transition('Material Sourcing'),
        Transition('Cultural Verify'),
        Transition('Eco Transport'),
        Transition('Batch Storytelling'),
        Transition('Craftsman Assignment'),
        Transition('Product Creation'),
        Transition('Provenance Catalog'),
        Transition('Community Marketing'),
        Transition('Collector Targeting'),
        Transition('Package Assembly'),
        Transition('Local Cooperatives'),
        Transition('Environmental Audit'),
        Transition('Ethical Logistics'),
        Transition('Global Shipping'),
        Transition('Feedback Collection')
    ],
    order={
        ('Material Sourcing', 'Cultural Verify'),
        ('Cultural Verify', 'Eco Transport'),
        ('Eco Transport', 'Batch Storytelling'),
        ('Batch Storytelling', 'Craftsman Assignment'),
        ('Craftsman Assignment', 'Product Creation'),
        ('Product Creation', 'Provenance Catalog'),
        ('Provenance Catalog', 'Community Marketing'),
        ('Community Marketing', 'Collector Targeting'),
        ('Collector Targeting', 'Package Assembly'),
        ('Package Assembly', 'Local Cooperatives'),
        ('Local Cooperatives', 'Environmental Audit'),
        ('Environmental Audit', 'Ethical Logistics'),
        ('Ethical Logistics', 'Global Shipping'),
        ('Global Shipping', 'Feedback Collection')
    }
)