from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = ['Site Survey', 'Design Layout', 'System Build', 'Install Sensors', 'Select Crops', 'Setup Lighting', 'Configure Climate', 'Nutrient Mix', 'Automate Watering', 'Test Systems', 'Train Staff', 'Waste Plan', 'Market Link', 'Data Monitor', 'Optimize Yield']

# Create the transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Create the loop for the installation and testing of systems
loop_install_test = OperatorPOWL(operator=Operator.LOOP, children=[transitions['Install Sensors'], transitions['Test Systems']])

# Create the XOR for the selection of crops and staff training
xor_crop_training = OperatorPOWL(operator=Operator.XOR, children=[transitions['Select Crops'], transitions['Train Staff']])

# Create the loop for the nutrient mixing and watering
loop_nutrient_watering = OperatorPOWL(operator=Operator.LOOP, children=[transitions['Nutrient Mix'], transitions['Automate Watering']])

# Create the XOR for the waste plan and market link
xor_waste_market = OperatorPOWL(operator=Operator.XOR, children=[transitions['Waste Plan'], transitions['Market Link']])

# Create the XOR for the data monitoring and yield optimization
xor_data_optimize = OperatorPOWL(operator=Operator.XOR, children=[transitions['Data Monitor'], transitions['Optimize Yield']])

# Create the root node with the dependencies
root = StrictPartialOrder(nodes=[loop_install_test, xor_crop_training, loop_nutrient_watering, xor_waste_market, xor_data_optimize])
root.order.add_edge(loop_install_test, xor_crop_training)
root.order.add_edge(loop_install_test, loop_nutrient_watering)
root.order.add_edge(xor_crop_training, xor_waste_market)
root.order.add_edge(xor_crop_training, xor_data_optimize)
root.order.add_edge(loop_nutrient_watering, xor_waste_market)
root.order.add_edge(loop_nutrient_watering, xor_data_optimize)

# Print the root node
print(root)