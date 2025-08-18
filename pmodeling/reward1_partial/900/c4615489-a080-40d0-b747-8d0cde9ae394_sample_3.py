import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
Permit_Filing = Transition(label='Permit Filing')
Design_Layout = Transition(label='Design Layout')
Install_HVAC = Transition(label='Install HVAC')
Set_Lighting = Transition(label='Set Lighting')
Build_Racks = Transition(label='Build Racks')
Install_Hydroponics = Transition(label='Install Hydroponics')
Configure_Sensors = Transition(label='Configure Sensors')
Select_Crops = Transition(label='Select Crops')
Seed_Planting = Transition(label='Seed Planting')
Monitor_Growth = Transition(label='Monitor Growth')
Nutrient_Mixing = Transition(label='Nutrient Mixing')
Staff_Training = Transition(label='Staff Training')
Market_Launch = Transition(label='Market Launch')
Waste_Recycling = Transition(label='Waste Recycling')
Customer_Onboarding = Transition(label='Customer Onboarding')

# Define the process as a partial order
root = StrictPartialOrder(nodes=[
    Site_Survey,
    Structural_Audit,
    Permit_Filing,
    Design_Layout,
    Install_HVAC,
    Set_Lighting,
    Build_Racks,
    Install_Hydroponics,
    Configure_Sensors,
    Select_Crops,
    Seed_Planting,
    Monitor_Growth,
    Nutrient_Mixing,
    Staff_Training,
    Market_Launch,
    Waste_Recycling,
    Customer_Onboarding
])

# Define dependencies between activities (partial order)
root.order.add_edge(Site_Survey, Structural_Audit)
root.order.add_edge(Structural_Audit, Permit_Filing)
root.order.add_edge(Permit_Filing, Design_Layout)
root.order.add_edge(Design_Layout, Install_HVAC)
root.order.add_edge(Install_HVAC, Set_Lighting)
root.order.add_edge(Set_Lighting, Build_Racks)
root.order.add_edge(Build_Racks, Install_Hydroponics)
root.order.add_edge(Install_Hydroponics, Configure_Sensors)
root.order.add_edge(Configure_Sensors, Select_Crops)
root.order.add_edge(Select_Crops, Seed_Planting)
root.order.add_edge(Seed_Planting, Monitor_Growth)
root.order.add_edge(Monitor_Growth, Nutrient_Mixing)
root.order.add_edge(Nutrient_Mixing, Staff_Training)
root.order.add_edge(Staff_Training, Market_Launch)
root.order.add_edge(Market_Launch, Waste_Recycling)
root.order.add_edge(Waste_Recycling, Customer_Onboarding)