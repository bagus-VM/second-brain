---
title: "Java for Software Analysis — Essential Concepts"
tags: [concept, software-analyse, java, maven, junit, javaparser, asm, weka, picocli, semester-1]
course: "Software Analyse"
source_count: 2
status: current
last_updated: 2026-06-05
prerequisites: []
---

## One-line Summary
*Everything you need to know about Java, Maven, and the libraries used in both Software Analyse projects — explained for someone who'd rather be writing Python.*

## Core Intuition

You hate Java. Fine. But these two projects use Java-specific tools that you MUST understand for the exam. This page is your survival guide — no "hello world" tutorials, just the concepts that actually matter.

---

## Java Basics You Actually Need

### Classes and Objects

```java
public class Dog {
    private String name;        // field (instance variable)
    private int age;            // field

    public Dog(String name, int age) {  // constructor
        this.name = name;       // 'this' refers to the current instance
        this.age = age;
    }

    public String getName() {   // getter method
        return name;
    }
}
```

**Key rules:**
- `public` = accessible from anywhere. `private` = only within this class.
- `this.name` = the field. `name` = the parameter. Use `this.` to disambiguate.
- Methods return a type (`String`, `int`, `void` for nothing). 

### Enums — Critical for Sign Analysis

```java
public enum SignValue {
    BOTTOM, MINUS, ZERO, ZERO_MINUS, PLUS, PLUS_MINUS, ZERO_PLUS, TOP;
}
```

An enum is a type with a fixed set of constants. Each constant has an `ordinal()` (its position, starting from 0).

**Why enums are perfect for lattices:**
- Fixed set of values (you can't add new ones at runtime)
- Built-in `ordinal()` for indexing
- Can have methods: `SignValue.join(a, b)` works like a static method
- Can use `values()` array: `SignValue.values()[3]` gives `ZERO_MINUS`

### Generics

```java
Map<String, Integer> counts = new HashMap<>();  // maps Strings to Integers
List<SignValue> values = new ArrayList<>();      // a list of SignValues
```

Generics are Java's way of saying "this collection holds X type." The `<>` is the diamond operator — it infers the type from context.

### Interfaces and Abstract Classes

```java
public interface TransferRelation {
    SignValue evaluate(int constant);
    SignValue evaluate(Operation op, SignValue lhs, SignValue rhs);
}

public abstract class FeatureMetric {
    public abstract double computeMetric(String codeSnippet);
    public abstract String getIdentifier();
}
```

- **Interface:** A contract. Any class that "implements" it must provide all methods. Multiple interfaces allowed.
- **Abstract class:** A partial implementation. Can have both abstract and concrete methods. Only one parent allowed.
- In the projects: `TransferRelation` is an interface. `FeatureMetric` is an abstract class. `SignTransferRelation` implements `TransferRelation`. `NumberLinesFeature` extends `FeatureMetric`.

### Static Methods and Fields

```java
public class MathUtils {
    public static int add(int a, int b) {  // static = no instance needed
        return a + b;
    }
}
// Usage: MathUtils.add(2, 3) — no 'new MathUtils()'
```

Static methods belong to the class, not an instance. They can't access `this` or instance fields.

### Annotations

```java
@Override                    // "I'm overriding a parent method"
@Test                        // "This is a JUnit test"
@CommandLine.Command(...)    // picocli: marks a class as a CLI command
```

Annotations are metadata. They don't change code behavior directly but tell the compiler, framework, or tool something about the method/class.

### Streams and Lambdas (Java 8+)

```java
// Lambda: anonymous function
(x) -> x * 2                    // takes x, returns x*2
(a, b) -> a + b                 // takes a and b, returns a+b

// Stream: functional iteration
List<String> names = List.of("Alice", "Bob", "Charlie");
names.stream()
     .filter(n -> n.length() > 3)    // keep names longer than 3 chars
     .map(String::toUpperCase)        // convert to uppercase
     .toList();                        // collect to list
// Result: [ALICE, CHARLIE]
```

**In the projects:** You'll see `.stream().map().collect()` patterns for transforming collections. The `::` is a method reference — shorthand for `s -> s.toUpperCase()`.

### Exceptions

```java
try {
    String content = Files.readString(path);  // might throw IOException
} catch (IOException e) {
    System.err.println("Failed to read file: " + e.getMessage());
}
```

Java forces you to handle checked exceptions (like `IOException`). Unchecked exceptions (like `NullPointerException`) don't need explicit handling.

---

## Maven — The Build System

### What is Maven?

Maven is Java's build tool. Think of it as `pip` + `make` + `pytest` combined. It handles:
- **Dependencies** (like requirements.txt)
- **Compilation** (like make)
- **Testing** (like pytest)
- **Packaging** (like pyinstaller)

### pom.xml — The Configuration File

```xml
<project>
    <dependencies>
        <dependency>
            <groupId>org.ow2.asm</groupId>      <!-- package namespace -->
            <artifactId>asm</artifactId>         <!-- package name -->
            <version>9.9</version>               <!-- version -->
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <!-- runs JUnit tests -->
            </plugin>
        </plugins>
    </build>
</project>
```

### Key Commands

```bash
mvn compile          # compile source code
mvn test             # run all tests
mvn clean test       # delete old build artifacts, then test
mvn package          # create a JAR file
mvn dependency:copy-dependencies  # copy all dependency JARs
```

### The Project Structure

```
project/
├── pom.xml                          ← Maven config
├── src/                             ← source code (non-standard layout)
│   └── de/uni_passau/.../           ← Java package structure
│       ├── SignValue.java
│       └── SignTransferRelation.java
├── test/                            ← test code (non-standard layout)
│   └── de/uni_passau/.../
│       └── SignValueTest.java
└── target/                          ← compiled output (generated)
    ├── classes/                     ← compiled .class files
    └── test-classes/                ← compiled test .class files
```

**Non-standard layout:** Normally Maven uses `src/main/java/` and `src/test/java/`. These projects use `src/` and `test/` directly. This is configured in the pom.xml.

---

## Libraries You Need to Know

### 1. JavaParser — AST Parsing (Used in Readability Project)

**What it does:** Parses Java source code into an Abstract Syntax Tree (AST).

**Why you need it:** You can't compute metrics like cyclomatic complexity by counting characters. You need to understand the STRUCTURE of the code — which parts are if-statements, which are loops, which are operators. JavaParser gives you that structure.

**Key concept — the Visitor Pattern:**

```java
public class CyclomaticComplexityVisitor extends VoidVisitorAdapter<Void> {
    private int complexity = 0;

    @Override
    public void visit(IfStmt n, Void arg) {
        complexity++;              // count this if-statement
        super.visit(n, arg);       // continue visiting children
    }

    @Override
    public void visit(ForStmt n, Void arg) {
        complexity++;              // count this for-loop
        super.visit(n, arg);       // continue visiting children
    }
}
```

**How it works:**
1. Parse code into AST: `Parser.parseJavaSnippet(code)` returns a `BodyDeclaration`
2. Create a visitor: `new CyclomaticComplexityVisitor()`
3. Walk the tree: `ast.accept(visitor, null)` — calls `visit()` for each node type
4. Read results: `visitor.getComplexity()`

**The visitor pattern is the core design pattern in both projects.** Every feature extraction (Readability) and every bytecode instruction handling (Sign Analysis) uses some form of visitor.

**AST node types you'll see:**
- `IfStmt` — if statement
- `ForStmt` — for loop
- `BinaryExpr` — binary operation (a + b, a == b)
- `UnaryExpr` — unary operation (!a, -a)
- `MethodCallExpr` — method call
- `AssignExpr` — assignment (a = b)
- `VariableDeclarator` — variable declaration with optional initializer
- `FieldAccessExpr` — field access (obj.field)
- `ConditionalExpr` — ternary (a ? b : c)

**Parse start — CLASS_BODY:**
```java
StaticJavaParser.parse(code, ParseStart.CLASS_BODY);
```
This tells JavaParser to parse the code as a class body (methods, fields, inner classes), NOT as a full compilation unit (which would require package declaration, imports, etc.). The `.jsnp` files are class body fragments.

### 2. ASM — Bytecode Framework (Used in Sign Analysis)

**What it does:** Reads and manipulates Java bytecode (`.class` files).

**Why you need it:** Sign analysis operates on BYTECODE, not source code. Bytecode is what the JVM actually executes. ASM gives you:
- `ClassReader`: reads a `.class` file into memory
- `ClassNode` / `MethodNode`: in-memory representation
- `Analyzer`: generic fixpoint dataflow engine
- `Interpreter`: abstract class you override for your transfer functions

**Key concept — the Interpreter framework:**

```java
public class SignInterpreter extends Interpreter<SignValue> {
    private final TransferRelation transferRelation;
    private final Map<String, MethodNode> methods;

    @Override
    public SignValue newOperation(AbstractInsnNode insn) {
        // Handle constant loading: ICONST_0, BIPUSH, SIPUSH, LDC
        switch (insn.getOpcode()) {
            case ICONST_0: return transferRelation.evaluate(0);
            case ICONST_1: return transferRelation.evaluate(1);
            // ... etc
        }
    }

    @Override
    public SignValue binaryOperation(AbstractInsnNode insn, SignValue lhs, SignValue rhs) {
        // Handle: IADD, ISUB, IMUL, IDIV
        switch (insn.getOpcode()) {
            case IADD: return transferRelation.evaluate(Operation.ADD, lhs, rhs);
            case IDIV: return transferRelation.evaluate(Operation.DIV, lhs, rhs);
            // ... etc
        }
    }

    @Override
    public SignValue naryOperation(AbstractInsnNode insn, List<SignValue> values) {
        // Handle method calls: INVOKEVIRTUAL, INVOKESTATIC, etc.
        // → recursive inter-procedural analysis
    }
}
```

**The Analyzer does the heavy lifting:**
```java
Analyzer<SignValue> analyzer = new Analyzer<>(interpreter);
Frame<SignValue>[] frames = analyzer.analyze(className, methodNode);
// frames[i] = abstract state BEFORE instruction i
// frames[i].getLocal(j) = abstract value of local variable j
// frames[i].getStack(k) = abstract value at stack position k
```

**JVM Stack Machine Basics:**
- The JVM is a **stack machine** — operations push/pop from a stack
- `ICONST_5` pushes the constant 5 onto the stack
- `IADD` pops two ints, pushes their sum
- `IDIV` pops two ints, pushes their quotient
- `ISTORE_1` pops an int and stores it in local variable 1
- `ILOAD_1` pushes local variable 1 onto the stack

```
int x = 5;      →  ICONST_5  →  [5]
                  ISTORE_1   →  []        (local 1 = 5)

int y = x + 3;  →  ILOAD_1   →  [5]
                  ICONST_3   →  [5, 3]
                  IADD       →  [8]
                  ISTORE_2   →  []        (local 2 = 8)
```

### 3. WEKA — Machine Learning (Used in Readability Project)

**What it does:** A Java ML library with classifiers, filters, and evaluation tools.

**Why you need it:** You've extracted features from code snippets. Now you need to train a model. WEKA does this in Java.

**Key classes:**
- `Instances`: A dataset (table of rows × columns)
- `Logistic`: Logistic regression classifier
- `Standardize`: Z-score normalization filter
- `Evaluation`: Cross-validation and metrics

**The pipeline:**
```java
// 1. Load CSV
DataSource source = new DataSource(csvPath);
Instances dataset = source.getDataSet();
dataset.setClassIndex(dataset.numAttributes() - 1);  // last column = class

// 2. Apply filter (standardize)
Standardize filter = new Standardize();
filter.setInputFormat(dataset);
Instances normalized = Filter.useFilter(dataset, filter);

// 3. Train and evaluate
Logistic classifier = new Logistic();
classifier.setRidge(1e-6);  // regularization
Evaluation eval = new Evaluation(normalized);
eval.crossValidateModel(classifier, normalized, 10, new Random(1));
```

**FilteredClassifier** wraps the filter + classifier together so the filter is applied automatically during cross-validation:
```java
FilteredClassifier fc = new FilteredClassifier();
fc.setFilter(new Standardize());
fc.setClassifier(new Logistic());
eval.crossValidateModel(fc, dataset, 10, new Random(1));
```

### 4. picocli — CLI Framework

**What it does:** Parses command-line arguments into Java objects.

**Why you need it:** Both projects have CLI entry points. Instead of manually parsing `args[]`, picocli does it with annotations.

```java
@Command(name = "analysis", subcommands = {Preprocess.class, Classify.class})
public class Main implements Runnable {
    public void run() { System.out.println("Use a subcommand"); }
}

@Command(name = "preprocess")
public class SubcommandPreprocess implements Callable<Integer> {
    @Option(names = "-s", required = true)
    private Path sourceDir;

    @Option(names = "-g", required = true)
    private Path groundTruth;

    @Parameters  // positional args
    private List<String> features;

    public Integer call() {
        // sourceDir, groundTruth, features are already populated
        // ... do the work ...
        return 0;
    }
}
```

**Usage:**
```bash
java -cp ... Main preprocess -s snippets/ -g truth.csv LINES TOKEN_ENTROPY H_VOLUME
```

### 5. JUnit — Testing Framework

**What it does:** Runs unit tests.

**Key annotations:**
- `@Test` — marks a method as a test
- `@BeforeEach` — runs before each test (setup)
- `@ParameterizedTest` — runs the same test with different inputs

**Assertions:**
```java
assertEquals(expected, actual);      // equality check
assertTrue(condition);               // boolean check
assertThrows(Exception.class, () -> { /* code that should throw */ });
```

**AssertJ (fluent assertions):**
```java
assertThat(result).isEqualTo(expected);
assertThat(list).hasSize(3).contains("a", "b");
```

---

## Design Patterns Used in Both Projects

### 1. Visitor Pattern (Both Projects)

Used in: `CyclomaticComplexityVisitor`, `OperatorVisitor`, `OperandVisitor`, `SignInterpreter`

**Problem:** You have a tree/graph of objects (AST nodes or bytecode instructions) and want to perform different operations on them without modifying the node classes.

**Solution:** Define a visitor class with a `visit()` method for each node type. The tree "accepts" the visitor, which dispatches to the right method.

### 2. Strategy Pattern (Both Projects)

Used in: `FeatureMetric` abstraction, `TransferRelation` interface

**Problem:** You want to swap algorithms at runtime.

**Solution:** Define an interface, implement it in multiple classes, inject the right one.

### 3. Template Method (Readability Project)

Used in: `FeatureMetric.computeMetric()` is abstract; subclasses fill in the details.

**Problem:** The algorithm skeleton is the same (parse → compute → return), but the computation step varies.

**Solution:** Abstract class defines the skeleton, subclasses override the variable step.

---

## Connections

- [[readability-classifier]] — Uses JavaParser, WEKA, picocli, JUnit
- [[sign-analysis]] — Uses ASM, picocli, JUnit
- [[visitor-pattern]] — The central design pattern in both projects
- [[data-flow-analysis]] — Sign Analysis's Analyzer uses fixpoint iteration

---

## Open Questions
- What's the difference between checked and unchecked exceptions?
- When would you use an abstract class vs. an interface?
- How does Java's type erasure affect generics at runtime?
