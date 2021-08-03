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

