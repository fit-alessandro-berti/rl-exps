root = StrictPartialOrder(
    nodes=[
        Transition('Colony Sourcing'),
        Transition('Hive Design'),
        Transition('Site Survey'),
        Transition('Installation Prep'),
        Transition('Hive Setup'),
        Transition('Sensor Install'),
        Transition('Health Monitor'),
        Transition('Pest Control'),
        Transition('Honey Harvest'),
        Transition('Wax Processing'),
        Transition('Product Packaging'),
        Transition('Order Dispatch'),
        Transition('Workshop Setup'),
        Transition('Community Outreach'),
        Transition('Regulation Check'),
        Transition('Data Analysis'),
        Transition('Maintenance Plan')
    ],
    order={
        'Colony Sourcing': 'Hive Design',
        'Hive Design': 'Site Survey',
        'Site Survey': 'Installation Prep',
        'Installation Prep': 'Hive Setup',
        'Hive Setup': 'Sensor Install',
        'Sensor Install': 'Health Monitor',
        'Health Monitor': 'Pest Control',
        'Pest Control': 'Honey Harvest',
        'Honey Harvest': 'Wax Processing',
        'Wax Processing': 'Product Packaging',
        'Product Packaging': 'Order Dispatch',
        'Order Dispatch': 'Workshop Setup',
        'Workshop Setup': 'Community Outreach',
        'Community Outreach': 'Regulation Check',
        'Regulation Check': 'Data Analysis',
        'Data Analysis': 'Maintenance Plan'
    }
)