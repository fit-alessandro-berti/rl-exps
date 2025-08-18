root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Energy Partner'),
        Transition(label='Permit Filing'),
        Transition(label='Hydro Unit'),
        Transition(label='AI Setup'),
        Transition(label='Nutrient Plan'),
        Transition(label='System Install'),
        Transition(label='Crop Testing'),
        Transition(label='Data Analysis'),
        Transition(label='Community Meet'),
        Transition(label='Yield Adjust'),
        Transition(label='Carbon Audit'),
        Transition(label='Logistics Plan'),
        Transition(label='Quality Check'),
        Transition(label='Scale Review')
    ],
    order=[
        (Transition(label='Site Survey'), Transition(label='Energy Partner')),
        (Transition(label='Energy Partner'), Transition(label='Permit Filing')),
        (Transition(label='Permit Filing'), Transition(label='Hydro Unit')),
        (Transition(label='Hydro Unit'), Transition(label='AI Setup')),
        (Transition(label='AI Setup'), Transition(label='Nutrient Plan')),
        (Transition(label='Nutrient Plan'), Transition(label='System Install')),
        (Transition(label='System Install'), Transition(label='Crop Testing')),
        (Transition(label='Crop Testing'), Transition(label='Data Analysis')),
        (Transition(label='Data Analysis'), Transition(label='Community Meet')),
        (Transition(label='Community Meet'), Transition(label='Yield Adjust')),
        (Transition(label='Yield Adjust'), Transition(label='Carbon Audit')),
        (Transition(label='Carbon Audit'), Transition(label='Logistics Plan')),
        (Transition(label='Logistics Plan'), Transition(label='Quality Check')),
        (Transition(label='Quality Check'), Transition(label='Scale Review'))
    ]
)