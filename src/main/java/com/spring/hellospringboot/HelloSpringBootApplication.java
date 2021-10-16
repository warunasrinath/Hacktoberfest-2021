package com.spring.hellospringboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloSpringBootApplication {

    public static void main(String[] args) {
        SpringApplication.run(HelloSpringBootApplication.class, args);
        System.out.println(addNumber(40,44));
    }

 public static int addNumber(int a,int b) {
     return a+b;
    }
}
