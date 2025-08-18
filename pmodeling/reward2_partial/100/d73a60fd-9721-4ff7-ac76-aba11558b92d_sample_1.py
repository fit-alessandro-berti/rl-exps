import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
System_Design = Transition(label='System Design')
Permit_Filing = Transition(label='Permit Filing')
Foundation_Prep = Transition(label='Foundation Prep')
Frame_Build = Transition(label='Frame Build')
Irrigation_Setup = Transition(label='Irrigation Setup')
Lighting_Install = Transition(label='Lighting Install')
Climate_Control = Transition(label='Climate Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Planting = Transition(label='Crop Planting')
Pest_Scouting = Transition(label='Pest Scouting')
Data_Monitoring = Transition(label='Data Monitoring')
Waste_Sorting = Transition(label='Waste Sorting')
Energy_Audit = Transition(label='Energy Audit')
Community_Meet = Transition(label='Community Meet')
Yield_Analysis = Transition(label='Yield Analysis')

# Define the POWL structure
root = StrictPartialOrder(nodes=[
    Site_Survey,
    Structural_Audit,
    System_Design,
    Permit_Filing,
    Foundation_Prep,
    Frame_Build,
    Irrigation_Setup,
    Lighting_Install,
    Climate_Control,
    Nutrient_Mix,
    Crop_Planting,
    Pest_Scouting,
    Data_Monitoring,
    Waste_Sorting,
    Energy_Audit,
    Community_Meet,
    Yield_Analysis
])

# Define the order dependencies
root.order.add_edge(Site_Survey, Structural_Audit)
root.order.add_edge(Structural_Audit, System_Design)
root.order.add_edge(System_Design, Permit_Filing)
root.order.add_edge(Permit_Filing, Foundation_Prep)
root.order.add_edge(Foundation_Prep, Frame_Build)
root.order.add_edge(Frame_Build, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Lighting_Install)
root.order.add_edge(Lighting_Install, Climate_Control)
root.order.add_edge(Climate_Control, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Crop_Planting)
root.order.add_edge(Crop_Planting, Pest_Scouting)
root.order.add_edge(Pest_Scouting, Data_Monitoring)
root.order.add_edge(Data_Monitoring, Waste_Sorting)
root.order.add_edge(Waste_Sorting, Energy_Audit)
root.order.add_edge(Energy_Audit, Community_Meet)
root.order.add_edge(Community_Meet, Yield_Analysis)

print(root)