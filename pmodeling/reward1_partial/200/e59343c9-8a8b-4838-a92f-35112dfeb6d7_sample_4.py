from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

site_survey = Transition(label='Site Survey')
permit_approval = Transition(label='Permit Approval')
design_layout = Transition(label='Design Layout')
system_procure = Transition(label='System Procure')
nutrient_prep = Transition(label='Nutrient Prep')
structure_build = Transition(label='Structure Build')
sensor_install = Transition(label='Sensor Install')
climate_setup = Transition(label='Climate Setup')
seed_select = Transition(label='Seed Select')
germinate_seeds = Transition(label='Germinate Seeds')
monitor_growth = Transition(label='Monitor Growth')
data_analyze = Transition(label='Data Analyze')
pest_control = Transition(label='Pest Control')
harvest_crop = Transition(label='Harvest Crop')
package_goods = Transition(label='Package Goods')
ship_products = Transition(label='Ship Products')

skip = SilentTransition()

site_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_approval])
design_layout_choice = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])
system_procure_choice = OperatorPOWL(operator=Operator.XOR, children=[system_procure, skip])
nutrient_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, skip])
structure_build_choice = OperatorPOWL(operator=Operator.XOR, children=[structure_build, skip])
sensor_install_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
climate_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
seed_select_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_select, skip])
germinate_seeds_choice = OperatorPOWL(operator=Operator.XOR, children=[germinate_seeds, skip])
monitor_growth_choice = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, skip])
data_analyze_choice = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, skip])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
harvest_crop_choice = OperatorPOWL(operator=Operator.XOR, children=[harvest_crop, skip])
package_goods_choice = OperatorPOWL(operator=Operator.XOR, children=[package_goods, skip])
ship_products_choice = OperatorPOWL(operator=Operator.XOR, children=[ship_products, skip])

root = StrictPartialOrder(nodes=[
    site_approval_loop, 
    design_layout_choice, 
    system_procure_choice, 
    nutrient_prep_choice, 
    structure_build_choice, 
    sensor_install_choice, 
    climate_setup_choice, 
    seed_select_choice, 
    germinate_seeds_choice, 
    monitor_growth_choice, 
    data_analyze_choice, 
    pest_control_choice, 
    harvest_crop_choice, 
    package_goods_choice, 
    ship_products_choice
])

root.order.add_edge(site_approval_loop, design_layout_choice)
root.order.add_edge(site_approval_loop, system_procure_choice)
root.order.add_edge(design_layout_choice, nutrient_prep_choice)
root.order.add_edge(design_layout_choice, structure_build_choice)
root.order.add_edge(system_procure_choice, sensor_install_choice)
root.order.add_edge(system_procure_choice, climate_setup_choice)
root.order.add_edge(nutrient_prep_choice, seed_select_choice)
root.order.add_edge(nutrient_prep_choice, germinate_seeds_choice)
root.order.add_edge(structure_build_choice, monitor_growth_choice)
root.order.add_edge(structure_build_choice, data_analyze_choice)
root.order.add_edge(sensor_install_choice, pest_control_choice)
root.order.add_edge(sensor_install_choice, harvest_crop_choice)
root.order.add_edge(climate_setup_choice, package_goods_choice)
root.order.add_edge(climate_setup_choice, ship_products_choice)
root.order.add_edge(seed_select_choice, germinate_seeds_choice)
root.order.add_edge(germinate_seeds_choice, monitor_growth_choice)
root.order.add_edge(germinate_seeds_choice, data_analyze_choice)
root.order.add_edge(monitor_growth_choice, pest_control_choice)
root.order.add_edge(monitor_growth_choice, harvest_crop_choice)
root.order.add_edge(data_analyze_choice, package_goods_choice)
root.order.add_edge(data_analyze_choice, ship_products_choice)
root.order.add_edge(pest_control_choice, harvest_crop_choice)
root.order.add_edge(package_goods_choice, ship_products_choice)