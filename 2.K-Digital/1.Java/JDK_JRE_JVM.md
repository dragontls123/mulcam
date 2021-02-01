![](markdown-img/jvm_jre_jdk.png)

# JDK⊃JRE+@⊃JVM+@



## JDK(Java Development Kit)

- 자바 프로그래밍시 필요한 컴파일러 등을 포함

- JRE+@



## JRE(Java Runtime Environment

- 컴파일된 자바 프로그램을 실행시킬 수 있는 자바 환경

- JVM+@



## JVM(Java Virtual Machine)

- 자바 바이너리 파일(.class) 실행

- 플랫폼 의존적

- 역할 
  - 자바 애플리케이션을 클래스 로더를 통해 읽어 들여 자바 API와 함께 실행
  - JAVA와 운영체제 사이에서 중재자 역할을 수행하여 OS에 구애받지 않고 재사용을 가능하게 해줌
  - 메모리관리, Garbage Collection