package com.spring.hellospringboot;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class Helloworld {
    @GetMapping
    public List<String> getHelloworld(){
        String x = "HACKTOBER FEST 2021 !!!";
        return List.of(x);
    }
}
