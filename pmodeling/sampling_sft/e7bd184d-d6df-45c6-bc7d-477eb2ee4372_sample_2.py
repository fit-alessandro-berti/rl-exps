import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_analysis   = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
enviro_design   = Transition(label='Enviro Design')
hydro_setup     = Transition(label='Hydro Setup')
aeroponics_add  = Transition(label='Aeroponics Add')
lighting_procure= Transition(label='Lighting Procure')
water_recycle   = Transition(label='Water Recycle')
rack_install    = Transition(label='Rack Install')
seed_select     = Transition(label='Seed Select')
germinate_seeds = Transition(label='Germinate Seeds')
nutrient_mix    = Transition(label='Nutrient Mix')
staff_train     = Transition(label='Staff Train')
pest_control    = Transition(label='Pest Control')
pilot_crop      = Transition(label='Pilot Crop')
data_gather     = Transition(label='Data Gather')
yield_optimize  = Transition(label='Yield Optimize')

# Define the core sequential workflow as a partial order
core_workflow = StrictPartialOrder(nodes=[
    site_analysis, structure_check, enviro_design,
    hydro_setup, aeroponics_add, lighting_procure,
    water_recycle, rack_install,
    seed_select, germinate_seeds, nutrient_mix,
    staff_train, pest_control,
    pilot_crop, data_gather, yield_optimize
])
core_order = core_workflow.order
core_order.add_edge(site_analysis,     structure_check)
core_order.add_edge(structure_check,   enviro_design)
core_order.add_edge(enviro_design,     hydro_setup)
core_order.add_edge(enviro_design,     aeroponics_add)
core_order.add_edge(hydro_setup,       lighting_procure)
core_order.add_edge(hydro_setup,       water_recycle)
core_order.add_edge(aeroponics_add,    lighting_procure)
core_order.add_edge(aeroponics_add,    water_recycle)
core_order.add_edge(lighting_procure,  rack_install)
core_order.add_edge(water_recycle,     rack_install)
core_order.add_edge(rack_install,      seed_select)
core_order.add_edge(seed_select,       germinate_seeds)
core_order.add_edge(germinate_seeds,   nutrient_mix)
core_order.add_edge(nutrient_mix,      staff_train)
core_order.add_edge(staff_train,       pest_control)
core_order.add_edge(pest_control,      pilot_crop)
core_order.add_edge(pilot_crop,        data_gather)
core_order.add_edge(data_gather,       yield_optimize)

# Define the loop: after pilot crop, optionally do yield optimization then repeat
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_optimize, core_workflow]
)

# The root model is the core workflow followed by the loop
root = StrictPartialOrder(nodes=[core_workflow, loop])
root.order.add_edge(core_workflow, loop)