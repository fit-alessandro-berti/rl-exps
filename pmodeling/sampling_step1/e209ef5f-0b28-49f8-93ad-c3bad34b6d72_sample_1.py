import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Soil_Analyze = Transition(label='Soil Analyze')
Site_Mapping = Transition(label='Site Mapping')
Bed_Setup = Transition(label='Bed Setup')
Crop_Select = Transition(label='Crop Select')
Sensor_Deploy = Transition(label='Sensor Deploy')
Irrigation_Adjust = Transition(label='Irrigation Adjust')
Nutrient_Feed = Transition(label='Nutrient Feed')
Pest_Scouting = Transition(label='Pest Scouting')
Pest_Predict = Transition(label='Pest Predict')
Workshop_Host = Transition(label='Workshop Host')
Crop_Rotate = Transition(label='Crop Rotate')
Waste_Compost = Transition(label='Waste Compost')
Water_Recycle = Transition(label='Water Recycle')
Data_Analyze = Transition(label='Data Analyze')
Cycle_Refine = Transition(label='Cycle Refine')
Resource_Share = Transition(label='Resource Share')
Yield_Report = Transition(label='Yield Report')

# Define the partial order
root = StrictPartialOrder(nodes=[Soil_Analyze, Site_Mapping, Bed_Setup, Crop_Select, Sensor_Deploy, Irrigation_Adjust, Nutrient_Feed, Pest_Scouting, Pest_Predict, Workshop_Host, Crop_Rotate, Waste_Compost, Water_Recycle, Data_Analyze, Cycle_Refine, Resource_Share, Yield_Report])

# Define the dependencies (partial order edges)
root.order.add_edge(Soil_Analyze, Site_Mapping)
root.order.add_edge(Site_Mapping, Bed_Setup)
root.order.add_edge(Bed_Setup, Crop_Select)
root.order.add_edge(Crop_Select, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, Irrigation_Adjust)
root.order.add_edge(Irrigation_Adjust, Nutrient_Feed)
root.order.add_edge(Nutrient_Feed, Pest_Scouting)
root.order.add_edge(Pest_Scouting, Pest_Predict)
root.order.add_edge(Pest_Predict, Workshop_Host)
root.order.add_edge(Workshop_Host, Crop_Rotate)
root.order.add_edge(Crop_Rotate, Waste_Compost)
root.order.add_edge(Waste_Compost, Water_Recycle)
root.order.add_edge(Water_Recycle, Data_Analyze)
root.order.add_edge(Data_Analyze, Cycle_Refine)
root.order.add_edge(Cycle_Refine, Resource_Share)
root.order.add_edge(Resource_Share, Yield_Report)