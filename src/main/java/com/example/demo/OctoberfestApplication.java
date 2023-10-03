package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.example.demo.Services.CsvServices;

@SpringBootApplication
public class OctoberfestApplication {

	public static void main(String[] args) {
	
		SpringApplication.run(OctoberfestApplication.class, args);
		
	}

}
