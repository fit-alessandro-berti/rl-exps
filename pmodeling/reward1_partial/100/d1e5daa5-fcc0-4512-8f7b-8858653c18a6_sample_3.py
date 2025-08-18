root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Regulation Check'),
        Transition(label='Design Modules'),
        Transition(label='Install Hydroponics'),
        Transition(label='Integrate Sensors'),
        Transition(label='Calibrate Nutrients'),
        Transition(label='Program Climate'),
        Transition(label='Select Crops'),
        Transition(label='Optimize Lighting'),
        Transition(label='Train Staff'),
        Transition(label='Plan Harvest'),
        Transition(label='Recycle Waste'),
        Transition(label='Analyze Demand'),
        Transition(label='Plan Logistics'),
        Transition(label='Monitor Systems')
    ],
    order={
        'Site Survey': 'Regulation Check',
        'Regulation Check': 'Design Modules',
        'Design Modules': 'Install Hydroponics',
        'Install Hydroponics': 'Integrate Sensors',
        'Integrate Sensors': 'Calibrate Nutrients',
        'Calibrate Nutrients': 'Program Climate',
        'Program Climate': 'Select Crops',
        'Select Crops': 'Optimize Lighting',
        'Optimize Lighting': 'Train Staff',
        'Train Staff': 'Plan Harvest',
        'Plan Harvest': 'Recycle Waste',
        'Recycle Waste': 'Analyze Demand',
        'Analyze Demand': 'Plan Logistics',
        'Plan Logistics': 'Monitor Systems'
    }
)