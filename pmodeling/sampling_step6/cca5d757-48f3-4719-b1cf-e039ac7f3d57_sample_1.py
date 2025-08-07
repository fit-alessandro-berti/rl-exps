import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Assess = Transition(label='Site Assess')
Load_Testing = Transition(label='Load Testing')
Climate_Study = Transition(label='Climate Study')
Medium_Prep = Transition(label='Medium Prep')
Bed_Install = Transition(label='Bed Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Crop_Select = Transition(label='Crop Select')
Pest_Control = Transition(label='Pest Control')
Community_Meet = Transition(label='Community Meet')
Monitor_Deploy = Transition(label='Monitor Deploy')
Waste_Cycle = Transition(label='Waste Cycle')
Yield_Forecast = Transition(label='Yield Forecast')
Market_Link = Transition(label='Market Link')
Workshop_Plan = Transition(label='Workshop Plan')
Tech_Integrate = Transition(label='Tech Integrate')

# Define the root POWL model as a strict partial order
root = StrictPartialOrder(nodes=[
    Site_Assess,
    Load_Testing,
    Climate_Study,
    Medium_Prep,
    Bed_Install,
    Irrigation_Setup,
    Crop_Select,
    Pest_Control,
    Community_Meet,
    Monitor_Deploy,
    Waste_Cycle,
    Yield_Forecast,
    Market_Link,
    Workshop_Plan,
    Tech_Integrate
])

# Optionally, you can define dependencies if they exist
# For example, Site_Assess might need to happen before Load_Testing
# root.order.add_edge(Site_Assess, Load_Testing)

print(root)