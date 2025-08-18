root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Structural Audit'),
        Transition(label='Permit Filing'),
        Transition(label='Design Layout'),
        Transition(label='Install HVAC'),
        Transition(label='Set Lighting'),
        Transition(label='Build Racks'),
        Transition(label='Install Hydroponics'),
        Transition(label='Configure Sensors'),
        Transition(label='Select Crops'),
        Transition(label='Seed Planting'),
        Transition(label='Monitor Growth'),
        Transition(label='Nutrient Mixing'),
        Transition(label='Staff Training'),
        Transition(label='Market Launch'),
        Transition(label='Waste Recycling'),
        Transition(label='Customer Onboarding')
    ],
    order=[
        ('Site Survey', 'Structural Audit'),
        ('Structural Audit', 'Permit Filing'),
        ('Permit Filing', 'Design Layout'),
        ('Design Layout', 'Install HVAC'),
        ('Install HVAC', 'Set Lighting'),
        ('Set Lighting', 'Build Racks'),
        ('Build Racks', 'Install Hydroponics'),
        ('Install Hydroponics', 'Configure Sensors'),
        ('Configure Sensors', 'Select Crops'),
        ('Select Crops', 'Seed Planting'),
        ('Seed Planting', 'Monitor Growth'),
        ('Monitor Growth', 'Nutrient Mixing'),
        ('Nutrient Mixing', 'Staff Training'),
        ('Staff Training', 'Market Launch'),
        ('Market Launch', 'Waste Recycling'),
        ('Waste Recycling', 'Customer Onboarding')
    ]
)