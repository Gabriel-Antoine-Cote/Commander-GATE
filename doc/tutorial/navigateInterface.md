[DOCUMENTATION MAIN PAGE](mainPage.md)
---
# How to navigate the interface

There are three section to Commander-GATE. The first section is the hierarchy section. It shows the structure of the project and how each element is related to eachother. For example, a child volume will appear under its parent volume. The second section is the inspector section. This shows the parameters to configured for the selected element in the hierarchy section. The last section is the console section in which logs are written when an event happened.

The first view of Commander-GATE is a blank project just as shown here. The user will then need to select and expend elements in the hierarchy tree to have acces to their parameters. 
<div align="center">
   <img src="media/interface_start.png" alt="Interface Start View" width="50%">
   <p align="center">The view when starting Commander-GATE</p>
</div>

<div align="center">
   <img src="media/interface_example.png" alt="Interface Example View" width="50%">
   <p align="center">In this image, the output node is selected and therefore, its parameters shown in the inspector section.</p>
</div>

## The Hierarchy section

The hierarchy section shows the structure of the project. For OpenGATE, it is only natural that the project has a tree structure to represent the parent-child relation. The relationship is base on the [OpenGATE 9.4](https://opengate.readthedocs.io/en/latest/) macro commands. Indeed, the macro command is structured like a tree in which the gate node is the root and the following nodes comes from the next element in the macro command.

For example, the following macro command : [*/gate/output/ascii/enable*](https://opengate.readthedocs.io/en/latest/data_output_management.html#ascii-and-binary-outputs). This can be seperated into three section. The first is the gate node, then the output node and finally, the ascii/enable parameter. In the hierarchy section above, we can see that the "Enable ASCII output" parameter is from the output node which is itself a child of the gate node.

## The Inspector section

The Inspector section shows the parameters of the selected node. There is a multitude of type of parameters that the user interacts with. Here is a list of every type of input and how they function. For further information on types of parameter, the [uaml configuration page](yamlConfiguration.md) in the documentation offers a complete overview of it.

### **text**
The text input is a simple box in which the user can enter a number. The number will always be transformed into a float, but will be treated as an integer if the decimal part is zero. A text input can have units or not. That is up to the parameter to decide if units are demanded by the configuration. A text input may have more than one box input. The second text input shown in the image is a text input with multiple entry.

<div align="center">
   <img src="media/textInput.png" alt="Text Input View" width="50%">
   <p align="center">In this image, the parameters of the world volume are mostly text input.</p>
</div>

### **multiple text**
The multiple text input is similar to the text input, but does not have a upperbound on the number of entry that the user inputs. The user can add element to the parameter by clicking the "add" button and remove them by clicking the associated "X" button of the unwanted element.

<div align="center">
   <img src="media/multipleTextInput1.png" alt="Multiple Text Input View" width="50%">
   <p align="center">In this image, the multiple text input is empty.</p>
</div>

<div align="center">
   <img src="media/multipleTextInput2.png" alt="Multiple Text Input View" width="50%">
   <p align="center">In this image, the multiple text input has three inputs.</p>
</div>

### **dropdown**
The dropdown input allows the user to chose one item from a list of elements. The user only needs to click on the element of his choosing and it will be selected. Some dropdown are dynamic. This means that its list of possible value to choose from can change depending on other parameters. For example, the "Level selection" in the world node changes depending on the "system structure type" in the systems node. Other dropdown may update themself to allow new node as option. For example, the digitizer node need to bind to an attached volume. The digitizer list will only show the available volume. If the user attach a volume and go back to the digitizer, the dropdown will be updated to include the new volume as an option.

<div align="center">
   <img src="media/dropdownInput.png" alt="Dropdown Input View" width="50%">
   <p align="center">In this image, the dropdown contains all the material available by the simulation.</p>
</div>

### **checkable dropdown**
Like the multiple text input for the text input, the checkable dropdown allows the users to select multiple options from a dropdown.

<div align="center">
   <img src="media/checkableDropdownInput1.png" alt="Checkable Dropdown Input View" width="50%">
   <p align="center">In this image, the checkable dropdown updates itself to allow all volume.</p>
</div>

<div align="center">
   <img src="media/checkableDropdownInput2.png" alt="Checkable Dropdown Input View" width="50%">
   <p align="center">In this image, the checkable dropdown contains all volumes in the simulation.</p>
</div>

### **checkbox**
The checkbox input allows booling input. For example, the user can enable a certain flag.

<div align="center">
   <img src="media/checkboxInput.png" alt="Checkbox Input View" width="50%">
   <p align="center">In this image, the checkbox allows to write the ASCII ouput of the singles.</p>
</div>

### **select**
The select input allows the user to select a file in their environment. This can be used to load the material database or select the location of the output file.

<div align="center">
   <img src="media/selectInput.png" alt="Select Input View" width="50%">
   <p align="center">In this image, the "browse..." button lets the user locate a file.</p>
</div>

## The Console section
The console section shows the logs and comments that are useful for the user. In up coming versions, the console should show a definition of the parameter selected to help the user know what is demanded of them.