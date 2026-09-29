---
title: "Visitor Pattern"
tags: [concept, software-analyse, semester-1, software-analyse]
course: "Software Analyse"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites: ["[[java-for-software-analysis]]"]
---

## One-line Summary
The Visitor pattern separates an algorithm from the object structure it operates on by letting you define new operations on a tree of objects without modifying their classes.

## Core Intuition
Imagine you have a tree of Java code elements (classes, methods, statements, expressions) and you want to do different things with it: count cyclomatic complexity, extract Halstead metrics, check for bugs. Without the visitor pattern, you'd add a `computeComplexity()` method, a `computeHalstead()` method, and a `checkBugs()` method to *every* node class. That's messy — every new analysis requires changing every class. The visitor pattern flips this: you keep the tree structure stable and define each analysis as a separate "visitor" that walks the tree.

## Formal Definition / Statement

### Structure
- **Element:** The nodes of the tree (e.g., AST nodes: IfStatement, ForLoop, MethodCall)
- **Visitor:** A class with a `visit(ElementType)` method for each element type
- **accept(visitor):** Each element has an `accept(visitor)` method that calls `visitor.visit(this)`

### Double Dispatch
The pattern uses double dispatch — the operation depends on both the element type AND the visitor type:
1. Element.accept(visitor) → calls visitor.visit(this)
2. The compiler resolves `this` to the concrete type, selecting the right visit() overload

### Interface
```
interface ASTVisitor {
    void visit(IfStatement node);
    void visit(ForLoop node);
    void visit(MethodCall node);
    void visit(ReturnStatement node);
    // ... one method per element type
}

interface ASTNode {
    void accept(ASTVisitor visitor);
}
```

## Key Properties / Complexity

### Advantages
- **Open/Closed Principle:** Add new operations (visitors) without modifying element classes
- **Single Responsibility:** Each visitor encapsulates one analysis
- **State accumulation:** Visitors can maintain state across the traversal (e.g., a running count of complexity)

### Disadvantages
- **Rigid hierarchy:** Adding a new element type requires updating ALL visitors (violates OCP for elements)
- **Boilerplate:** Each visitor needs a method for every element type
- **Encapsulation break:** Visitors often need access to element internals

### When to Use
- Stable element hierarchy with many operations (analyses)
- Exactly the scenario in software analysis: AST nodes rarely change, but new analyses are added frequently

## Worked Example
**Cyclomatic Complexity Visitor (from Readability Classifier project):**

```java
class CyclomaticComplexityVisitor implements ASTVisitor {
    private int complexity = 0;
    
    @Override
    public void visit(IfStatement node) {
        complexity++;  // if = one decision point
        super.visit(node);  // recurse into children
    }
    
    @Override
    public void visit(ForLoop node) {
        complexity++;  // loop = one decision point
        super.visit(node);
    }
    
    @Override
    public void visit(ConditionalExpr node) {
        complexity++;  // ternary ? : = one decision point
        super.visit(node);
    }
    
    // Default: just recurse, no complexity increment
    @Override
    public void visit(MethodCall node) {
        super.visit(node);
    }
    
    public int getComplexity() {
        return complexity + 1;  // +1 for the method itself
    }
}
```

The visitor walks the entire AST, incrementing a counter at each decision point. The `+1` accounts for the single straight-through path.

**Sign Analysis Visitor (from Sign Analysis project):**
Uses ASM's `ClassVisitor`/`MethodVisitor` to walk Java bytecode and perform fixpoint dataflow analysis — same pattern, different framework.

## Common Pitfalls
- Forgetting to recurse into children — if `visit(IfStatement)` doesn't call `super.visit()`, nested structures are missed
- Not handling all element types — unvisited elements are silently skipped
- Double-counting with JavaParser — calling `super.visit()` on certain nodes triggers child visits that also call `visit()` on sub-elements
- Confusing the pattern with the Strategy pattern — Strategy encapsulates one algorithm per class; Visitor encapsulates one *traversal* with multiple operations

## Connections
- [[java-for-software-analysis]] — Both projects (Readability Classifier and Sign Analysis) use the visitor pattern extensively
- [[readability-classifier]] — HalsteadVolumeVisitor, CyclomaticComplexityVisitor, OperatorVisitor, OperandVisitor
- [[sign-analysis]] — ClassVisitor/MethodVisitor from ASM framework
- [[data-flow-analysis]] — Analysis visitors perform fixpoint iteration over the CFG
- [[abstract-syntax-tree]] — The tree structure that visitors traverse
- [[widening-narrowing]] — Widening may be applied within analysis visitors for loop convergence

## Open Questions
- How does the visitor pattern compare to pattern matching in functional languages (e.g., Scala match expressions)?
- Can the visitor pattern be made type-safe without exhaustive switch statements?
- When is the Acyclic Visitor pattern (with default methods) preferable to the classic visitor?
