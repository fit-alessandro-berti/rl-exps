root = StrictPartialOrder(
    nodes=[
        Transition(label='Scan Markets'),
        Transition(label='Host Workshops'),
        Transition(label='Form Teams'),
        Transition(label='Develop Prototypes'),
        Transition(label='Simulate Tests'),
        Transition(label='Collect Feedback'),
        Transition(label='Review Ethics'),
        Transition(label='Conduct Analysis'),
        Transition(label='Identify Partners'),
        Transition(label='Align Strategy'),
        Transition(label='Launch Pilots'),
        Transition(label='Monitor Trends'),
        Transition(label='AI Analytics'),
        Transition(label='Pivot Plans'),
        Transition(label='Cycle Renewal')
    ],
    order=[
        (Transition(label='Scan Markets'), Transition(label='Host Workshops')),
        (Transition(label='Host Workshops'), Transition(label='Form Teams')),
        (Transition(label='Form Teams'), Transition(label='Develop Prototypes')),
        (Transition(label='Develop Prototypes'), Transition(label='Simulate Tests')),
        (Transition(label='Simulate Tests'), Transition(label='Collect Feedback')),
        (Transition(label='Collect Feedback'), Transition(label='Review Ethics')),
        (Transition(label='Review Ethics'), Transition(label='Conduct Analysis')),
        (Transition(label='Conduct Analysis'), Transition(label='Identify Partners')),
        (Transition(label='Identify Partners'), Transition(label='Align Strategy')),
        (Transition(label='Align Strategy'), Transition(label='Launch Pilots')),
        (Transition(label='Launch Pilots'), Transition(label='Monitor Trends')),
        (Transition(label='Monitor Trends'), Transition(label='AI Analytics')),
        (Transition(label='AI Analytics'), Transition(label='Pivot Plans')),
        (Transition(label='Pivot Plans'), Transition(label='Cycle Renewal')),
        (Transition(label='Cycle Renewal'), Transition(label='Scan Markets'))
    ]
)