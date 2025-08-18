from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
enviro_design = Transition(label='Enviro Design')
hydro_setup = Transition(label='Hydro Setup')
aeroponics_add = Transition(label='Aeroponics Add')
lighting_procure = Transition(label='Lighting Procure')
water_recycle = Transition(label='Water Recycle')
rack_install = Transition(label='Rack Install')
seed_select = Transition(label='Seed Select')
germinate_seeds = Transition(label='Germinate Seeds')
nutrient_mix = Transition(label='Nutrient Mix')
staff_train = Transition(label='Staff Train')
pest_control = Transition(label='Pest Control')
pilot_crop = Transition(label='Pilot Crop')
data_gather = Transition(label='Data Gather')
yield_optimize = Transition(label='Yield Optimize')

# Define the process tree structure
root = StrictPartialOrder(nodes=[
    site_analysis,
    structure_check,
    enviro_design,
    hydro_setup,
    aeroponics_add,
    lighting_procure,
    water_recycle,
    rack_install,
    seed_select,
    germinate_seeds,
    nutrient_mix,
    staff_train,
    pest_control,
    pilot_crop,
    data_gather,
    yield_optimize
])

# Add edges to define the dependencies
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(site_analysis, enviro_design)
root.order.add_edge(structure_check, hydro_setup)
root.order.add_edge(structure_check, aeroponics_add)
root.order.add_edge(enviro_design, hydro_setup)
root.order.add_edge(enviro_design, aeroponics_add)
root.order.add_edge(hydro_setup, lighting_procure)
root.order.add_edge(hydro_setup, water_recycle)
root.order.add_edge(hydro_setup, rack_install)
root.order.add_edge(aeroponics_add, lighting_procure)
root.order.add_edge(aeroponics_add, water_recycle)
root.order.add_edge(aeroponics_add, rack_install)
root.order.add_edge(lighting_procure, staff_train)
root.order.add_edge(lighting_procure, pest_control)
root.order.add_edge(water_recycle, staff_train)
root.order.add_edge(water_recycle, pest_control)
root.order.add_edge(rack_install, staff_train)
root.order.add_edge(rack_install, pest_control)
root.order.add_edge(seed_select, germinate_seeds)
root.order.add_edge(nutrient_mix, germinate_seeds)
root.order.add_edge(germinate_seeds, staff_train)
root.order.add_edge(germinate_seeds, pest_control)
root.order.add_edge(staff_train, pilot_crop)
root.order.add_edge(pest_control, pilot_crop)
root.order.add_edge(pilot_crop, data_gather)
root.order.add_edge(pilot_crop, yield_optimize)

print(root)