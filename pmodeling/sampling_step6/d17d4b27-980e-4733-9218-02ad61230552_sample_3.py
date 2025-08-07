import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_analysis = Transition(label='Site Analysis')
zoning_review = Transition(label='Zoning Review')
modular_design = Transition(label='Modular Design')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
ai_monitoring = Transition(label='AI Monitoring')
lighting_control = Transition(label='Lighting Control')
energy_audit = Transition(label='Energy Audit')
water_reclaim = Transition(label='Water Reclaim')
waste_sorting = Transition(label='Waste Sorting')
community_meet = Transition(label='Community Meet')
staff_training = Transition(label='Staff Training')
yield_forecast = Transition(label='Yield Forecast')
market_sync = Transition(label='Market Sync')
supply_chain = Transition(label='Supply Chain')

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    zoning_review,
    modular_design,
    climate_setup,
    nutrient_mix,
    seed_selection,
    ai_monitoring,
    lighting_control,
    energy_audit,
    water_reclaim,
    waste_sorting,
    community_meet,
    staff_training,
    yield_forecast,
    market_sync,
    supply_chain
])

# Define the dependencies between activities (if any)
# In this case, there are no explicit dependencies mentioned, so we don't need to add any edges.

print(root)