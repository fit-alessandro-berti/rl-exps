root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Design Modules'),
        Transition(label='Source Materials'),
        Transition(label='Install Framework'),
        Transition(label='Setup Irrigation'),
        Transition(label='Integrate Sensors'),
        Transition(label='Configure AI'),
        Transition(label='Select Crops'),
        Transition(label='Calibrate Climate'),
        Transition(label='Plant Seeds'),
        Transition(label='Monitor Growth'),
        Transition(label='Manage Pests'),
        Transition(label='Recycle Waste'),
        Transition(label='Engage Community'),
        Transition(label='Ensure Compliance'),
        Transition(label='Distribute Produce')
    ],
    order=[
        (Transition(label='Site Survey'), Transition(label='Design Modules')),
        (Transition(label='Design Modules'), Transition(label='Source Materials')),
        (Transition(label='Source Materials'), Transition(label='Install Framework')),
        (Transition(label='Install Framework'), Transition(label='Setup Irrigation')),
        (Transition(label='Setup Irrigation'), Transition(label='Integrate Sensors')),
        (Transition(label='Integrate Sensors'), Transition(label='Configure AI')),
        (Transition(label='Configure AI'), Transition(label='Select Crops')),
        (Transition(label='Select Crops'), Transition(label='Calibrate Climate')),
        (Transition(label='Calibrate Climate'), Transition(label='Plant Seeds')),
        (Transition(label='Plant Seeds'), Transition(label='Monitor Growth')),
        (Transition(label='Monitor Growth'), Transition(label='Manage Pests')),
        (Transition(label='Manage Pests'), Transition(label='Recycle Waste')),
        (Transition(label='Recycle Waste'), Transition(label='Engage Community')),
        (Transition(label='Engage Community'), Transition(label='Ensure Compliance')),
        (Transition(label='Ensure Compliance'), Transition(label='Distribute Produce'))
    ]
)