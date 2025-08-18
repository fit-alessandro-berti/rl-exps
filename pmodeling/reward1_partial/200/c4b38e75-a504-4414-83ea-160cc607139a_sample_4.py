root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Design Modules'),
        Transition(label='Install Sensors'),
        Transition(label='Calibrate Climate'),
        Transition(label='Select Seeds'),
        Transition(label='Optimize Nutrients'),
        Transition(label='Deploy Robots'),
        Transition(label='Monitor Growth'),
        Transition(label='Detect Pests'),
        Transition(label='Analyze Data'),
        Transition(label='Harvest Crops'),
        Transition(label='Customize Pack'),
        Transition(label='Recycle Waste'),
        Transition(label='Audit Energy'),
        Transition(label='Align Demand')
    ],
    order=[
        ('Site Survey', 'Design Modules'),
        ('Design Modules', 'Install Sensors'),
        ('Install Sensors', 'Calibrate Climate'),
        ('Calibrate Climate', 'Select Seeds'),
        ('Select Seeds', 'Optimize Nutrients'),
        ('Optimize Nutrients', 'Deploy Robots'),
        ('Deploy Robots', 'Monitor Growth'),
        ('Monitor Growth', 'Detect Pests'),
        ('Detect Pests', 'Analyze Data'),
        ('Analyze Data', 'Harvest Crops'),
        ('Harvest Crops', 'Customize Pack'),
        ('Customize Pack', 'Recycle Waste'),
        ('Recycle Waste', 'Audit Energy'),
        ('Audit Energy', 'Align Demand')
    ]
)