---
title: "Object-Oriented Programming (OOP)"
tags: [concept, software-analyse, semester-1, programming-paradigms]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-07-02
prerequisites: [programming-basics]
---

## One-line Summary
Object-oriented programming organizes code around objects — instances of classes that bundle data (fields) and behaviour (methods) — structured around four pillars: encapsulation, inheritance, polymorphism, and abstraction.

## Core Intuition
OOP models software the way we model the real world: as interacting objects. A `BankAccount` has a balance (data) and can `deposit()` or `withdraw()` (behaviour). The balance is private — you can't reach in and change it directly — you must use the interface. This "black box" thinking is the essence of encapsulation. Objects form hierarchies (a `SavingsAccount` IS-A `BankAccount`) and can be used interchangeably through polymorphism.

## Formal Definition / Statement
**Four Pillars of OOP:**

1. **Encapsulation**: Bundle data and methods into a class; hide internal state behind a public interface. Access modifiers (public, private, protected) enforce visibility.

2. **Inheritance**: A subclass extends a superclass, inheriting fields and methods. Establishes an IS-A relationship. Enables code reuse but can create tight coupling.

3. **Polymorphism**: The same interface can refer to objects of different types at runtime. Two forms:
   - *Ad hoc polymorphism* (method overloading): same name, different parameter types
   - *Subtype polymorphism* (method overriding): subclass provides its own implementation

4. **Abstraction**: Simplify complexity by hiding implementation details. Abstract classes and interfaces define contracts without specifying implementation.

## Key Properties / Complexity
- **Modularity**: Code organized into self-contained objects
- **Reusability**: Inheritance and composition enable reuse
- **Maintainability**: Encapsulation limits impact of changes
- **Extensibility**: New classes extend existing ones without modification (Open/Closed Principle)
- **Testability**: Objects can be tested in isolation (with mocking)

## Worked Example
**Java example — Shape hierarchy:**

```java
abstract class Shape {
    abstract double area();           // abstraction
    abstract double perimeter();
}

class Circle extends Shape {          // inheritance
    private double radius;            // encapsulation

    Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double area() {                   // polymorphism (overriding)
        return Math.PI * radius * radius;
    }

    @Override
    double perimeter() {
        return 2 * Math.PI * radius;
    }
}

class Rectangle extends Shape {
    private double width, height;

    Rectangle(double w, double h) {
        this.width = w;
        this.height = h;
    }

    @Override
    double area() { return width * height; }

    @Override
    double perimeter() { return 2 * (width + height); }
}

// Polymorphism in action:
Shape s = new Circle(5);      // reference type: Shape, actual type: Circle
System.out.println(s.area()); // calls Circle.area() at runtime
```

**Why this matters for AOP:** OOP organizes code by class, but crosscutting concerns (logging every `area()` call, security checks on `withdraw()`) don't fit into a single class — they get scattered across many classes. This is exactly the problem [[aspect-oriented-programming]] solves.

## Common Pitfalls
- **God objects**: Classes that do too much, violating Single Responsibility Principle
- **Inheritance abuse**: Deep inheritance hierarchies create tight coupling; prefer composition over inheritance
- **Liskov Substitution violation**: Subclass breaks the contract of the superclass
- **Anemic domain model**: Classes with only getters/setters and no real behaviour — just data bags
- **Over-engineering**: Using OOP patterns where simple functions would suffice

## Connections
- [[aspect-oriented-programming]] — AOP addresses limitations of OOP's modularization for crosscutting concerns
- [[design-patterns]] — design patterns are reusable OOP solutions to common problems
- [[java-for-software-analysis]] — Java is the canonical OOP language used in this course
- [[software-analyse-lecture-9]] — lecture covers how OOP structures relate to software analysis

## Open Questions
- How does OOP's module structure create the crosscutting problem that AOP solves?
- When does inheritance become harmful compared to composition?
- How do SOLID principles relate to the four pillars of OOP?
