from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = ['Site Survey', 'Structural Audit', 'Permit Filing', 'Design Layout', 'Install HVAC', 'Set Lighting', 'Build Racks', 'Install Hydroponics', 'Configure Sensors', 'Select Crops', 'Seed Planting', 'Monitor Growth', 'Nutrient Mixing', 'Staff Training', 'Market Launch', 'Waste Recycling', 'Customer Onboarding']

# Create the POWL model
root = StrictPartialOrder(nodes=activities)
# Add dependencies based on the process description
root.order.add_edge('Site Survey', 'Structural Audit')
root.order.add_edge('Structural Audit', 'Permit Filing')
root.order.add_edge('Permit Filing', 'Design Layout')
root.order.add_edge('Design Layout', 'Install HVAC')
root.order.add_edge('Install HVAC', 'Set Lighting')
root.order.add_edge('Set Lighting', 'Build Racks')
root.order.add_edge('Build Racks', 'Install Hydroponics')
root.order.add_edge('Install Hydroponics', 'Configure Sensors')
root.order.add_edge('Configure Sensors', 'Select Crops')
root.order.add_edge('Select Crops', 'Seed Planting')
root.order.add_edge('Seed Planting', 'Monitor Growth')
root.order.add_edge('Monitor Growth', 'Nutrient Mixing')
root.order.add_edge('Nutrient Mixing', 'Staff Training')
root.order.add_edge('Staff Training', 'Market Launch')
root.order.add_edge('Market Launch', 'Waste Recycling')
root.order.add_edge('Waste Recycling', 'Customer Onboarding')

# Print the root to verify the model
print(root)