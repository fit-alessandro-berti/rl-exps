from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Modular_Build = Transition(label='Modular Build')
Install_Pumps = Transition(label='Install Pumps')
Setup_Sensors = Transition(label='Setup Sensors')
Calibrate_Lights = Transition(label='Calibrate Lights')
Nutrient_Mix = Transition(label='Nutrient Mix')
Plant_Seeding = Transition(label='Plant Seeding')
Water_Cycling = Transition(label='Water Cycling')
Energy_Audit = Transition(label='Energy Audit')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Data_Analysis = Transition(label='Data Analysis')
Yield_Forecast = Transition(label='Yield Forecast')
Supply_Order = Transition(label='Supply Order')
Waste_Recycle = Transition(label='Waste Recycle')
System_Upgrade = Transition(label='System Upgrade')

root = StrictPartialOrder(nodes=[
    Site_Survey, Design_Layout, Modular_Build, Install_Pumps, Setup_Sensors, Calibrate_Lights, Nutrient_Mix,
    Plant_Seeding, Water_Cycling, Energy_Audit, Pest_Control, Growth_Monitor, Data_Analysis, Yield_Forecast,
    Supply_Order, Waste_Recycle, System_Upgrade
])

# Define the dependencies between activities
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Modular_Build)
root.order.add_edge(Modular_Build, Install_Pumps)
root.order.add_edge(Install_Pumps, Setup_Sensors)
root.order.add_edge(Setup_Sensors, Calibrate_Lights)
root.order.add_edge(Calibrate_Lights, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Plant_Seeding)
root.order.add_edge(Plant_Seeding, Water_Cycling)
root.order.add_edge(Water_Cycling, Energy_Audit)
root.order.add_edge(Energy_Audit, Pest_Control)
root.order.add_edge(Pest_Control, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Data_Analysis)
root.order.add_edge(Data_Analysis, Yield_Forecast)
root.order.add_edge(Yield_Forecast, Supply_Order)
root.order.add_edge(Supply_Order, Waste_Recycle)
root.order.add_edge(Waste_Recycle, System_Upgrade)