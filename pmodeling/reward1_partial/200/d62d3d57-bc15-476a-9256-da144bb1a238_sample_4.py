root = StrictPartialOrder(
    nodes=[
        Transition('Site Survey'),
        Transition('Structure Assess'),
        Transition('System Design'),
        Transition('Crop Select'),
        Transition('Permit Obtain'),
        Transition('Enviro Setup'),
        Transition('Irrigation Plan'),
        Transition('Sensor Install'),
        Transition('AI Calibration'),
        Transition('Staff Train'),
        Transition('Nutrient Mix'),
        Transition('Pest Monitor'),
        Transition('Yield Analyze'),
        Transition('Market Align'),
        Transition('Launch Farm')
    ],
    order={
        'Site Survey': 'Structure Assess',
        'Structure Assess': 'System Design',
        'System Design': 'Crop Select',
        'Crop Select': 'Permit Obtain',
        'Permit Obtain': 'Enviro Setup',
        'Enviro Setup': 'Irrigation Plan',
        'Irrigation Plan': 'Sensor Install',
        'Sensor Install': 'AI Calibration',
        'AI Calibration': 'Staff Train',
        'Staff Train': 'Nutrient Mix',
        'Nutrient Mix': 'Pest Monitor',
        'Pest Monitor': 'Yield Analyze',
        'Yield Analyze': 'Market Align',
        'Market Align': 'Launch Farm'
    }
)