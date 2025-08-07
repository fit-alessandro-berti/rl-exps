import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root POWL model
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

# Note: Since there are no dependencies or transitions between activities in this case, the 'root' variable is already the complete POWL model.