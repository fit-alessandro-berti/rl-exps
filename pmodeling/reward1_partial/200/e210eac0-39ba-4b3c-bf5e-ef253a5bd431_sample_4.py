import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
Site_Survey = Transition(label='Site Survey')
Regulation_Check = Transition(label='Regulation Check')
Modular_Design = Transition(label='Modular Design')
Material_Sourcing = Transition(label='Material Sourcing')
Energy_Integration = Transition(label='Energy Integration')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
System_Assembly = Transition(label='System Assembly')
Automation_Config = Transition(label='Automation Config')
Crop_Seeding = Transition(label='Crop Seeding')
Growth_Monitoring = Transition(label='Growth Monitoring')
Waste_Handling = Transition(label='Waste Handling')
Community_Meet = Transition(label='Community Meet')
Data_Analysis = Transition(label='Data Analysis')
Feedback_Loop = Transition(label='Feedback Loop')
Yield_Forecast = Transition(label='Yield Forecast')

# Define silent transitions
skip = SilentTransition()

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey, Regulation_Check, Modular_Design, Material_Sourcing, Energy_Integration, Climate_Setup,
    Nutrient_Mix, System_Assembly, Automation_Config, Crop_Seeding, Growth_Monitoring, Waste_Handling,
    Community_Meet, Data_Analysis, Feedback_Loop, Yield_Forecast
])

# Define the dependencies (order)
root.order.add_edge(Site_Survey, Regulation_Check)
root.order.add_edge(Regulation_Check, Modular_Design)
root.order.add_edge(Modular_Design, Material_Sourcing)
root.order.add_edge(Material_Sourcing, Energy_Integration)
root.order.add_edge(Energy_Integration, Climate_Setup)
root.order.add_edge(Climate_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, System_Assembly)
root.order.add_edge(System_Assembly, Automation_Config)
root.order.add_edge(Automation_Config, Crop_Seeding)
root.order.add_edge(Crop_Seeding, Growth_Monitoring)
root.order.add_edge(Growth_Monitoring, Waste_Handling)
root.order.add_edge(Waste_Handling, Community_Meet)
root.order.add_edge(Community_Meet, Data_Analysis)
root.order.add_edge(Data_Analysis, Feedback_Loop)
root.order.add_edge(Feedback_Loop, Yield_Forecast)

# Return the root of the POWL model
print(root)