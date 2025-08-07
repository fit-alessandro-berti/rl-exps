import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Select = Transition(label='Site Select')
Env_Assess = Transition(label='Env Assess')
Design_Modules = Transition(label='Design Modules')
Hydroponics_Setup = Transition(label='Hydroponics Setup')
Software_Dev = Transition(label='Software Dev')
Seed_Choose = Transition(label='Seed Choose')
LED_Install = Transition(label='LED Install')
Train_Staff = Transition(label='Train Staff')
Compliance_Check = Transition(label='Compliance Check')
Engage_Community = Transition(label='Engage Community')
Plant_Crops = Transition(label='Plant Crops')
Monitor_Growth = Transition(label='Monitor Growth')
Optimize_Yields = Transition(label='Optimize Yields')
Waste_Manage = Transition(label='Waste Manage')
Energy_Audit = Transition(label='Energy Audit')
Water_Recycle = Transition(label='Water Recycle')

# Create a partial order model
root = StrictPartialOrder(nodes=[
    Site_Select,
    Env_Assess,
    Design_Modules,
    Hydroponics_Setup,
    Software_Dev,
    Seed_Choose,
    LED_Install,
    Train_Staff,
    Compliance_Check,
    Engage_Community,
    Plant_Crops,
    Monitor_Growth,
    Optimize_Yields,
    Waste_Manage,
    Energy_Audit,
    Water_Recycle
])

# Optionally, add dependencies if needed (not shown in this simplified example)