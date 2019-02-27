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
### Scaffold
#### Common Issues
##### Widgets appear behind navigation elements (e.g. behind nav bars)
A common issue when setting up a page `Scaffold` is to see content appearing behind the main navigation element (e.g. behind the nav bar). To avoid this, the immediate child widget of a `Scaffold` instance needs to be wrapped in a so called `SafeArea`[^safearea] widget:

``` dart hl_lines="4 8"
class SearchPage1 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new CupertinoPageScaffold(
        navigationBar: CupertinoNavigationBar(
          middle: Text('Saved Searches'),
        ),
        child: SafeArea(
          child: Column(
          // the rest of the widget continues
```

### Row and Column
TODO: add more detials from [Flutter — Row/Column Cheat Sheet](https://medium.com/jlouage/flutter-row-column-cheat-sheet-78c38d242041)

### Advanced Topics
#### Slivers
Slivers[^slivers] are not a very deeply discussed topic in Flutter, mainly because they sit underneath more commonly used Widgets such as ListView, and GridView. This is a problem, because it leads to lots of panic when it comes to working with slivers.

> A sliver is just a portion of a scrollable area. Under the covers, all of the scrollable views you use, like ListView and GridView, are actually implemented using Slivers.[^slivers2]

[^slivers]: [Slivers | Flutter Docs](https://flutter.dev/docs/development/ui/advanced/slivers)
[^slivers2]: [Slivers Demystifed](https://medium.com/flutter-io/slivers-demystified-6ff68ab0296f)

[^safearea]: [SafeArea | Flutter Docs](https://docs.flutter.io/flutter/widgets/SafeArea-class.html)
