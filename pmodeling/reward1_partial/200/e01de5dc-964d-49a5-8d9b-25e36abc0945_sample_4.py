import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
Seed_Select = Transition(label='Seed Select')
Germinate_Seeds = Transition(label='Germinate Seeds')
Transplant_Seedlings = Transition(label='Transplant Seedlings')
Mix_Nutrients = Transition(label='Mix Nutrients')
Adjust_pH = Transition(label='Adjust pH')
Monitor_Climate = Transition(label='Monitor Climate')
Control_Humidity = Transition(label='Control Humidity')
CO2_Regulation = Transition(label='CO2 Regulation')
Detect_Pests = Transition(label='Detect Pests')
Deploy_Biocontrols = Transition(label='Deploy Biocontrols')
Schedule_Harvest = Transition(label='Schedule Harvest')
Automate_Picking = Transition(label='Automate Picking')
Package_Produce = Transition(label='Package Produce')
Compost_Waste = Transition(label='Compost Waste')
Recycle_Water = Transition(label='Recycle Water')
Data_Logging = Transition(label='Data Logging')
System_Maintenance = Transition(label='System Maintenance')

# Define silent transitions
Skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Seed_Select, Germinate_Seeds, Transplant_Seedlings, Mix_Nutrients, Adjust_pH, Monitor_Climate, Control_Humidity, CO2_Regulation])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Detect_Pests, Deploy_Biocontrols, Schedule_Harvest, Automate_Picking])
xor = OperatorPOWL(operator=Operator.XOR, children=[Package_Produce, Compost_Waste, Recycle_Water])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Data_Logging, System_Maintenance])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor, xor2])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)

# Print the root POWL model
print(root)