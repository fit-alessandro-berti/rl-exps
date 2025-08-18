import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
Site_Survey = Transition(label='Site Survey')
Climate_Study = Transition(label='Climate Study')
Design_Layout = Transition(label='Design Layout')
System_Install = Transition(label='System Install')
Crop_Select = Transition(label='Crop Select')
Nutrient_Plan = Transition(label='Nutrient Plan')
Sensor_Setup = Transition(label='Sensor Setup')
Automation_Test = Transition(label='Automation Test')
Staff_Train = Transition(label='Staff Train')
Compliance_Check = Transition(label='Compliance Check')
Marketing_Sync = Transition(label='Marketing Sync')
Data_Monitor = Transition(label='Data Monitor')
Yield_Analyze = Transition(label='Yield Analyze')
Supply_Chain = Transition(label='Supply Chain')
Customer_Engage = Transition(label='Customer Engage')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey,
    Climate_Study,
    Design_Layout,
    System_Install,
    Crop_Select,
    Nutrient_Plan,
    Sensor_Setup,
    Automation_Test,
    Staff_Train,
    Compliance_Check,
    Marketing_Sync,
    Data_Monitor,
    Yield_Analyze,
    Supply_Chain,
    Customer_Engage
])

# Define the dependencies (edges) between the transitions
root.order.add_edge(Site_Survey, Climate_Study)
root.order.add_edge(Climate_Study, Design_Layout)
root.order.add_edge(Design_Layout, System_Install)
root.order.add_edge(System_Install, Crop_Select)
root.order.add_edge(Crop_Select, Nutrient_Plan)
root.order.add_edge(Nutrient_Plan, Sensor_Setup)
root.order.add_edge(Sensor_Setup, Automation_Test)
root.order.add_edge(Automation_Test, Staff_Train)
root.order.add_edge(Staff_Train, Compliance_Check)
root.order.add_edge(Compliance_Check, Marketing_Sync)
root.order.add_edge(Marketing_Sync, Data_Monitor)
root.order.add_edge(Data_Monitor, Yield_Analyze)
root.order.add_edge(Yield_Analyze, Supply_Chain)
root.order.add_edge(Supply_Chain, Customer_Engage)

print(root)