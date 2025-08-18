from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their exact labels
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Climate_Setup = Transition(label='Climate Setup')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automation_Code = Transition(label='Automation Code')
Crop_Planning = Transition(label='Crop Planning')
Pest_Control = Transition(label='Pest Control')
Energy_Audit = Transition(label='Energy Audit')
Waste_Sort = Transition(label='Waste Sort')
Planting_Tier = Transition(label='Planting Tier')
Harvest_Preparation = Transition(label='Harvest Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Community_Meet = Transition(label='Community Meet')
Data_Review = Transition(label='Data Review')
System_Upgrade = Transition(label='System Upgrade')

# Create the partial order structure
root = StrictPartialOrder(nodes=[
    Site_Survey,
    Design_Layout,
    Climate_Setup,
    Sensor_Install,
    Nutrient_Mix,
    Automation_Code,
    Crop_Planning,
    Pest_Control,
    Energy_Audit,
    Waste_Sort,
    Planting_Tier,
    Harvest_Preparation,
    Logistics_Plan,
    Community_Meet,
    Data_Review,
    System_Upgrade
])

# Define the dependencies (partial order edges) between the activities
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Climate_Setup)
root.order.add_edge(Climate_Setup, Sensor_Install)
root.order.add_edge(Sensor_Install, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Automation_Code)
root.order.add_edge(Automation_Code, Crop_Planning)
root.order.add_edge(Crop_Planning, Pest_Control)
root.order.add_edge(Pest_Control, Energy_Audit)
root.order.add_edge(Energy_Audit, Waste_Sort)
root.order.add_edge(Waste_Sort, Planting_Tier)
root.order.add_edge(Planting_Tier, Harvest_Preparation)
root.order.add_edge(Harvest_Preparation, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Community_Meet)
root.order.add_edge(Community_Meet, Data_Review)
root.order.add_edge(Data_Review, System_Upgrade)

print(root)