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

# Define the partial order model
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

# Define the order dependencies
root.order.add_edge(Site_Assess, Load_Testing)
root.order.add_edge(Load_Testing, Climate_Study)
root.order.add_edge(Climate_Study, Medium_Prep)
root.order.add_edge(Medium_Prep, Bed_Install)
root.order.add_edge(Bed_Install, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Crop_Select)
root.order.add_edge(Crop_Select, Pest_Control)
root.order.add_edge(Pest_Control, Community_Meet)
root.order.add_edge(Community_Meet, Monitor_Deploy)
root.order.add_edge(Monitor_Deploy, Waste_Cycle)
root.order.add_edge(Waste_Cycle, Yield_Forecast)
root.order.add_edge(Yield_Forecast, Market_Link)
root.order.add_edge(Market_Link, Workshop_Plan)
root.order.add_edge(Workshop_Plan, Tech_Integrate)

# Print the root model
print(root)