# Flutter
## Core Concepts
### Stateful vs. Stateless Widgets

In Flutter, everything you see on the screen and can interact with, is called a ***Widget***[^widgets] [^widgets2]. Flutter distinguishes between *stateless* and *stateful* widgets. For those, familiar with React, the distinction is similar to that between class and functional React components[^react].

#### Stateless widgets
A stateless widget is the rough equivalent of a one-way street. It is given some final state at instantiation time, and throughoutits lifetime, it only makes use of those. A stateless widget cannot hold non-fina fields, in fact if you try to add one to a class that extends from `StatelessWidget`, you will see the following warning:

> This class (or a class which this class inherits from) is marked as '@immutable', but one or more of its instance fields are not final.

If you dive deeper into the Flutter SDK code, you will find the following piece of documentation regarding `@immutable`:

> A class is immutable if all of the instance fields of the class, whether defined directly or inherited, are `final`.

TODO: Add more detials from [Widget - State - Context - InheritedWidget](https://www.didierboelens.com/2018/06/widget---state---context---inheritedwidget/)

[^widgets]: [Basic widgets | Flutter](https://flutter.io/docs/development/ui/widgets/basics)

[^widgets2]: [Flutter Widgets | Flutter by Example]([https://flutter.io/docs/development/ui/widgets/basics](https://flutterbyexample.com/flutter-widgets/))

[^react]: [Reactjs: Class Components and Functional Components](https://medium.com/@lailbrown/reactjs-class-components-and-functional-components-5f00edbd5d92)

## Layout
### Row and Column
TODO: add more detials from [Flutter — Row/Column Cheat Sheet](https://medium.com/jlouage/flutter-row-column-cheat-sheet-78c38d242041)
