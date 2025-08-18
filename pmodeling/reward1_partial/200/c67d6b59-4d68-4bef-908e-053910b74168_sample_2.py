root = StrictPartialOrder(
    nodes=[
        Transition(label='Client Meet'),
        Transition(label='Design Draft'),
        Transition(label='Vendor Select'),
        Transition(label='Component Order'),
        Transition(label='Parts Inspect'),
        Transition(label='Frame Build'),
        Transition(label='Wiring Setup'),
        Transition(label='Software Load'),
        Transition(label='Flight Sim'),
        Transition(label='Quality Test'),
        Transition(label='Feedback Review'),
        Transition(label='Adjust Design'),
        Transition(label='Compliance Check'),
        Transition(label='Packaging Prep'),
        Transition(label='Final Demo'),
        Transition(label='Ship Drone')
    ],
    order={
        ('Client Meet', 'Design Draft'): None,
        ('Design Draft', 'Vendor Select'): None,
        ('Vendor Select', 'Component Order'): None,
        ('Component Order', 'Parts Inspect'): None,
        ('Parts Inspect', 'Frame Build'): None,
        ('Frame Build', 'Wiring Setup'): None,
        ('Wiring Setup', 'Software Load'): None,
        ('Software Load', 'Flight Sim'): None,
        ('Flight Sim', 'Quality Test'): None,
        ('Quality Test', 'Feedback Review'): None,
        ('Feedback Review', 'Adjust Design'): None,
        ('Adjust Design', 'Compliance Check'): None,
        ('Compliance Check', 'Packaging Prep'): None,
        ('Packaging Prep', 'Final Demo'): None,
        ('Final Demo', 'Ship Drone'): None
    }
)