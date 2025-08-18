root = StrictPartialOrder(
    nodes=[
        Transition(label='Threat Assess'),
        Transition(label='Alert Dispatch'),
        Transition(label='Resource Check'),
        Transition(label='Team Mobilize'),
        Transition(label='Command Setup'),
        Transition(label='Intel Gather'),
        Transition(label='Risk Evaluate'),
        Transition(label='Priority Set'),
        Transition(label='Field Deploy'),
        Transition(label='Comm Sync'),
        Transition(label='Public Update'),
        Transition(label='Supply Manage'),
        Transition(label='Safety Monitor'),
        Transition(label='Incident Log'),
        Transition(label='Recovery Plan'),
        Transition(label='Debrief Team'),
        Transition(label='Data Archive')
    ],
    order=[
        (Transition(label='Threat Assess'), Transition(label='Alert Dispatch')),
        (Transition(label='Alert Dispatch'), Transition(label='Resource Check')),
        (Transition(label='Resource Check'), Transition(label='Team Mobilize')),
        (Transition(label='Team Mobilize'), Transition(label='Command Setup')),
        (Transition(label='Command Setup'), Transition(label='Intel Gather')),
        (Transition(label='Intel Gather'), Transition(label='Risk Evaluate')),
        (Transition(label='Risk Evaluate'), Transition(label='Priority Set')),
        (Transition(label='Priority Set'), Transition(label='Field Deploy')),
        (Transition(label='Field Deploy'), Transition(label='Comm Sync')),
        (Transition(label='Comm Sync'), Transition(label='Public Update')),
        (Transition(label='Public Update'), Transition(label='Supply Manage')),
        (Transition(label='Supply Manage'), Transition(label='Safety Monitor')),
        (Transition(label='Safety Monitor'), Transition(label='Incident Log')),
        (Transition(label='Incident Log'), Transition(label='Recovery Plan')),
        (Transition(label='Recovery Plan'), Transition(label='Debrief Team')),
        (Transition(label='Debrief Team'), Transition(label='Data Archive'))
    ]
)