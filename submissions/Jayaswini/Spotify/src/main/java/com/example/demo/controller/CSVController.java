package com.example.demo.controller;

import java.io.FileNotFoundException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.Services.CsvServices;

@RestController
public class CSVController {
	@Autowired
	private CsvServices csv;
	@GetMapping("/csv")
	private void csvData() {
		try {
			csv.CsvParseData();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
