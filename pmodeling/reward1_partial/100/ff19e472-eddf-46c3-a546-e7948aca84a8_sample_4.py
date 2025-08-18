root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Design Layout'),
        Transition(label='Install Modules'),
        Transition(label='Calibrate Climate'),
        Transition(label='Prepare Nutrients'),
        Transition(label='Select Seeds'),
        Transition(label='Start Germination'),
        Transition(label='Deploy Sensors'),
        Transition(label='Monitor Growth'),
        Transition(label='Manage Pests'),
        Transition(label='Schedule Harvest'),
        Transition(label='Process Waste'),
        Transition(label='Optimize Energy'),
        Transition(label='Conduct Training'),
        Transition(label='Update Records'),
        Transition(label='Review Performance')
    ],
    order=[
        ('Site Survey', 'Design Layout'),
        ('Design Layout', 'Install Modules'),
        ('Install Modules', 'Calibrate Climate'),
        ('Calibrate Climate', 'Prepare Nutrients'),
        ('Prepare Nutrients', 'Select Seeds'),
        ('Select Seeds', 'Start Germination'),
        ('Start Germination', 'Deploy Sensors'),
        ('Deploy Sensors', 'Monitor Growth'),
        ('Monitor Growth', 'Manage Pests'),
        ('Manage Pests', 'Schedule Harvest'),
        ('Schedule Harvest', 'Process Waste'),
        ('Process Waste', 'Optimize Energy'),
        ('Optimize Energy', 'Conduct Training'),
        ('Conduct Training', 'Update Records'),
        ('Update Records', 'Review Performance')
    ]
)