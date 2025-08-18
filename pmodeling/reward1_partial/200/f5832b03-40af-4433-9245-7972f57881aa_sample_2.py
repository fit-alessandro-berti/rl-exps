root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Design Layout'),
        Transition(label='Legal Review'),
        Transition(label='Tech Sourcing'),
        Transition(label='Structural Build'),
        Transition(label='Climate Setup'),
        Transition(label='Irrigation Install'),
        Transition(label='Sensor Deploy'),
        Transition(label='Crop Select'),
        Transition(label='Nutrient Prep'),
        Transition(label='Waste System'),
        Transition(label='Automation Config'),
        Transition(label='Trial Growth'),
        Transition(label='Data Analysis'),
        Transition(label='Quality Audit'),
        Transition(label='Stakeholder Meet'),
        Transition(label='Compliance Check')
    ],
    order=[
        ('Site Survey', 'Design Layout'),
        ('Design Layout', 'Legal Review'),
        ('Legal Review', 'Tech Sourcing'),
        ('Tech Sourcing', 'Structural Build'),
        ('Structural Build', 'Climate Setup'),
        ('Climate Setup', 'Irrigation Install'),
        ('Irrigation Install', 'Sensor Deploy'),
        ('Sensor Deploy', 'Crop Select'),
        ('Crop Select', 'Nutrient Prep'),
        ('Nutrient Prep', 'Waste System'),
        ('Waste System', 'Automation Config'),
        ('Automation Config', 'Trial Growth'),
        ('Trial Growth', 'Data Analysis'),
        ('Data Analysis', 'Quality Audit'),
        ('Quality Audit', 'Stakeholder Meet'),
        ('Stakeholder Meet', 'Compliance Check')
    ]
)