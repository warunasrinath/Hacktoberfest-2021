package com.spring.hellospringboot;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class Helloworld {
    @GetMapping
    public List<String> getHelloworld(){
        return List.of("Hello Woorld");
    }
}
