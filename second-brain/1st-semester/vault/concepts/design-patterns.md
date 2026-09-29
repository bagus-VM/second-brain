---
title: "Design Patterns"
tags: [concept, software-analyse, semester-1, software-engineering]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-07-02
prerequisites: [object-oriented-programming]
---

## One-line Summary
Design patterns are reusable, catalogued solutions to common software design problems, categorized into creational, structural, and behavioral patterns by the Gang of Four (1994).

## Core Intuition
Every experienced developer eventually solves the same problems: "How do I create objects without specifying the exact class?" (Factory), "How do I notify dependent objects when something changes?" (Observer), "How do I make incompatible interfaces work together?" (Adapter). Design patterns name these solutions so teams can communicate about them precisely. They're not libraries — they're templates for thinking about design.

## Formal Definition / Statement
**Source:** Gamma, Helm, Johnson, Vlissides (Gang of Four), *Design Patterns: Elements of Reusable Object-Oriented Software*, 1994.

**Three categories:**

### Creational Patterns (object creation)
- **Factory Method**: Define an interface for creating objects, let subclasses decide which class to instantiate
- **Builder**: Separate construction of a complex object from its representation
- **Singleton**: Ensure a class has only one instance with a global access point

### Structural Patterns (object composition)
- **Adapter**: Convert one interface into another clients expect
- **Decorator**: Attach additional responsibilities to an object dynamically
- **Facade**: Provide a unified interface to a set of subsystems

### Behavioral Patterns (object interaction)
- **Observer**: Define a one-to-many dependency so that when one object changes state, all dependents are notified
- **Strategy**: Define a family of algorithms, encapsulate each one, make them interchangeable
- **Template Method**: Define the skeleton of an algorithm in a superclass, defer steps to subclasses

## Key Properties / Complexity
- **Language-independent**: Patterns apply across programming languages
- **Not invention, but documentation**: Patterns describe what good designers already do
- **Level of abstraction**: More abstract than algorithms, more concrete than principles
- **Named vocabulary**: Enables concise communication ("use an Observer here")
- **Trade-offs**: Every pattern has costs (indirection, complexity) alongside benefits

## Worked Example
**Observer Pattern — weather station:**

```java
// Subject (Observable)
class WeatherStation {
    private List<Observer> observers = new ArrayList<>();
    private float temperature;

    void addObserver(Observer o) { observers.add(o); }
    void removeObserver(Observer o) { observers.remove(o); }

    void setTemperature(float temp) {
        this.temperature = temp;
        notifyObservers();
    }

    void notifyObservers() {
        for (Observer o : observers) {
            o.update(temperature);
        }
    }
}

// Observer interface
interface Observer {
    void update(float temperature);
}

// Concrete observers
class PhoneDisplay implements Observer {
    @Override
    public void update(float temperature) {
        System.out.println("Phone: " + temperature + "°C");
    }
}

class WebDisplay implements Observer {
    @Override
    public void update(float temperature) {
        System.out.println("Web: " + temperature + "°C");
    }
}
```

**Relation to AOP:** Observer modularizes event handling but still requires manual wiring — every subject must explicitly manage its observer list and call `notifyObservers()`. [[aspect-oriented-programming]] can automate this with pointcuts: "whenever `setTemperature()` is called, execute the display update" — no manual wiring needed.

## Common Pitfalls
- **Pattern fever**: Applying patterns everywhere, even where simple code suffices
- **Cargo culting**: Using a pattern without understanding the problem it solves
- **Over-engineering**: Adding indirection (Factory, Strategy, etc.) for problems that don't need it
- **Missing the intent**: Patterns solve specific problems; using them for different problems causes confusion
- **Rigid application**: Patterns are templates, not recipes — adapt them to context

## Connections
- [[aspect-oriented-programming]] — some patterns (Observer, Template Method) are alternative ways to handle crosscutting concerns without aspects
- [[object-oriented-programming]] — design patterns are reusable OOP solutions
- [[java-for-software-analysis]] — Java implements patterns idiomatically
- [[software-analyse-lecture-9]] — lecture connects patterns to aspect-oriented analysis

## Open Questions
- When does a pattern become over-engineering?
- How do patterns relate to the SOLID principles?
- Can AOP replace certain patterns entirely, or do they serve complementary purposes?
- How do design patterns evolve in modern languages with first-class functions and closures?
