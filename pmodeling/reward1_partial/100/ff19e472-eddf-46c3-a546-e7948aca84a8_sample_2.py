import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their labels
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Install_Modules = Transition(label='Install Modules')
Calibrate_Climate = Transition(label='Calibrate Climate')
Prepare_Nutrients = Transition(label='Prepare Nutrients')
Select_Seeds = Transition(label='Select Seeds')
Start_Germination = Transition(label='Start Germination')
Deploy_Sensors = Transition(label='Deploy Sensors')
Monitor_Growth = Transition(label='Monitor Growth')
Manage_Pests = Transition(label='Manage Pests')
Schedule_Harvest = Transition(label='Schedule Harvest')
Process_Waste = Transition(label='Process Waste')
Optimize_Energy = Transition(label='Optimize Energy')
Conduct_Training = Transition(label='Conduct Training')
Update_Records = Transition(label='Update Records')
Review_Performance = Transition(label='Review Performance')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey, Design_Layout, Install_Modules, Calibrate_Climate,
    Prepare_Nutrients, Select_Seeds, Start_Germination, Deploy_Sensors,
    Monitor_Growth, Manage_Pests, Schedule_Harvest, Process_Waste,
    Optimize_Energy, Conduct_Training, Update_Records, Review_Performance
])

# Add dependencies between transitions
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Install_Modules)
root.order.add_edge(Install_Modules, Calibrate_Climate)
root.order.add_edge(Calibrate_Climate, Prepare_Nutrients)
root.order.add_edge(Prepare_Nutrients, Select_Seeds)
root.order.add_edge(Select_Seeds, Start_Germination)
root.order.add_edge(Start_Germination, Deploy_Sensors)
root.order.add_edge(Deploy_Sensors, Monitor_Growth)
root.order.add_edge(Monitor_Growth, Manage_Pests)
root.order.add_edge(Manage_Pests, Schedule_Harvest)
root.order.add_edge(Schedule_Harvest, Process_Waste)
root.order.add_edge(Process_Waste, Optimize_Energy)
root.order.add_edge(Optimize_Energy, Conduct_Training)
root.order.add_edge(Conduct_Training, Update_Records)
root.order.add_edge(Update_Records, Review_Performance)

# Print the root model
print(root)