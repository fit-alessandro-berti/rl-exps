import pm4py

# Define transitions for each activity
site_survey = pm4py.objects.powl.obj.Transition(label='Site Survey')
system_design = pm4py.objects.powl.obj.Transition(label='System Design')
module_build = pm4py.objects.powl.obj.Transition(label='Module Build')
nutrient_mix = pm4py.objects.powl.obj.Transition(label='Nutrient Mix')
seed_selection = pm4py.objects.powl.obj.Transition(label='Seed Selection')
planting_plan = pm4py.objects.powl.obj.Transition(label='Planting Plan')
irrigation_setup = pm4py.objects.powl.obj.Transition(label='Irrigation Setup')
climate_control = pm4py.objects.powl.obj.Transition(label='Climate Control')
lighting_adjust = pm4py.objects.powl.obj.Transition(label='Lighting Adjust')
pest_monitor = pm4py.objects.powl.obj.Transition(label='Pest Monitor')
waste_cycle = pm4py.objects.powl.obj.Transition(label='Waste Cycle')
data_capture = pm4py.objects.powl.obj.Transition(label='Data Capture')
yield_forecast = pm4py.objects.powl.obj.Transition(label='Yield Forecast')
regulation_check = pm4py.objects.powl.obj.Transition(label='Regulation Check')
community_meet = pm4py.objects.powl.obj.Transition(label='Community Meet')
harvest_prep = pm4py.objects.powl.obj.Transition(label='Harvest Prep')
market_link = pm4py.objects.powl.obj.Transition(label='Market Link')

# Define the partial order structure
root = pm4py.objects.powl.obj.StrictPartialOrder(nodes=[
    site_survey, system_design, module_build, nutrient_mix, seed_selection, planting_plan,
    irrigation_setup, climate_control, lighting_adjust, pest_monitor, waste_cycle,
    data_capture, yield_forecast, regulation_check, community_meet, harvest_prep, market_link
])

# Add edges representing the workflow
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, module_build)
root.order.add_edge(module_build, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, planting_plan)
root.order.add_edge(planting_plan, irrigation_setup)
root.order.add_edge(irrigation_setup, climate_control)
root.order.add_edge(climate_control, lighting_adjust)
root.order.add_edge(lighting_adjust, pest_monitor)
root.order.add_edge(pest_monitor, waste_cycle)
root.order.add_edge(waste_cycle, data_capture)
root.order.add_edge(data_capture, yield_forecast)
root.order.add_edge(yield_forecast, regulation_check)
root.order.add_edge(regulation_check, community_meet)
root.order.add_edge(community_meet, harvest_prep)
root.order.add_edge(harvest_prep, market_link)

print(root)