# Airbnb Clone

<img src="https://i.imgur.com/6JaLQ4z.png" align="center"/>

## Index

- [MVC Model](#model) 
- [The project](#project)
- [Console usage](#console)
- [Resources](#Resources)
- [Authors](#Authors())

## Description
<a name="model"/>
This project consists in recreating the _AirBnB_ software structure. This one is based on the model MVC (Model-View-Controller) a model that consists in creating a layerd structure that delimits each layer from the others and letting them interact with each other safely.

## Model:
This level is very important as it represents the data to the user. This level defines where the application’s data objects are stored. The model doesn’t know anything about views and controllers. So, whenever there are changes done in the model it will automatically notify observers that the changes are made. The model may be a single object or a structure of objects.

## View:
A view is a visual representation of the MVC model. This level creates an interface to show the actual output to the user. However, a view will not display anything itself. It is the controller or model that tells view of what to display to the user. It also handles requests from the user and informs the controller. A view is connected to its model and gets the data necessary for the presentation by asking certain questions. Sometimes, it also updates the model by sending appropriate messages. All these questions and messages are sent back to the model in such an easy terminology that can easily understand the information sent by a model or a controller.

## Controller:
The controller is a level that acts as the brain of the entire MVC system. A controller also acts as a link between a user and the system. It provides the user with the input by providing appropriate views to present it appropriately on the screen. The controller understands user output, converts it into the appropriate messages and passes the same to views.

## Benefits of the model:

One of the principal benefits of using a MVC model is making easy the identification of problems in the logic, creating a more accesible environment to identify issues. As the areas are separated in different layers errors may be handled individually within each area.

Moreover, this model supports rapid and parallel development. If an MVC model is used to develop any particular web application (or other software) then it is possible that one programmer can work on the view while the other can work on the controller to create the business logic of the web application. Hence this way, the application developed using the MVC model can be completed three times faster than applications that are developed using other development patterns.

<div align="center">
<center><img src="https://i.imgur.com/v3qA2ih.jpeg" width="75%" height="75%"/><center/>
<div/>

## The scope of this project
<a name="project"/>
For this project the goal was recreating the model described before but using simpler methods for each layer. The beginning of an approach on how the _AirBnB_ software works behind the scenes. The hole project was written in python. The model layer was all the logic implemented in the models folder. Creating the BaseModel class and all the classes that inherit this model, such as User, Amenity, City, Place, etc. The persistence of the data was handled by the FileStorage system, making able to save the information created in JSON files when the program was running. The controller layer was the console, for witch was used the cmd module provided by python. In this early state of the project the view was considered by the console itself, the interface created for the user will be considered in future iterations.


## The console, how to use it?
<a name="console"/>

For running the console make sure that execution permissions are enabled. After that execute the file.
The (hbnb) prompt will be displayed. In the example below is shown how can be runned some commands. 
<div align="center">
<img src="https://hippieboton.xyz/Console_AirBnB.gif" align="center"/>
<div/>

- `help` command will give the available commands. Running `help` followed by the name of a command will display a simple description of the command.

- `create` command will create an instance of the class indicated after the command. Returns the ID of the instance created. Example: 
```console
(hbnb) create User 
```

- `update` command updates an attribute of an instance. If an attribute doesn't exist will create a new one. Example:
```console
(hbnb) update User cb11001d-1430-481d-a67f-01055350fc59 name "Pichu"
```

- `show` command will display the string representation of instance of the class indicated by its ID number. Example:
```console
(hbnb) update User cb11001d-1430-481d-a67f-01055350fc59
```

- `destroy` command will delete an instance based on the class name and id. Example:
```console
(hbnb) destroy User cb11001d-1430-481d-a67f-01055350fc59
```

- `all` command will display a string representation of all instances based or not on the class name (Class name is optional). Example:
```console
(hbnb) all
```

- `EOF` and `quit` command will exit the console

## Resources
<a name="Resources"/>

-   [cmd module](https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rw "cmd module")
-   [uuid module](https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g "uuid module")
-   [datetime](https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q "datetime")
-   [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g "unittest module")
-   [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg "args/kwargs")
-   [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A "Python test cheatsheet")

## Authors
<a name="Authors"/>

- [Raimundo Gallino](https://github.com/RaimundoGallino)
- [Diego Varela](https://github.com/dieg0varela)
