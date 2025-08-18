import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
Site_Survey = Transition(label='Site Survey')
Load_Testing = Transition(label='Load Testing')
Crop_Selection = Transition(label='Crop Selection')
Soil_Preparation = Transition(label='Soil Prep')
Irrigation_Setup = Transition(label='Irrigation Setup')
Permits_Acquire = Transition(label='Permits Acquire')
Supplier_Outreach = Transition(label='Supplier Outreach')
Planting_Seedlings = Transition(label='Planting Seedlings')
Pest_Monitoring = Transition(label='Pest Monitoring')
Nutrient_Testing = Transition(label='Nutrient Testing')
Waste_Sorting = Transition(label='Waste Sorting')
Staff_Training = Transition(label='Staff Training')
Community_Meet = Transition(label='Community Meet')
Harvest_Planning = Transition(label='Harvest Planning')
Market_Launch = Transition(label='Market Launch')
Yield_Tracking = Transition(label='Yield Tracking')

# Define the partial order for the process
root = StrictPartialOrder(nodes=[
    Site_Survey, Load_Testing, Crop_Selection, Soil_Preparation, Irrigation_Setup, Permits_Acquire, Supplier_Outreach,
    Planting_Seedlings, Pest_Monitoring, Nutrient_Testing, Waste_Sorting, Staff_Training, Community_Meet, Harvest_Planning,
    Market_Launch, Yield_Tracking
])

# Add the order relationships between activities
root.order.add_edge(Site_Survey, Load_Testing)
root.order.add_edge(Load_Testing, Crop_Selection)
root.order.add_edge(Crop_Selection, Soil_Preparation)
root.order.add_edge(Soil_Preparation, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Permits_Acquire)
root.order.add_edge(Permits_Acquire, Supplier_Outreach)
root.order.add_edge(Supplier_Outreach, Planting_Seedlings)
root.order.add_edge(Planting_Seedlings, Pest_Monitoring)
root.order.add_edge(Pest_Monitoring, Nutrient_Testing)
root.order.add_edge(Nutrient_Testing, Waste_Sorting)
root.order.add_edge(Waste_Sorting, Staff_Training)
root.order.add_edge(Staff_Training, Community_Meet)
root.order.add_edge(Community_Meet, Harvest_Planning)
root.order.add_edge(Harvest_Planning, Market_Launch)
root.order.add_edge(Market_Launch, Yield_Tracking)

# Optionally, you can add silent transitions for clarity
root.order.add_edge(Permits_Acquire, Site_Survey)  # Assuming site survey is done before permits are acquired
root.order.add_edge(Community_Meet, Market_Launch)  # Assuming community meet is done before market launch