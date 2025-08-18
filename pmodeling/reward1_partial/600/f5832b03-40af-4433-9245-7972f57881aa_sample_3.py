import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Legal_Review = Transition(label='Legal Review')
Tech_Sourcing = Transition(label='Tech Sourcing')
Structural_Build = Transition(label='Structural Build')
Climate_Setup = Transition(label='Climate Setup')
Irrigation_Install = Transition(label='Irrigation Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Crop_Select = Transition(label='Crop Select')
Nutrient_Prep = Transition(label='Nutrient Prep')
Waste_System = Transition(label='Waste System')
Automation_Config = Transition(label='Automation Config')
Trial_Growth = Transition(label='Trial Growth')
Data_Analysis = Transition(label='Data Analysis')
Quality_Audit = Transition(label='Quality Audit')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Compliance_Check = Transition(label='Compliance Check')

# Define the partial order and dependencies
root = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Legal_Review, Tech_Sourcing, Structural_Build, Climate_Setup, Irrigation_Install, Sensor_Deploy, Crop_Select, Nutrient_Prep, Waste_System, Automation_Config, Trial_Growth, Data_Analysis, Quality_Audit, Stakeholder_Meet, Compliance_Check])

# Define the dependencies
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Legal_Review)
root.order.add_edge(Legal_Review, Tech_Sourcing)
root.order.add_edge(Tech_Sourcing, Structural_Build)
root.order.add_edge(Structural_Build, Climate_Setup)
root.order.add_edge(Climate_Setup, Irrigation_Install)
root.order.add_edge(Irrigation_Install, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, Crop_Select)
root.order.add_edge(Crop_Select, Nutrient_Prep)
root.order.add_edge(Nutrient_Prep, Waste_System)
root.order.add_edge(Waste_System, Automation_Config)
root.order.add_edge(Automation_Config, Trial_Growth)
root.order.add_edge(Trial_Growth, Data_Analysis)
root.order.add_edge(Data_Analysis, Quality_Audit)
root.order.add_edge(Quality_Audit, Stakeholder_Meet)
root.order.add_edge(Stakeholder_Meet, Compliance_Check)

# Print the POWL model
print(root)