import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Design Layout', 'System Build', 'Install Sensors', 'Set Controls', 'Test Modules', 'Select Crops', 'Configure Irrigation', 'Deploy AI', 'Monitor Pests', 'Manage Energy', 'Recycle Waste', 'Train Staff', 'Launch Market', 'Engage Community']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the process
# Site Survey
# Design Layout
# System Build
# Install Sensors
# Set Controls
# Test Modules
# Select Crops
# Configure Irrigation
# Deploy AI
# Monitor Pests
# Manage Energy
# Recycle Waste
# Train Staff
# Launch Market
# Engage Community

# Define the dependencies
dependencies = [
    ('Site Survey', 'Design Layout'),
    ('Design Layout', 'System Build'),
    ('System Build', 'Install Sensors'),
    ('Install Sensors', 'Set Controls'),
    ('Set Controls', 'Test Modules'),
    ('Test Modules', 'Select Crops'),
    ('Select Crops', 'Configure Irrigation'),
    ('Configure Irrigation', 'Deploy AI'),
    ('Deploy AI', 'Monitor Pests'),
    ('Monitor Pests', 'Manage Energy'),
    ('Manage Energy', 'Recycle Waste'),
    ('Recycle Waste', 'Train Staff'),
    ('Train Staff', 'Launch Market'),
    ('Launch Market', 'Engage Community')
]

# Create the root node
root = StrictPartialOrder(nodes=transitions, order=dependencies)

# Print the root node
print(root)