[Back to the main page](mainPage.md)
---
# Commander-GATE system architecture

The architecture of the Commander-GATE project is seperated in three sections following the View Control Model patron. Each of the section have their own folder to keep the business logic seperated from the graphical interface. The Model folder's responsability is to generate the starting project and handled updated given by the Control API. The Control folder's responsability is to handle what the View demands and treat it accordingly. The View folder's responsability is to show the graphical interface to the user and output the users input to the Control.

## Project's file structure
```
src
├── Control
│   └── # Contains the API that connects the View of the system with the Model and other useful object to iteract with.
├── Model
│   ├── DynamicData
│   │   ├── Concreate
│   │   │   └── # Contains the Model objects that contains the data of the OpenGATE configuration
│   │   ├── Interface
│   │   │   └── # Contains the interfaces of the Model objects. It is also the interface of the Proxy Objects
│   │   └── Proxy
│   │       └── # Contains a read only version of the Model objects that the View can interact with.
│   └── StaticData
│       └── # Contains data that is not changed when the project is run. The yaml file describe the Model object parameters.
└── View
    ├── actions
    │   └── # Contains the objects that performs actions
    ├── helper
    │   └── # Contains the objects that offer helping functions
    ├── parameters 
    │   └── # Contains the parameters object and how to threat them (Some are custom widget, other are wrapper of already existing ones)
    ├── popups
    │   └── # Contains the objects that handles the pop ups window
    ├── sections
    │   └── # Contains the section object (Hierarchy, Inspector, Console) of the main window
    ├── MainWindow.py # Control the GUI of the project
    └── StyleSheets.py # Describes the style of certain widgets
```
## Model structure
Command-GATE Model is inspired by the OpenGATE 9.4 macro command structure. In OpenGATE 9.4, the macro commands can either be for the overall structure or for a specific element. For example, the macro command `/gate/run/initialize` is an overall command that is not attached to a specific element. On the other hand, the following commands are specifics.

```
(1) /gate/world/daughters/name Phantom
(2) /gate/world/daughters/insert box
(3) /gate/Phantom/setMaterial Water
```
The first (1) command creates a child volume name Phantom. The second (2) commands insert the child volume as a box volume. The third volume (3) is a specific command that interact directly to the *Phantom* volume. To see how to spot a specific command, the name of the volume is in the command itself. An overall command set a parameter in the simulation where as a specific command set a parameter of a specific object. (Ex.: Volume, Digitizer, Source, Output, Acquisition, System, ...)

With this structure in mind, commands related to specific object are grouped together for clarity. For example, the volume specific parameters are owned by volume objects. Digitizer specific parameters are owned by digitizer objects and so on.

The model is made up of two type of elements, GateObject and GateParameter. A GateObject's purpose is to form the structure of the model (the node of the tree) and own the GateParameter that is related to itself. The GateParameter's purpose is to hold the data related to the commands of the object. For example, the command `/gate/Phantom/setMaterial Water` has the data **Water**. In the model, a GateParameter would hold the data that the volume is made of water. This parameter would be own by the GateObject representing the phantom object.

Since the OpenGATE project has a lot of command to enable the user to customize the simulation as precisely has needed, the project uses a yaml configuration file that describe every parameter and how to fill it. The [Yaml Configuration](./yamlConfiguration.md) page offers further information on it.

The Model is structure in the following way :

```
root (GateTree)
├── gate
│   ├── systems
│   ├── physics
│   │   └── (0..n) process
│   ├── source (source folder)
│   │   └── (0..n) source
│   ├── actor (actor folder)
│   │   └── (0..n) actor
│   │       └── (0..n) filter 
│   ├── digitizer (digitizer folder)
│   │   └── (0..n) Singles
│   │       ├── adderComptPhoIdel
│   │       ├── adderCompton
│   │       ├── adder
│   │       ├── readout
│   │       ├── energyResolution
│   │       ├── timeResolution
│   │       ├── spatialResolution
│   │       ├── energyFraming
│   │       ├── clusterin
│   │       ├── efficiency
│   │       ├── pileup
│   │       ├── deadtime
│   │       ├── noise
│   │       ├── merger
│   │       ├── intrinsicResolution
│   │       ├── crosstalk
│   │       ├── buffer
│   │       ├── gridDiscretizator
│   │       ├── doIModel
│   │       ├── timeDelay
│   │       ├── multipleRejection
│   │       └── virtualSegmentation 
│   ├── output
│   ├── acquisition
│   ├── distributions (distribution folder)
│   │   └── (0..n) distribution
│   └── world
│       └── (0..n) childVolume (childVolume can have child volumes themselves so it forms a tree structure.)
└── vis
```
For the rest of this page, a parameter in the model will be identified by the absolute path of the GateObject owning it and the displayed label attached to it. For example, the GateParameter "**Systems Structure Type**" owned by the "*systems*" GateObject is identified with the `gate/systems/"Systems Structure Type" `

The root of the tree (**GateTree**) creates every GateObject and GateParameter needed during startup. All the methods are owned by the root to create new GateObject and GateParameter.

Since the model can only have one root, the GateTree object is a singleton. This helps the Control structure stay static and environment independant for the View structure. To have access to the Model, a simple GateTree() call is sufficient. The root of the Model contains the yaml configuration, its GateObject children, the list of materials available and every GateParameter that needs to be upda

### Dynamic structure
The OpenGATE project is a contextual simulation configuration. This means that the order in which the commands are written impacts the result of the simulation (In most cases, the simulation fails). This is not surprising, most programming language function that way. What is special in OpenGATE is that changes in parameters in one object of the simulation impacts many more objects elsewhere. This means that parameters of the model needs to update frequently to insure the right parameters.

For example, `gate/systems/"Systems Structure Type"` impacts what level values are available in the `gate/world/"Level selection"` GateParameter. So be careful when changing a parameter because the new value may invalidate previously changed data. The [Yaml Configuration](./yamlConfiguration.md) page offers more information on how the updates are handled.

## Control structure
The model 


Plan for this page:
- Explain how the View Model Control works deeply
- EXplain how the data flows from the model to the view.
- Explain how the data is updated by the users interaction