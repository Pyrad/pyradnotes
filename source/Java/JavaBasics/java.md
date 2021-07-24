# Heading 0

## Heading 1

### Heading 2

#### Heading 3

---



# Font

---

**This is bold font**

*This is Italic font*

***This is bold & Italic font***

~~This is slash font~~



# Image

---

![Riho](../../_static/riho.jpg)











# Hyperlink

---

[My Link](www.google.com)



# List

---

### Unordered List

- row a
- row b
- row c

### Ordered List

1. row a 
2. row b
3. row c



# Table

---

| name  | sex  | age  |
| ----- | ---- | ---- |
| Pyrad | Male | 18   |







# Java内存

---

1. 线程内存区域
   1. 程序计数器
   2. Java虚拟机栈
   3. 本地方法栈
2. 堆
3. 方法区
4. 运行时常量池
5. 直接内存

- Java VM启动时会开启Garbage Collection的线程
  - **引用计数法**
  - **引用可达法（根搜索算法）**
  
- **三种GC**
  
  - Minor GC：清理年轻代，Eden区满了就出发一次Minor GC，清理无用对象，将有用的对象复制到Survivor1和Survivor2中
  - Major GC：清理年老代
  - Full GC：可以清理年轻代、年老代，有性能影响。
  
- **年轻代**
  
  - Eden区：（1个）尽可能收集生命周期短的对象（新生成的对象首先放这里），对应**Minor GC**，复制算法效率高，但浪费内存空间。
  - survivor区：（2个，分别是from和to）
  
- **年老代**
  
  - Eden区经过N（一般是15）次GC之后仍然存活的，被放到这里。
  - 有一个tenured区
  - 当年老代越来越多的时候，启动**Major GC**和**Full GC**全面清理年轻代和年老代区
  
- **永久代**
  
  - 用于存放静态文件，如Java类，方法等。持久代对GC没有显著的影响
  - JDK7以前是**方法区**的一种实现
  - JDK8之后使用元数据和metaspace
  
- 在一个java class类的构造器（constructor）里可以调用重载的其他的构造器，但必须是位于函数体的第一句，且使用this

  ```java
  public class User {
      int id;
      String name;
      String pwd;
      
      public User(int id, String name) {
          this.id = id;
          this.name = name;
      }
      
      public User(int id, String name, String pwd) {
          this(id, name); // <- overloaded constructor
          this.pwd = pwd;
      }
  }
  ```

  

# 面向对象三大特征

- 继承
  - Java中类只有单继承，没有C++中的类多继承
  - 但是Java中有接口的多继承
- 封装
- 多态
- Java中使用extends来实现继承

# 运算符 instanceof 

instanceof是二元运算符

```java
System.out.println(s instanceof Person);
System.out.println(s instanceof Student);
```



# 类中方法的重写

Java中重写函数的返回值，可以是本类的object，也可以是直接父类的object，但不可以是间接父类的object（爷爷辈的class）



# 关键字final

- 修饰变量：一旦被赋值，不能再改变
- 修饰方法：方法不可被重写，但可以被重载
- 修饰类：修饰的类不能被继承



# equals和==

- ==

  就是比较两个object的地址是否相同

- equals

  Object类里面的method，默认就是比较两个object的地址，但是可以被重载，用来比较两个object的内容是否相同（或者其他用途）

# super

可以看做是子类对父类对象的引用，可以通过super来引用父类的方法和熟悉（成员）

一个类中，构造方法的第一行没有显示调用super(...)或this(...)，Java编译器会自动默认调用super()，即调用父类的无参数构造函数。



# 封装

|  修饰符   | 同一个类 | 同一个包中 | 子类 | 所有类 |
| :-------: | :------: | :--------: | :--: | :----: |
|  private  |    *     |            |      |        |
|  default  |    *     |     *      |      |        |
| protected |    *     |     *      |  *   |        |
|  public   |    *     |     *      |  *   |   *    |



父类和子类在同一个包中，子类***可以***访问父类的protected成员，也***可以***访问父类对象的protected成员

父类和子类不在同一个包中，子类***可以***访问父类的protected成员，但***不可以***访问父类对象的protected成员



# 多态

同一个方法调用，由于对象的不同可能有不同的行为。



# 向下类型转换

类似于C++中的强制类型转换

```java
class Animal {
    public static void main() {
        System.out.println("Animal");
    }
    public void shout() {
        System.out.println("shout!");
    }
}

class Dog extends Animal {
    public static void main(String [] args) {
        Animal a = new Dog();
        Dog d = (Dog)a;  //<-- casting
        d.shout();
    }
    public void shout() {
        System.out.println("Wang!");
    }   
}
```



# 抽象类和抽象方法

```java
abstract class Animal { // <-- 抽象类只能被继承，不能实例化
    abstract public void shout(); //<-- 抽象方法在父类中可以不实现
}

class Dog extends Animal {
    public void shout() { // <-- 抽象方法必须在子类中实现
        System.out.println("Shout!");
    }
}
```

- 有抽象方法的类只能是抽象类
- 抽象类不能实例化
- 抽象类只能被继承
- 抽象类的方法必须被子类实现



# 接口

- 规范和实现彻底分离，即接口里面只有规范。

- 可以这样讲，接口是类的图纸，类是对象的模板。

- 接口中的常量总是public static final（可以省略）

- 接口中的方法总是public abstract（可以省略）

- 接口可以继承别的接口

- 接口可以多继承

- JDK8以后接口里面可以加入普通的静态方法和默认方法

- 接口里面的static method和它的继承里面的static method（哪怕函数名一样），是不同的两个函数（在方法区里面是不同的内存区域）

  ```java
  interface A {
      default void moren() {
          System.out.println("go");
      }
      
      public static void testStaticMethod() {
           System.out.println("testStaticMethod A");
      }
  }
  
  class TestA implements A {
      public static void testStaticMethod() {
           System.out.println("testStaticMethod TestA");
      }
      public static void main(String[] args) {
          System.out.println("InterfaceTester");
          TestA a = new TestA();
          a.testStaticMethod(); // <- testStaticMethod A
          A.testStaticMethod(); // <- testStaticMethod TestA
      }
  }
  ```

  

# String类

- 不可变字符序列
- 在java.lang中
- Java字符串就是Unicode字符序列
- Java没有内置字符串类型
- 需要掌握的常用方法：
  - char charAt(int index)
  - boolean equals(String other)
  - boolean equalsIgnoreCase(String other)
  - int indexOf(String str)
  - lastIndexOf()
  - int length()
  - String replace(char oldChar, char newChar)
  - boolean startsWith(String prefix)
  - boolean endsWith(String prefix)
  - String substring(int beginIndex)
  - String substring(int beginIndex, int endIndex)
  - String toLowerCase()
  - String toUpperCase()
  - String trim()
- 

# 常量池

1. 全局字符常量池

   每个VM中只有一份，放字符串常量池的引用（堆中生成字符串对象实例）

2. class文件常量池

   编译时每个class都有，在编译阶段，存放的是常量（文本字符串，final常量）和符号引用

3. 运行时常量池



# 内部类

定义在一个类的内部，分为

1. 成员内部类（非静态内部类和静态内部类）

2. 匿名内部类

3. 局部内部类

## 非静态内部类

非静态内部类主意事项：

- 内部类可以直接访问外部类的private成员
- 非静态内部类必须依存于一个外部类对象
- 非静态内部类不能有静态方法、静态属性和静态初始化块

## 静态内部类

- 可以看做是外部类的一个静态成员
- 可以访问外部类的静态成员，不能访问外部类的普通成员

## 匿名内部类

适合只使用一次的类

## 局部内部类

在方法中定义的类，作用域在于该方法内部（类似C++和Python中的lambda）

```java
package com.pyrad.testInnerClass;

public class testInnerClass {

    private int id = 0;
    static private int cnt = 0;

    public static void main(String[] args) {
        testInnerClass.Inner inn0 = new testInnerClass().new Inner();
        inn0.showInner();

        testInnerClass out0 = new testInnerClass();
        testInnerClass.Inner inn1 = out0.new Inner();
        inn1.showInner();

        testInnerClass.InnerStatic inn2 = new testInnerClass.InnerStatic();
        inn2.show();

        // Anonymous inner class usage
        testInnerClass out1 = new testInnerClass();
        out1.test(new A() {
                      @Override
                      public void run() {
                          System.out.println("run");
                      }
                  }
                );

    }

    public void show() {
        System.out.println("testInnerClass");
    }

    /**
     * 非静态内部类
     */
    public class Inner {
        private String m_name = "Tom";
        private int id = 0;
        public void showInner() {
            System.out.println("My name is " + m_name);
            System.out.println(id);
            System.out.println(testInnerClass.this.id);
        }
    }

    /**
     * 静态内部类
     */
    static class InnerStatic {
        private String m_name = "Java";
        public void show() {
            System.out.println(testInnerClass.cnt);
        }
    }

    public void test(A a) {
        a.run();
    }
}


interface A {
    void run();
}
```

# 创建对象的步骤

1. 分配对象空间，对象成员变量初始化为0或空
2. 执行属性值的显示初始化
3. 执行构造方法
4. 返回对象地址

# Java虚拟机内存模型

## 栈

- 描述方法执行的模型，每个方法调用时会创建一个栈帧（存储局部变量、操作数、方法出口等）
- JVM给每个线程创建一个栈，用来存放改线程执行的信息（实际参数、局部变量等）
- 栈是线程私有，不能线程间共享
- 栈是”先进后出，后进先出“
- 栈由系统自动分配，速度快，是连续的内存空间

## 堆

- 用于存储创建的对象和数组
- JVM只有一个堆，被所有线程共享
- 堆是一个不连续的内存空间，分配灵活但速度慢

## 方法区

- 方法区是Java虚拟机的规范可以有不同的实现
  - JDK7以前是**永久代**
  - JDK7部分去除**永久代**，静态变量、字符串常量池都挪到了堆内存中
  - JDK8是元数据空间和堆结合起来
- JVM只有一个方法区，被所有线程共享
- 实际上也是堆，只是用于存储类、常量相关的信息
- 用来存储程序中永远不变或唯一的内容

## 垃圾回收机制

- 针对***堆***中的对象



# 数组

- 定义

  - 数组变量属于引用类型，数组也是对象
  - 数组存元素的类型可以是任何类型
  - 数组是对象，数组中的元素是对象的属性
    - 初始化有默认初始化，动态初始化，以及静态初始化
  - 代码示例

  ```java
  package com.pyrad.testArray;
  
  public class testArray {
      public static void main(String[] args) {
          System.out.println("Array testing");
          testArray t = new testArray();
          t.test();
      }
  
      public void test() {
  
          int[] arr = new int[10]; // 默认初始化：0
          boolean[] barr = new boolean[10]; // 默认初始化：false
          String[] sarr = new String[10]; // 默认初始化：null
  
          // 静态初始化
          int[] arr1 = {0, 1, 2, 3};
          boolean[] barr1 = {false, true, false};
          String[] sarr1 = {"good", "bad"};
          Man[] marr = {new Man(0, "Jim"), new Man(1,"Tom"), new Man(2, "Kate")};
  
          // 动态初始化
          int[] s = null;
          s = new int[10];
          for (int i = 0; i < 10; i++) {
              s[i] = 2 * i + 1;
              System.out.println(s[i]);
          }
          for (int i = 0; i < s.length; i++) {
              System.out.println(s[i]);
          }
  		// for-each loop：只能读取，不能修改元素的值
          for (int k : s) {
              System.out.println(k);
          }
          
          // Copy (deep copy)
          String[] src = {"Jim", "Tom", "Kate"};
          String[] dest = new String[src.length];
          System.arraycopy(src, 0, dest, 0, src.length);
          for (String cstr : dest) {
              System.out.println(cstr);
          }
          
          // Arrays class test
          int[] iarr = {4, 3, 5, 1, 2, 0};
          System.out.println(Arrays.toString(iarr));
          Arrays.sort(iarr);
          System.out.println(Arrays.toString(iarr));
          System.out.println(Arrays.binarySearch(iarr, 3));
      }
  }
  
  class Man {
      private int m_id;
      private String m_name;
      Man(int id, String name) {
          this.m_id = id;
          this.m_name = name;
      }
      public void show() {
          System.out.printf("Name: %s, ID: %d\n", m_id, m_name);
      }
  }
  ```

  

- 四个特点

- 常见操作

  - 普通遍历
  - for-each
    - 增强型的for循环只能读取，不能修改元素的值
  - 数组拷贝
    - System.arraycopy
  - java.util.Array类
    - 提供排序、查找、填充、打印等相关方法

- 多维数组

  - 内存结构

    ```java
    package com.pyrad.testArrayMultiple;
    
    import java.lang.reflect.Array;
    import java.util.Arrays;
    
    /**
     * 多维数组
     */
    public class testArrayMultiple {
        public static void main(String[] args) {
            defaultInit();
            staticInit();
            dynInit();
        }
    
        // 默认初始化
        public static void defaultInit() {
            int[][] a = new int[3][];
            a[0] = new int[2];
            a[1] = new int[4];
            a[2] = new int[3];
    
            for (int[] ca : a) {
                System.out.println(Arrays.toString(ca));
            }
        }
    
        // 静态初始化
        public static void staticInit() {
            int[][] a = {{1, 3}, {1, 3, 7, 8}, {2, 0, 1}};
            a[0] = new int[2];
            a[1] = new int[4];
            a[2] = new int[3];
    
            for (int[] ca : a) {
                System.out.println(Arrays.toString(ca));
            }
        }
    
        // 动态初始化
        public static void dynInit() {
            int[][] a = new int[3][];
            a[0] = new int[]{1, 3};
            a[1] = new int[]{1, 3, 7, 8};
            a[2] = new int[]{2, 0, 1};
    
            for (int[] ca : a) {
                System.out.println(Arrays.toString(ca));
            }
        }
    }
    
    ```

    

  - 存储表格

  - Javabean和数组存储表格

- 常见算法

- comparable接口

  - 重写类中的compareTo接口即可
    - 大于规则：返回1
    - 等于规则：返回0
    - 小于规则：返回-1

# 常用的类

1. 基本数据类型的包装类(Wrapper class)

   - | 基本数据类型 |   包装类    |
     | :----------: | :---------: |
     |     byte     |    Byte     |
     |   boolean    |   Boolean   |
     |    short     |    Short    |
     |     char     |  Character  |
     |     int      | **Integer** |
     |     long     |    Long     |
     |    float     |    Float    |
     |    double    |   double    |

   - Number类是抽象类，它提供了一些抽象方法：intValue(), doubleValue(), floatValue(), doubleValue()等。

   - 自动装箱和拆箱(JDK 1.5之后)

     ```java
     // autoboxing & unboxing
     Integer i7 = 3; // > JDK 1.5, autoboxing
     int i8 = i7; // > JDK 1.5, unboxing
     ```

     

   - **包装类的缓存**

     如果第二次或以上使用同一个**[-128, 127]**之间的数字，返回缓存数组中的某个元素

     ```java
     Integer i9 = 4000;
     Integer i10 = 4000;
     Integer i11 = 123;
     Integer i12 = 123;
     System.out.println(i9 == i10);  // false
     System.out.println(i11 == i12); // true, wrapper class cache, implemented in Integer.valueOf()
     System.out.println(i9.equals(i10)); // true
     ```

     

2. 字符串相关（String）

   - **String**：不可变字符序列
   - **StringBuilder**：可变字符序列（效率高，线程不安全）
   - **StringBuffer**：可变字符序列（效率低，线程安全）

3. 时间处理
   时间在java里也是一个long类型的数组，以1970.1.1 00:00:00为时间原点
   **Date**类提供时间的基本操作
   **Calendar**类是一个抽象类，提供关于日期计算的功能，其一个具体子类是**GregorianCalendar**。

   ```java
   import java.text.ParseException;
   import java.text.SimpleDateFormat;
   import java.util.Date;
   import java.util.Calendar;
   import java.util.GregorianCalendar;
   
   
   public static void test() {
           SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
           try {
               Date d1 = df.parse("1998-10-21 23:12:29");
               System.out.println(d1);
   
               Date d2 = new Date(1000L * 3600 * 23);
               String str = df.format(d2);
               System.out.println(str);
           } catch (ParseException e) {
               e.printStackTrace();
           }
   }
   
   public static void test2() {
           GregorianCalendar c = new GregorianCalendar(2021, 7, 19, 21, 2, 23);
           int cur_y = c.get(Calendar.YEAR);
           int cur_m = c.get(Calendar.MONTH);
   
           c.set(Calendar.DATE, 3);
   
           c.add(Calendar.MONTH, +3);
   
           GregorianCalendar c0 = new GregorianCalendar();
           c0.setTime(new Date());
   
           System.out.println(c);
           System.out.println(c0);
   
   }
   ```

   

4. 其他
   **Math**类：abs，acos，asin，sin，cos，sqrt，pow，max，min，ceil，floor，random（[0,1)之间的随机数），round，toDegrees，toRadians
   **Random**类

   ```java
       public static void test() {
           Random r = new Random();
           r.nextDouble();
           r.nextInt();
           r.nextFloat();
           r.nextBoolean();
           r.nextInt(10);
       }
   ```

   **File**类
   在java.io.File中，默认创建文件在系统定义的***user.dir***中

   ```java
   package com.pyrad.testFile;
   
   import java.io.File;
   import java.io.IOException;
   import java.util.Date;
   
   public class testFile {
       public static void main(String[] args) throws IOException {
           test();
       }
   
       public static void test() throws IOException {
           // Get current project's path
           System.out.println("Current project path is:");
           System.out.println(System.getProperty("user.dir"));
   
           // default path is: user.dir
           File f = new File("first.java.txt");
           if (f.exists()) {
               System.out.printf("File %s already exists\n", f.getName());
               System.out.println("File is directory:" + f.isDirectory());
               System.out.println("File is file:" + f.isFile());
               System.out.println("File size:" + f.length());
               System.out.println("File last modified:" + new Date(f.lastModified()));
               // Other operations:
               // boolean suc = f.mkdir()
               // f.mkdirs()
               // f.delete()
           } else {
               f.createNewFile();
               System.out.printf("Create file %s\n", f.getName());
           }
   
           File f2 = new File("C:\\Users\\Pyrad\\IdeaProjects\\JavaLearn\\src\\com\\pyrad\\testFile\\java.2nd.txt");
           f2.createNewFile();
       }
   }
   ```

   枚举

   枚举类隐式地继承了**java.lang.Enum**

   ```java
   public class testEnum {
       public static void main(String[] args) {
           test();
       }
   
       public static void test() {
           System.out.println(Season.SPRING);
           System.out.println(Season.valueOf(Season.AUTUMN.name()));
           System.out.println(Season.valueOf(Season.AUTUMN.name()));
   
           for (Week k : Week.values()) {
               System.out.println(k);
           }
   
           int a = new Random().nextInt(4);
           Season[] ss = Season.values();
           switch (ss[a]) {
               case SPRING:
                   System.out.println("Spring");
                   break;
               case SUMMER:
                   System.out.println("Summer");
                   break;
               case AUTUMN:
                   System.out.println("Autum");
                   break;
               case WINTER:
                   System.out.println("Winter");
                   break;
               default:
                   System.out.println("Not known");
                   break;
           }
       }
   }
   
   enum Season {
       SPRING, SUMMER, AUTUMN, WINTER
   }
   
   enum Week {
       MON, TUE, WED, THU, FRI, SAT, SUN
   }
   ```




# 异常

第一步：抛出异常对象

第二步：捕获异常对象

异常对象都是继承于**java.lang.Throwable**类，**Throwable**有两个子类**Error**和**Exception**。

Error类不用处理也处理不了，但Exception可以处理。

Exception类分为两种：**CheckedException**和（**RuntimeException**）**UncheckedException**。

不管有无异常，**finally**都会执行，通常用来释放前面申请的资源

处理方式：

（1）捕获异常

（2）声明异常

（3）try-with-resource（新，JDK7，它可以自动关闭实现了**AutoClosable**接口的类）

```java
// （1）捕获并处理异常
try {
    // whatever
} catch (Exception e1) {
    e1.printStackTrace();
} catch (Exception e2) {
    e2.printStackTrace();
} finally {
    // always execute here, no matter there's exception or not
}

// （2）声明异常：谁调用谁处理
static public void test() throws Exception {
     System.out.println("Might exception");
}


    static public void test3() {
        try (FileReader reader = new FileReader("d:/a.txt");){
            char c = (char) reader.read();
            System.out.println(c);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
```

自定义异常

一般定义两个构造器：default constructor和带有信息的constructor

```java
class IllegalAgeException extends Exception {
    // default constructor
    public IllegalAgeException() {}
    // constructor with message
    public IllegalAgeException(String msg) {
        super(msg);
    }
}
```



# 泛型

## 简单总结

主要解决编译期间的安全问题

简单示例

```java
public class testGeneric {
    public static void main(String[] args) {
        MyGeneric<String> ms = new MyGeneric<>();
        ms.show();
        ms.print("kkkk");

        MyGeneric<String> ms0 = new MyGeneric<>("ttt");
        ms.show();
        ms.print("ssss");
    }
}

// 如果要加上public访问修饰符，那么当前的.java文件名称必须是MyGeneric.java
class MyGeneric <T> {
    private T m_key;
    MyGeneric() { m_key = null; }
    MyGeneric(T k) { m_key = k; }
    public void show() { System.out.println(m_key); }
    public void print(T k) { System.out.println(k); }
}
```



经过编译之后，JVM都会把泛型替换成Object。

- 基本类型不能用于泛型：```Test<int> t;```这样的写法是错误的。
- 不能通过类型参数创建对象```T elem = new T();```这样的写法是错误的。

### 通配符？

- 上限限定：可以是泛型方法，也可适用泛型类。```<? extends Father>```
- 下限限定：只能用于泛型方法，不能用于泛型类。```<? super Child>```

### 泛型可变长参数

```java
public <T> Generic(T...arg) {
}
```



# Java容器

## 单例集合

祖先接口是Collection，有两个子接口List（有序可重复）、Set（无序无重复）

List有三个子类：ArrayList, LinkedList, Vector

Set有个子类：HashSet

## 双例集合

双例集合：key-value对，父接口是Map

有几个子类：HashTable，HashMap，TreeMap，LinkedHashMap，Property

## Collection的抽象方法

add

remove

contains

size

isEmpty

clear

iterator

containsAll

addAll（并集）

removeAll（差集）

retainAll（交集）

 toArray



## List接口的其他方法

add(int, Object)

set(int, Object)

get(int)

remove(int)
indexOf(Object)

lastIndexOf(Object)



## ArrayList类

- 本质是动态数组，底层用数组实现（底层以**1.5**倍上次数组大小的方式扩容）

- 线程不安全；多线程中可以用Vector或CopyOnWriteArrayList

- ArrayList底层用数组实现的。特点：查询效率高，增删效率低，线程不安全。

- 有几个两个重要对象

  - **elementData**：是一个Object[]，即object的数组
  - **size**：动态数组的实际大小
  - **DEFAULTCAPACITY_EMPTY_ELEMENTDATA**（一个final的空数组，默认构造时会赋值给elementData，JDK1.8之后的特点，**延迟加载**）

- 继承自AbstractList，并实现了以下几个接口

  - List：提供基本的增删改和遍历
  - RandomAccess：支持随机访问
  - Cloneable：可被克隆
  - java.io.Serializable：即可以支持序列化

  ```java
  public class ArrayList<E> extends AbstractList<E>
          implements List<E>, RandomAccess, Cloneable, java.io.Serializable {}
  ```

- 包含的方法

  ```java
  // Collection中定义的API
  boolean             add(E object)
  boolean             addAll(Collection<? extends E> collection)
  void                clear()
  boolean             contains(Object object)
  boolean             containsAll(Collection<?> collection)
  boolean             equals(Object object)
  int                 hashCode()
  boolean             isEmpty()
  Iterator<E>         iterator()
  boolean             remove(Object object)
  boolean             removeAll(Collection<?> collection)
  boolean             retainAll(Collection<?> collection)
  int                 size()
  <T> T[]             toArray(T[] array)
  Object[]            toArray()
  // AbstractCollection中定义的API
  void                add(int location, E object)
  boolean             addAll(int location, Collection<? extends E> collection)
  E                   get(int location)
  int                 indexOf(Object object)
  int                 lastIndexOf(Object object)
  ListIterator<E>     listIterator(int location)
  ListIterator<E>     listIterator()
  E                   remove(int location)
  E                   set(int location, E object)
  List<E>             subList(int start, int end)
  // ArrayList新增的API
  Object              clone()
  void                ensureCapacity(int minimumCapacity)
  void                trimToSize()
  void                removeRange(int fromIndex, int toIndex)
  ```

- 三种遍历方式

  ```java
  List<String> a = new ArrayList<>(20); //可以用父类的引用（指针）
  a.add("good"); a.add("day"); a.add("today");
  
  // 迭代器遍历
  Iterator itr = b.iterator(); // itr开始没有指向任何值
  while (itr.hasNext()) {
      String cur = (String) itr.next();
      System.out.println(cur);
  }
  System.out.println("----");
  
  // 索引遍历（随机访问）
  for (int i = 0; i < b.size(); i++) {
      System.out.println(b.get(i));
  }
  System.out.println("----");
  
  // 增强for循环遍历
  b.remove(b.iterator().next());
  for (String s : b) {
      System.out.println(s);
  }
  ```



## Vector类

Vector实现了List的接口，底层也是用数组实现的，相关的方法都有**同步检查**，所以是线程安全的。

Vector和ArrayList的使用基本上是一样的（方法基本都相同）

Vector扩容的倍数是以原先容量的**2倍扩容**

Vector采用的**默认初始化方式**是**立即初始化**，即最开始给elementData数组初始化为capacity是10（即容量为10）的数组。



## Stack类

Stack是**Vector**类的一个**子类**，即继承于Vector，特点是LIFO（Last In First Out）

扩展了Vector的5个方法

```java
boolean empty() // 查看栈是否空
E       peak() // 查看栈顶
E       pop() // 出栈
E       push(E item) // 入栈
int     search(Object o) // 返回元素在栈中的位置
```



```java
// 一个stack检查括号匹配的小程序
public static boolean symmetry() {
    String symbol = "...{..[..(...).....]..}...";
    Stack<String> stk = new Stack<>();
    for (int i = 0; i < symbol.length(); i++) {
        char c = symbol.charAt(i);
        if (c == '{') { stk.push("}"); }
        if (c == '[') { stk.push("]"); }
        if (c == '(') { stk.push(")"); }
        if (c == '}' || c == ']' || c == ')') {
            if (stk.empty()) {
                return false;
            }
            if (stk.peek().charAt(0) != c) {
                return false;
            }
            stk.pop();
        }
    }

    return stk.empty();
}
```



## LinkedList

- 也是实现了**List**的接口

- 底层用**双向链表**实现存储，查询效率低，增删效率高，线程不安全

- 继承（实现）关系

  ```java
  public class LinkedList<E>
      extends AbstractSequentialList<E>
      implements List<E>, Deque<E>, Cloneable, java.io.Serializable {}
  ```

  

- 重要的成员变量

  ```java
  transient int size;
  transient Node<E> first; // 指向链表的第一个元素
  transient Node<E> last; // 指向链表的最后一个元素
  ```

  

- 节点表示，是**LinkedList**的一个内部类

  ```java
  class Node<E> {
      E item;
      Node<E> next;
      Node<E> prev;
  }
  ```

- LinkedList除了Collection中的方法，还有自己的如下方法

  ```java
  void addFirst(E e); //元素添加到链表开头
  void addLast(E e); // 元素添加到链表尾
  getFirst(); // 返回链表第一个元素
  getLast(); // 返回链表最后一个元素
  removeFirst(); // 移除第一个元素，并返回该元素
  removeLast(); // 移除最后一个元素，并返回该元素
  E pop(); // 等效于removeFirst，移除头部元素（第一个）
  void push(E e); //等效于addFirst，在头部添加元素（第一个）
  boolean isEmpty();
  ```

  

## Set接口

- Set在是个**接口**，继承自Collection接口，但其方法和Collection的完全一致，并没有新增方法。
- 无序，不可重复，类似于C++中的std::set、std::unordered_set
- 常见的Set
  - HashSet
  - TreeSet



## HashSet

- 就是一个没有重复元素的集合

- 底层是**HashMap**实现的（简化版的HashMap）

- **HashMap**底层是用<font color='red'>**数组**</font>（默认初始长度16）和<font color='red'>**链表**</font>实现的，对元素的哈希值（**```hashCode```**方法）进行运算，然后决定元素在数组中的位置，同时也会通过元素的**```equals()```**方法来判断两个元素是否相同，如果相同则不会添加重复的元素（<font color='red'>**注意**</font>：是在元素的哈希值运算之后的值相同的时候，才会调用**```equals()```**方法，否则不会调用**```equals()```**方法）

- 如果经过对元素的hash值进行计算得到值相同，并且调用**```equals()```**方法也返回true，那么就会在该元素的位置（实际上是一个链表的节点）上生成一个链表（单向链表）把元素放到链表的下一个位置上，这就是前面提到的“底层是用<font color='red'>**数组**</font>（默认初始长度16）和<font color='red'>**链表**</font>实现的”

- 成员变量

  ```java
  private transient HashMap<E, Object> map;
  // Dummy value to associate with an Object in the backing Map
  // 即把key-value对里面的value固定给一个无意义的值，那么map就变成了set
  private static final Object PRESETN = new Object();
  ```

  

- HashSet中允许有null元素

- 利用Hash算法（散列算法）

- 因为是无序的，所以不能通过index索引来访问（其实和C++中的一模一样）

- 常见操作

  ```java
  public static void test() {    
      Set<String> sset = new HashSet<>();    
      sset.add("k"); sset.add("o"); sset.add("m"); sset.add("z");    
      for (String s : sset) {        
          System.out.println(s);    
      }    
      System.out.println(sset.contains("o") ? "Value exist" : "Value not found");    
      System.out.println(sset.remove("z"));    
      System.out.println(sset.remove("p"));        
      Set<Users> uset = new HashSet<>();	
      Users u = new Users("Pyrad", 18);	
      Users v = new Users("Pyrad", 18);	
      // 只有一个元素在uset中，因为Users类里面重写了hashCode和equals方法    
      for (Users cu : uset) {         
          System.out.println(cu);    
      }
  }
  // 可以通过重写自定义类的hashCode和equals方法来使用Set，以便达到想要的效果
  class Users {    
      private String username;    
      private int userage;    
      public Users(String username, int userage) { this.username = username; this.userage = userage;}    
      public Users() {}    
      public String getUsername() { return username;}    
      public void setUsername(String username) { this.username = username; }    
      public int getUserage() { return userage; }    
      public void setUserage(int userage) { this.userage = userage; }    
      @Override    
      public String toString() {        
          return "Users{" +                
              "username='" + username + '\'' +                
              ", userage=" + userage +                
              '}';    
      }    
      @Override    
      public boolean equals(Object o) {        
          if (this == o) return true;        
          if (o == null || getClass() != o.getClass()) 
              return false;        
          Users users = (Users) o;        
          return userage == users.userage && Objects.equals(username, users.username);    
      }    
      @Override    
      public int hashCode() {        
          return Objects.hash(username, userage);    
      }        
      // 如果要用于TreeMap或TreeSet    
      // (1) 就要在元素对应的类中实现接口Comparable<E>，并且重写compareTo    
      // (2) 或者在外部使用比较器    
      @Override    
      public int compareTo(Users o) {        
          if (this.getUsername().compareTo(o.getUsername()) == 0) {            
              return 1;        
          }       
          if (this.getUserage() > o.getUserage()) {          
              return 1;       
          }        
          return -1;    
      }
  }
  ```

## TreeSet容器

- 可以对元素进行排序

- 底层是TreeMap实现的，通过key来存储元素（TreeSet里面显然只使用到了key）

- TreeMap是用红黑树实现的

- 继承关系

  ```java
  public class TreeSet<E> extends AbstractSet<E>    
      implements NavigableSet<E>, Cloneable, java.io.Serializable// NavigableSet -> NvaigableMap -> SortedMap
  ```

- 成员变量

  ```java
  private transient NavigableMap<E, Object> m;
  private static final Object PRESENT = new Object();
  ```

- 需要给的排序规则

  - 通过元素自身实现比较规则（需要实现元素（就是类自己）Comparable接口中的compareTo方法）```Users```中的compareTo方法见如上

  - 通过比较器定义比较规则

    ```java
    import java.util.Comparator;
    // 如果Users类中没有compareTo方法，可以通过定义一个比较器类，传入其构造函数来实现
    public class UserComparator implements Comparator<Users> {   
        @Override   
        public int compare(Users o1, Users o2) {  
            return o1.compareTo(o2); 
        }
    }
    public static void test() {    
        Set<Users> uset2 = new TreeSet<>(new UserComparator());    
        uset2.add(u1); uset2.add(u2);
        for (Users s : uset2) {         
            System.out.println(s);      
        } 
    }
    ```

- 常用方法

  ```java
  public static void test() {   
      Set<String> tset = new TreeSet<>();  
      tset.add("d"); tset.add("c"); tset.add("a"); tset.add("c"); tset.add("b");  
      // 因为内部是红黑树，对加入的元素会排序，所以输出a,b,c和d   
      for (String s : tset) {        
          System.out.println(s); 
      }
  }
  ```

  

## Map接口

- Map是一个接口

- Map接口定义双例集合，它**不是**Collection的子接口

- 和C++中的std::map, std::unordered_map非常相似，比较理解即可

- 常用

  - TreeMap
  - HashMap

- Map接口中的常用方法

  ```java
  V put(K key, V value);               // 添加键值对，如果key已存在，会覆盖原有的key-value对，然后返回value；如果可以不存在，就返回null
  void putAll(Map m);                  // 复制另一个Map到此Map（并运算）
  V remove(Object key);                // 删除key对应的key-value对
  V get(Object key);                   // 得到key对应的value
  boolean containsKey(Object key);     // 是否有key
  boolean containsValue(Object value); // 是否有value
  Set keySet();                        // 取得所有key，并存储到Set中
  Set<Map.Entry<K,V>> entrySet();      // 返回一个Set，其Set的key是k-v对，在Map中以Map的内部类表示：Map.Entry<K,V>
  void clear();                        // 清空
  ```

## HashMap

- 是Map接口的实现类

- 底层采样哈希表存储数据，key重复的话，后面添加的会覆盖之前已经存在的key-value对

- 遍历方法

  ```java
  Map<String, String> m = new HashMap<>();
  String v = m.put("a", "A"); v = m.put("b", "BBS"); v = m.put("c", "CCS");v = m.put("d", "DDS");
  Set<String> allkeys = m.keySet();
  for (String s : allkeys) {  
      String cv = m.get(s);  
      System.out.println(cv);
  }
  Set<Map.Entry<String, String>> kvs = m.entrySet();
  for (Map.Entry<String, String> kv : kvs) { 
      System.out.println(kv.getKey() + ": " + kv.getValue());
  }
  ```

  
