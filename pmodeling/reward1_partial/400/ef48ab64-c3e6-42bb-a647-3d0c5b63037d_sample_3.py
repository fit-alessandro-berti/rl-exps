from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Create the POWL model
root = StrictPartialOrder(
    nodes=[
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
    ]
)

# Add edges to define the order of execution
root.order.add_edge(Site_Select, Env_Assess)
root.order.add_edge(Env_Assess, Design_Modules)
root.order.add_edge(Design_Modules, Hydroponics_Setup)
root.order.add_edge(Hydroponics_Setup, Software_Dev)
root.order.add_edge(Software_Dev, Seed_Choose)
root.order.add_edge(Seed_Choose, LED_Install)
root.order.add_edge(LED_Install, Train_Staff)
root.order.add_edge(Train_Staff, Compliance_Check)
root.order.add_edge(Compliance_Check, Engage_Community)
root.order.add_edge(Engage_Community, Plant_Crops)
root.order.add_edge(Plant_Crops, Monitor_Growth)
root.order.add_edge(Monitor_Growth, Optimize_Yields)
root.order.add_edge(Optimize_Yields, Waste_Manage)
root.order.add_edge(Waste_Manage, Energy_Audit)
root.order.add_edge(Energy_Audit, Water_Recycle)

print(root)