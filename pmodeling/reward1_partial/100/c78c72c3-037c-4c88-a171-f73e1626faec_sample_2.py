from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the urban vertical farm process
root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Design Layout'),
        Transition(label='System Build'),
        Transition(label='Install Sensors'),
        Transition(label='Set Controls'),
        Transition(label='Test Modules'),
        Transition(label='Select Crops'),
        Transition(label='Configure Irrigation'),
        Transition(label='Deploy AI'),
        Transition(label='Monitor Pests'),
        Transition(label='Manage Energy'),
        Transition(label='Recycle Waste'),
        Transition(label='Train Staff'),
        Transition(label='Launch Market'),
        Transition(label='Engage Community')
    ],
    order=[
        # Site Survey -> Design Layout
        ('Site Survey', 'Design Layout'),
        # Design Layout -> System Build
        ('Design Layout', 'System Build'),
        # System Build -> Install Sensors
        ('System Build', 'Install Sensors'),
        # Install Sensors -> Set Controls
        ('Install Sensors', 'Set Controls'),
        # Set Controls -> Test Modules
        ('Set Controls', 'Test Modules'),
        # Test Modules -> Select Crops
        ('Test Modules', 'Select Crops'),
        # Select Crops -> Configure Irrigation
        ('Select Crops', 'Configure Irrigation'),
        # Configure Irrigation -> Deploy AI
        ('Configure Irrigation', 'Deploy AI'),
        # Deploy AI -> Monitor Pests
        ('Deploy AI', 'Monitor Pests'),
        # Monitor Pests -> Manage Energy
        ('Monitor Pests', 'Manage Energy'),
        # Manage Energy -> Recycle Waste
        ('Manage Energy', 'Recycle Waste'),
        # Recycle Waste -> Train Staff
        ('Recycle Waste', 'Train Staff'),
        # Train Staff -> Launch Market
        ('Train Staff', 'Launch Market'),
        # Launch Market -> Engage Community
        ('Launch Market', 'Engage Community')
    ]
)