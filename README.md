# Commander
## Table of Contents

1. [Description](#description)
2. [Documentation](#documentation)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Support](#support)
6. [Roadmap](#roadmap)
7. [Contributing](#contributing)
8. [Authors and acknowledgement](#authors-and-acknowledgment)
9. [License](#license)
10. [Project status](#project-status)

---
## Description

This is the V0.1

A desktop toolkit for composing, inspecting, and exporting **GATE** simulation projects through a clean, PyQt6-based UI. Commander lets you build detector geometries, sources, physics/digitizer chains, and output pipelines using a structured **node tree** with rich parameter editors. It targets day‑to‑day productivity (quick iterations, presets, live validation) while staying faithful to GATE parameters.

### Goals of Commander-GATE
The main goal of this project is to facilitate the process of creating GATE simulations. Configurating [OpenGATE 9.4](https://opengate.readthedocs.io/en/latest/) simulation requires the user to understand the macro interface. The simulation configured by OpenGATE are mainly used by physicists and medical researchers. Programming the simulation configuration with [macro commands](https://opengate.readthedocs.io/en/latest/getting_started.html#the-user-interface-a-macro-language) may not be as straight forward as it may seems since its Application Programming Interface (API) structure is quite complex. This has been an issue in the OpenGATE community and a change in paradigm happen in [OpenGate 10](https://opengate-python.readthedocs.io/en/master/index.html). This new version's configuration is written in python with its own library for ease of use with the API. [OpenGate 10](https://opengate-python.readthedocs.io/en/master/index.html) is still in developpement and some features available in [OpenGATE 9.4](https://opengate.readthedocs.io/en/latest/) may not be present in [OpenGate 10](https://opengate-python.readthedocs.io/en/master/index.html).

Another goal of Commander-GATE is to check errors in the configuration of [OpenGATE 9.4](https://opengate.readthedocs.io/en/latest/)'s simulation. Since the [OpenGATE 9.4](https://opengate.readthedocs.io/en/latest/) simulation's configuration is written with [macro commands](https://opengate.readthedocs.io/en/latest/getting_started.html#the-user-interface-a-macro-language), there are no syntaxic checker to verify the configuration's output. Commander-GATE would verify the GATE parameter directly with the input from the user. After verification, the project would export the configuration into a medium that is native to the OpenGATE project. In other words, the project generate a macro file for [OpenGATE 9.4](https://opengate.readthedocs.io/en/latest/) and a python file for [OpenGate 10](https://opengate-python.readthedocs.io/en/master/index.html).

### Features of Commander-GATE

The Commander-GATE project is able to have the parameter types of OpenGATE 9.4 and OpenGATE 10. This allows the users to translate from one version to the other without forgetting parameters. Also, while it is possible to export the configuration to an OpenGATE native medium like macro file, Commander-GATE make it possible to also save its configuration in a JSON file. Therefore, the user can save its configuration and worked on it at a later time.

## Documentation
The project's documentation on how to navigate its interface and its elements are shown in the doc folder. Here is a link to the documentation's main page.

[**DOCUMENTATION'S MAIN PAGE**](doc/mainPage.md)

## Installation
### Prerequisite
Before installing the project, you will need to install the dependencies of it. To do so, you can install the python package with the **requirements.txt** file.

Install the virtual environment. To do so, you will need to go to the **root** of this project and execute the following command.

For Linux environment (in the terminal):

      python3 -m venv .venv
      source .venv/bin/activate
      python -m pip install --upgrade pip
      pip install -r requirements.txt

For Windows environment (in the command prompt):

      python3 -m venv .venv
      .venv\Scripts\activate.bat
      python -m pip install --upgrade pip
      pip install -r requirements.txt
      
### Install a stand-alone application
To generate a stand-alone application, you can do the following command at the top of the repo:

      pyinstaller --onefile --windowed --icon=appLogo.ico --add-data "appLogo.ico:." CTCommander.py

The application will be created in the **dist** folder.

### Run with source code
To run with the source code, you can simply run the main file:

      python CTCommander.py

## Usage

To ease the user's work flow with the project, Commander-GATE is a graphical only interface. This means that the users can accomplish anything that the project has to offer through the interface. The graphical interface is made with pyqt6, which is in itself a wrapper of Qt. "[How to navigate the interface](doc/navigateInterface.md)" page helps understand how to interact with the interface.

## Support
The OpenGATE project is open source and the community is thriving. You can check the [OpenGATE 10 repo](https://github.com/OpenGATE/opengate) and check the many discussion and issues that are being attended to. The OpenGATE project is built onto the [Geant4](https://geant4.web.cern.ch/) particle physics simulation. Check their documentation to better understant how everything works together. It is possible to also view the [OpenGATE 9 repo](https://github.com/OpenGATE/Gate) but to have access to the engine, it is suggested to use either the virtual machine or the docker container explained [here](https://opengate.readthedocs.io/en/latest/installation.html)

For more information on Commander-GATE, the [documentation](doc/mainPage.md) offers a more in-depth view in the project and how it was built.

## Roadmap
For the future of this project, here is a list of feature yet to be completed.
- Importing OpenGATE 10 configuration


## Contributing
If you desire, you can contribute to the Commander-GATE project. The project itself follows the git workflow. To work on feature, please fork the project and keep it updated with the main fork. To make sure that the added feature are well implemented, it is important to add working testbench and documentation for the feature. The testbench should be created in the **tests** folder following the same relative path as the class tested in the **src** folder. For example, the GateTree and HelperFunction are tested by their test conterpart (test_GateTree.py, test_HelperFunction.py).

```
src
├── Control
├── Model
│   ├── DynamicData
│   │   └── GateTree.py
│   └── HelperFunction
│       └── HelperFunction.py
└── View
```

```
tests
├── Control
├── Model
│   ├── DynamicData
│   │   └── test_GateTree.py
│   └── HelperFunction
│       └── test_HelperFunction.py
└── View
```
Documentation is important to log what has happened while you worked on the project. A feature should always be accompanied by documentation explaining why it was implemented this way and not another. Documentation should not only be for implemented features, but also unsuccesful route. This will give insight in future developper in what has already been tried with the system.

## Authors and acknowledgment

Intelligent systems and Machine learning Programmed for Embedded Technologies at University of Sherbrooke (IMPETUS) is responsable for this project.

## License

Plan for this section:
- Put the license of every python library used in this project

## Project status

Plan for this section:
- Say that it is currently on hold by january
