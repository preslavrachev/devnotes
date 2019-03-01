# Flutter
## Core Concepts
### Widgets
In Flutter, everything you see on the screen and can interact with, is called a ***Widget***[^widgets] [^widgets2]. Whether they keep any state or not, widgets are to be considered immutable - when the state a widget depends on depends on changes, the widget does not merely change, but it gets replaced with a new instance. This is a concept that has been popularized by frameworks such as React.

#### Stateful vs. Stateless Widgets

 Flutter distinguishes between *stateless* and *stateful* widgets. For those, familiar with React, the distinction is similar to that between class and functional React components[^react].

##### Stateless widgets
A stateless widget is the rough equivalent of a one-way street. It is given some final state at instantiation time, and throughoutits lifetime, it only makes use of those. A stateless widget cannot hold non-fina fields, in fact if you try to add one to a class that extends from `StatelessWidget`, you will see the following warning:

> This class (or a class which this class inherits from) is marked as '@immutable', but one or more of its instance fields are not final.

If you dive deeper into the Flutter SDK code, you will find the following piece of documentation regarding `@immutable`:

> A class is immutable if all of the instance fields of the class, whether defined directly or inherited, are `final`.

==TODO: Add more detials from [Widget - State - Context - InheritedWidget](https://www.didierboelens.com/2018/06/widget---state---context---inheritedwidget/)==

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
==TODO: add more detials from [Flutter — Row/Column Cheat Sheet](https://medium.com/jlouage/flutter-row-column-cheat-sheet-78c38d242041)==

### Advanced Topics
#### Slivers
Slivers[^slivers] are not a very deeply discussed topic in Flutter, mainly because they sit underneath more commonly used Widgets such as ListView, and GridView. This is a problem, because it leads to lots of panic when it comes to working with slivers.

> A sliver is just a portion of a scrollable area. Under the covers, all of the scrollable views you use, like ListView and GridView, are actually implemented using Slivers.[^slivers2]

[^slivers]: [Slivers | Flutter Docs](https://flutter.dev/docs/development/ui/advanced/slivers)
[^slivers2]: [Slivers Demystifed](https://medium.com/flutter-io/slivers-demystified-6ff68ab0296f)

[^safearea]: [SafeArea | Flutter Docs](https://docs.flutter.io/flutter/widgets/SafeArea-class.html)

## State Management

==TODO: elaborate on this [List of state management approaches](https://flutter.dev/docs/development/data-and-backend/state-mgmt/options)==

When it comes to state management, a good advice for people just starting out with Flutter is: use `ScopedModel` for as long as you can. In a large majority of cases, a scoped model would be more than sufficient. When it does not scale, you can have a look at BLoC or at Redux for those coming from React.[^efortuna] If you are new to Flutter and don't have a strong reason to choose any other approach, this is the first thing you should try, before moving on to some more compliated approaches.[^scoped_model]

[^efortuna]: [Emily Fortuna | It's All Widgets Podcast](https://itsallwidgets.com/podcast/episodes/23/emily-fortuna)

[^scoped_model]: [Simple app state management | Flutter Docs](https://flutter.dev/docs/development/data-and-backend/state-mgmt/simple)