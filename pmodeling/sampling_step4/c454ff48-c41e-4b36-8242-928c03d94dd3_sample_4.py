from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
Site_Assess = Transition(label='Site Assess')
Permit_Obtain = Transition(label='Permit Obtain')
Soil_Testing = Transition(label='Soil Testing')
Crop_Select = Transition(label='Crop Select')
Irrigation_Setup = Transition(label='Irrigation Setup')
Drainage_Install = Transition(label='Drainage Install')
Energy_Integrate = Transition(label='Energy Integrate')
Staff_Train = Transition(label='Staff Train')
Pest_Control = Transition(label='Pest Control')
Logistics_Plan = Transition(label='Logistics Plan')
Supply_Coordinate = Transition(label='Supply Coordinate')
Distribution_Map = Transition(label='Distribution Map')
Community_Engage = Transition(label='Community Engage')
Monitoring_Setup = Transition(label='Monitoring Setup')
Yield_Optimize = Transition(label='Yield Optimize')

# Define the POWL model
root = StrictPartialOrder(nodes=[Site_Assess, Permit_Obtain, Soil_Testing, Crop_Select, Irrigation_Setup, Drainage_Install, Energy_Integrate, Staff_Train, Pest_Control, Logistics_Plan, Supply_Coordinate, Distribution_Map, Community_Engage, Monitoring_Setup, Yield_Optimize])

# Define the order dependencies
root.order.add_edge(Site_Assess, Permit_Obtain)
root.order.add_edge(Permit_Obtain, Soil_Testing)
root.order.add_edge(Soil_Testing, Crop_Select)
root.order.add_edge(Crop_Select, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Drainage_Install)
root.order.add_edge(Drainage_Install, Energy_Integrate)
root.order.add_edge(Energy_Integrate, Staff_Train)
root.order.add_edge(Staff_Train, Pest_Control)
root.order.add_edge(Pest_Control, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Supply_Coordinate)
root.order.add_edge(Supply_Coordinate, Distribution_Map)
root.order.add_edge(Distribution_Map, Community_Engage)
root.order.add_edge(Community_Engage, Monitoring_Setup)
root.order.add_edge(Monitoring_Setup, Yield_Optimize)

# Print the final result
print(root)