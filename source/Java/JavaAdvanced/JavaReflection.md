# Java 反射和注解

## Java反射

Java反射机制：

在运行状态中，

（1）对任意一个类，能获取其所有的属性和方法

（2）对任意一个对象，能调用其任意方法和属性

这种动态获取信息、以及动态调用对象方法的功能，就是Java语言的反射机制

## Class类

Java源代码编译后产生字节码，类加载器子系统通过二进制字节流，从文件系统加载class文件

执行时，把字节码文件读入JVM（这个过程叫类的加载）

然后在内存中创建对应的一个java.lang.Class对象，这个对象被放入字节码信息中，对应加载的那个字节码信息，可以当做程序访问方法区中这个类的各种数据的外部接口

**java.lang**中提供了Class类

## 获取类字节码信息（四种方法）

1. 通过getClass()方法
2. 通过类的class这个内置属性
3. 通过Class类提供的静态方法forName，需传入全限定名（包名+类名）
4. 利用类的加载器

```java
package com.pyrad.testReflection;

public class testReflection {
    public static void main(String[] args) throws ClassNotFoundException {
        // 获取类字节码信息的四种方法
        // 1. 通过getClass()方法
        Person p = new Person();
        Class aClass = p.getClass();
        System.out.println(aClass);

        // 2. 通过类的class这个内置属性
        Class bClass = Person.class;
        System.out.println(bClass);

        // 3. 通过Class类提供的静态方法forName，需传入全限定名（包名+类名）
        String qaulifiedName = "com.pyrad.testReflection.Person";
        Class cClass = Class.forName(qaulifiedName);
        System.out.println(cClass);

        // 4. 利用类的加载器
        ClassLoader cloader = testReflection.class.getClassLoader();
        Class dClass = cloader.loadClass(qaulifiedName);
        System.out.println(dClass);

        // 这四个类都是同一个对象，因为在JVM里面，类的字节码只会加载一次，所以其对象也只有一个
        System.out.println(aClass == bClass);
        System.out.println(aClass == cClass);
        System.out.println(aClass == dClass);
    }
}

class Person {
    public int age;
    double height;
    protected double weight;
    private double wage;

    public Person() {
        this.age = 0;
        this.height = 0;
        this.weight = 0;
        this.wage = 0;
    }
}
```

## Class类的具体实例

可以从以下6种结构得到具体的Class类

1. 类：外部类，内部类
2. 接口
3. 注解
4. 数组
5. 基本数据类型
6. void

对于数组，只要是同一个维度，同一种元素类型，得到的字节码就是同一个

```java
public class testClassInJVM {
    public static void main(String[] args) {
        Class c1 = Person.class;
        Class c2 = Comparable.class;
        Class c3 = Override.class;

        int[] arr0 = {1, 2, 3};
        int[] arr1 = {4, 5, 6};
        Class c40 = arr0.getClass();
        Class c41 = arr1.getClass();
        // 对于数组，只要是同一个维度，同一种元素类型，得到的字节码就是同一个
        System.out.println(c40 == c41);

        Class c50 = int.class;
        Class c51 = double.class;
        Class c52 = byte.class;
        Class c53 = char.class;

        Class c6 = void.class;
    }
}
```



## 获取构造器

1. 通过Class类的**getContructors()**获得public修饰的所有**Constructor**（返回Constructor数组）
2. 通过Class类的**getDeclaredConstructors()**获得包括各种修饰（public, default, protected, private）的所有**Constructor**（返回Constructor数组）
3. 通过Class类的**getContructor(Class ...)**获得public修饰的指定类参数的**Constructor**
4. 通过Class类的**getDeclaredConstructor(Class ...)**获得包括private修饰的在内的指定类参数的**Constructor**

```java

public static void test1() throws Exception {
    Class cls = Student.class;
    Constructor[] ctrs = cls.getConstructors();
    for (Constructor c : ctrs) { System.out.println(c); }

    Constructor[] ctrs0 = cls.getDeclaredConstructors();
    for (Constructor c : ctrs0) { System.out.println(c); }

    Constructor ctr = cls.getConstructor();
    System.out.println(ctr);

    Constructor ctr1 = cls.getConstructor(String.class, int.class);
    System.out.println(ctr1);

    Constructor ctr2 = cls.getDeclaredConstructor(int.class, int.class);
    System.out.println(ctr2);

    // 创建实例并调用
    Object obj = ctr1.newInstance("Pyrad", 18);
    Student s = (Student) obj;
    s.cry();
    
    // 获得名字
    String n = ctr.getName();
    System.out.println(n);
    // 获得注解
    Annotation [] aarr = ctr.getAnnotations();
    for (Annotation a : aarr) { System.out.println(a); }
    // 获取构造函数的修饰限定符
    // 因为可能是如public static这样的，所以是加了getModifiers，而不是getModifier
    int mf0 = ctr.getModifiers();
    // 返回值是一个整型，可以通过Modifier工具类得到对应的字符串
    System.out.println(Modifier.toString(mf0));
    // 获得参数列表
    Class[] mf1 = ctr.getParameterTypes();
    for (Class c : mf1) { System.out.println(c); }
}
```



## 获取方法

和获取一个类的constructor类似，

1. 通过Class类的**getMethods()**获得public修饰的所有**Method**（返回Method数组）
2. 通过Class类的**getDeclaredMethods()**获得包括各种修饰（public, default, protected, private）的所有**Method**（返回Method数组）
3. 通过Class类的**getMethod(Class ...)**获得public修饰的指定类参数的**Method**
4. 通过Class类的**getDeclaredMethod(Class ...)**获得包括private修饰的在内的指定类参数的**Method**

也可以通过Method上的方法，获取关于某个具体Method的结构信息，一般方法（函数）的结构如下：

***@注解***

***修饰限定符 返回值 函数名(参数列表) throw 异常 {}***

包括注解和异常在内的所有信息，都可以获取到，参考下面的代码：

```java
public static void testGetMethod() throws Exception {
    Class cls = Student.class;
    Method[] marr0 = cls.getMethods();
    for (Method m : marr0) { System.out.println(m); }

    Method[] marr1 = cls.getDeclaredMethods();
    for (Method m : marr1) { System.out.println(m); }

    Method m0 = cls.getMethod("shout");
    System.out.println(m0);

    Method m1 = cls.getMethod("shout", String.class);
    System.out.println(m1);
    
    Method m2 = cls.getDeclaredMethod("smile");
    System.out.println(m2);

    /**
     * 一般函数的具体结构
     * @注解
     * 修饰限定符 返回值 函数名(参数列表) throw 异常 {}
     */

    // 获取注解，注意只能获取生命周期是Runtime的注解
    Annotation[] as = m0.getAnnotations();
    for (Annotation s : as) { System.out.println(s); }
    // 获取方法的限定符
    int mfs = m0.getModifiers();
    System.out.println(Modifier.toString(mfs));
    // 获取方法的返回值类型
    Class rt = m0.getReturnType();
    System.out.println(rt);
    // 获取方法的参数列表
    Class[] ps = m0.getParameterTypes();
    for (Class c : ps) { System.out.println(c); }
    // 获取异常
    Class[] es = m0.getExceptionTypes();
    for (Class c : es) { System.out.println(c); }

    // 调用方法
    Object o = cls.newInstance();
    m0.invoke(o);
    m0.invoke(o, "Hello!!");
}
```



## 获取类所实现的接口，注解，包名字



```java
public static void testGetInterfacePackage() throws Exception {
    Class cls = Student.class;
    // 获取该类的接口
    Class[] itfs = cls.getInterfaces();
    for (Class i : itfs) { System.out.println(i); }
    // 获取该类的父类的接口
    Class supercls = cls.getSuperclass();
    Class[] itfs0 = supercls.getInterfaces();
    for (Class i : itfs0) { System.out.println(i); }
    // 获取该类的包名
    Package pkg = cls.getPackage();
    System.out.println(pkg);
    System.out.println(pkg.getName());
    // 获取该类的注解
    Annotation[] as = cls.getAnnotations();
    for (Annotation a : as) { System.out.println(a); }
}
```



## 两个问题

- 用new <类>还是用反射创建一个类的实例？（反射的应用场合）
  程序运行起来之后才知道要创建一个什么的样的对象的时候，更适合用反射
- 反射是否破坏了面向对象的封装性？
  表面上是的，但封装的含义是建议用不同的访问限制外面的操作；反射虽然确实可以调用private修饰的方法等，但实际上实践中还是不建议使用。



# Junit

Junit是白盒测试

没有Junit时候的缺点

1. 要放在main方法中，以便运行
2. 为了测试不同的功能，需要定义多个测试类或方法 
3. 测试逻辑和业务逻辑混淆在一起，逻辑上不够清晰

Junit

1. 导入Junit的包
2. 定义一个函数
3. 加上Test注解
4. 可以在函数内加入断言
5. 如有需要，可以定义开始结束函数（用于申请和释放资源等），并加入对应的**Before**/**After**注解

```java
import org.junit.Assert;
import org.junit.Test;

@Before
public void beforeRunning() { System.out.println("--- Starting ---"); }

@After
public void afterRunning() { System.out.println("--- Ending ---"); }

@Test
public void testJunit() {
    System.out.println("this is a Junit");
    int a = 10/2;
    Assert.assertEquals(5, a);
}
```



# 注解

## 历史

注解（Annotation），也叫元数据，JDK 5.0引入

## 什么是注解？

- 代码里的***特殊标记***，这些标记在编译、类加载和运行时被读取，并执行相应处理。
- 可以不改变原有源代码的逻辑，在源文件中加入一些补充信息
- 代码分析工具、开发工具和部署工具可以通过这些信息进行验证或进行部署
- 使用时，在其前面加入**```@```**符号，并把注解当做一个修饰符使用，用于修饰它支持的程序元素

## 重要性

- 可当做修饰符使用，可以用来修饰包、类、构造器、方法、成员变量、参数、局部变量等的声明
- 信息被保存在Annotation的**"name=value"**对中，
- JavaSE注解的使用目的比较简单，JavaEE/Android中更重要（比如配置应用程序的切面，代替旧版JavaEE中繁冗的代码和XML配置）
- 开发模式基于注解的
  - JPA ：Java的持久化API
  - Spring2.5以上
  - Hibernate3.x之后
- 一定程度上：**框架 = 注解 + 反射 + 设计模式**



## 文档注解

一般使用在文档注释中，配合javadoc工具使用

注意事项

- @param @return和@exception只用于方法
- @param的格式：@param 形参 形参类型 形参说明
- @return的格式：@return 返回值类型 返回值说明（如果方法的返回值是void，就不能写）
- @exception格式：@exception 异常类型 异常说明
- @param和@exception可以并列多个

IDEA中使用Java doc：Tools -> Generate JavaDoc，在Other command line argument中加入```-encoding utf-8 -charset utf-8```，以防生成乱码



## JDK内置的3个注解

- @Override：限定重写父类方法，该注解只能用于方法（防止写错重写的方法）
- @Deprecated：用于表示所修饰的元素（类、方法、构造器、属性等）已过时
- @SuppressWarnings：抑制编译器警告

```java
@Override
public int weight() { return 200; }

@Deprecated
public void move() { System.out.println("moving"); }

public void msg() {
    @SuppressWarnings("unused")
    int age = 10;

    @SuppressWarnings({"unused", "rawtype"})
    ArrayList al = new ArrayList();
}
```



## 元注解

元注解是修饰其他注解的注解，JDK 5.0之后提供了4种

- **Retention**
  - 修饰注解的生命周期
  - 包含一个叫RetentionPolicy枚举类型的成员变量，使用时必须指定其值
  - **RetentionPolicy.SOURCE**：只在源文件中有效
  - **RetentionPolicy.CLASS**：在class文件中（字节码文件）有效，运行Java程序时，不会加载，不会保留在内存里，JVM不会保留该类型的注解。如果注解没有加Retention的元注解，默认值就是RetentionPolicy.CLASS
  - **RetentionPolicy.RUNTIME**：运行时有效，运行Java程序时，JVM会保留注释，加载在内存中，程序可以通过反射获取该注解
- **Target**
  - 只有一个成员变量value，该成员变量的值是一个枚举类型，值有TYPE，CONSTRUCTOR，FIELD等等
  - 这个元注解用来限定注解的应用在哪些元素上，比如所定义的注解只能修饰类、属性、构造器等到
- **Documented**
  - 如果用来修饰注解，JavaDoc就会把这个注解提取到API中
- **Inherited**
  - 如果用来修饰注解，那么这个被定义的注解如果使用在父类上，其子类就会自动继承这个用在父类上的注解，即相当于子类也使用了父类的那个注解
  - 这个元注解用的比较少



## 自定义注解

- 一般情况大多使用现成的注解，很少用自定义的注解

- 使用```@interface```关键字定义

- 在注解定义里面，```String[] value()```这样的实际是一个成员变量，只是看上去像一个无参方法

  - 无参方法的名字是成员变量的名字（只有一个参数的话，约定俗成叫value）
  - 无参方法的返回值是成员变量的类型
  - 无参方法的类型：基本数据类型，String，枚举，注解，或者它们对应的数组

- 注意事项

  - 如果定义了配置参数，就要给配置参数赋值
  - 如果只有一个配置参数，并且名字是value的话，使用的时候```value = XXX ```中的```value = ```可以省略不写
  - 定义注解时，配置参数可以有默认值
  - 如果配置参数有默认值，那么可以不写后面的```value = XXX```而直接使用默认值
  - 如果注解没有定义配置参数，可以叫**标记**，如果注解定义了配置参数，可以叫**元数据**

  ```java
  public @interface Galaxy {
      String[] value();
  }
  
  // 配置参数有默认值
  public @interface Galaxy2 {
      String value() default "kkk";
  }
  
  // 使用注解，Galaxy2的配置参数有默认值，可以省略其值
  @Galaxy2
  @Galaxy(value = {"Planet", "weight"})
  class Planet {
      public int weight() {
          return 100;
      }
  }
  ```

  

  

