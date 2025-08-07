import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
Site_Assess = Transition(label='Site Assess')
Structure_Check = Transition(label='Structure Check')
Soil_Test = Transition(label='Soil Test')
Climate_Eval = Transition(label='Climate Eval')
Permit_Obtain = Transition(label='Permit Obtain')
Design_Layout = Transition(label='Design Layout')
Seed_Sourcing = Transition(label='Seed Sourcing')
Irrigation_Set = Transition(label='Irrigation Set')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Control = Transition(label='Pest Control')
Sensor_Install = Transition(label='Sensor Install')
Staff_Train = Transition(label='Staff Train')
Crop_Planting = Transition(label='Crop Planting')
Yield_Monitor = Transition(label='Yield Monitor')
Market_Setup = Transition(label='Market Setup')
Maintenance = Transition(label='Maintenance')
Waste_Manage = Transition(label='Waste Manage')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Assess,
    Structure_Check,
    Soil_Test,
    Climate_Eval,
    Permit_Obtain,
    Design_Layout,
    Seed_Sourcing,
    Irrigation_Set,
    Nutrient_Mix,
    Pest_Control,
    Sensor_Install,
    Staff_Train,
    Crop_Planting,
    Yield_Monitor,
    Market_Setup,
    Maintenance,
    Waste_Manage
])

# Define the order dependencies
root.order.add_edge(Site_Assess, Structure_Check)
root.order.add_edge(Structure_Check, Soil_Test)
root.order.add_edge(Soil_Test, Climate_Eval)
root.order.add_edge(Climate_Eval, Permit_Obtain)
root.order.add_edge(Permit_Obtain, Design_Layout)
root.order.add_edge(Design_Layout, Seed_Sourcing)
root.order.add_edge(Seed_Sourcing, Irrigation_Set)
root.order.add_edge(Irrigation_Set, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Pest_Control)
root.order.add_edge(Pest_Control, Sensor_Install)
root.order.add_edge(Sensor_Install, Staff_Train)
root.order.add_edge(Staff_Train, Crop_Planting)
root.order.add_edge(Crop_Planting, Yield_Monitor)
root.order.add_edge(Yield_Monitor, Market_Setup)
root.order.add_edge(Market_Setup, Maintenance)
root.order.add_edge(Maintenance, Waste_Manage)

print(root)