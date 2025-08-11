import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Climate_Study = Transition(label='Climate Study')
Permit_Check = Transition(label='Permit Check')
System_Design = Transition(label='System Design')
Equipment_Buy = Transition(label='Equipment Buy')
Sensor_Setup = Transition(label='Sensor Setup')
Irrigation_Fit = Transition(label='Irrigation Fit')
Solar_Install = Transition(label='Solar Install')
Staff_Train = Transition(label='Staff Train')
Pilot_Plant = Transition(label='Pilot Plant')
Data_Monitor = Transition(label='Data Monitor')
Crop_Harvest = Transition(label='Crop Harvest')
Maintenance_Plan = Transition(label='Maintenance Plan')
Community_Meet = Transition(label='Community Meet')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey,
    Load_Test,
    Climate_Study,
    Permit_Check,
    System_Design,
    Equipment_Buy,
    Sensor_Setup,
    Irrigation_Fit,
    Solar_Install,
    Staff_Train,
    Pilot_Plant,
    Data_Monitor,
    Crop_Harvest,
    Maintenance_Plan,
    Community_Meet
])

# Add dependencies
root.order.add_edge(Site_Survey, Load_Test)
root.order.add_edge(Load_Test, Climate_Study)
root.order.add_edge(Climate_Study, Permit_Check)
root.order.add_edge(Permit_Check, System_Design)
root.order.add_edge(System_Design, Equipment_Buy)
root.order.add_edge(Equipment_Buy, Sensor_Setup)
root.order.add_edge(Sensor_Setup, Irrigation_Fit)
root.order.add_edge(Irrigation_Fit, Solar_Install)
root.order.add_edge(Solar_Install, Staff_Train)
root.order.add_edge(Staff_Train, Pilot_Plant)
root.order.add_edge(Pilot_Plant, Data_Monitor)
root.order.add_edge(Data_Monitor, Crop_Harvest)
root.order.add_edge(Crop_Harvest, Maintenance_Plan)
root.order.add_edge(Maintenance_Plan, Community_Meet)

# Print the root
print(root)