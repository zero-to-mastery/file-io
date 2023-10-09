package com.example.demo.Services;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import org.springframework.stereotype.Service;

@Service
public class CsvServices {
	
	private List<List<String>> records = new ArrayList<>();
	int count=0;
	
	private List<String> getRecordFromLine(String line) {
		
	    List<String> values = new ArrayList<String>();
	    try (Scanner rowScanner = new Scanner(line)) {
	        rowScanner.useDelimiter(",");
	        while (rowScanner.hasNext()) {
	            values.add(rowScanner.next());
	        }
	    }
	    return values;}
	
	public void CsvParseData() throws FileNotFoundException {
	
	try (Scanner scanner = new Scanner(new File("src/main/resources/spotify-2023.csv"))) {
	    while (scanner.hasNextLine()) {
	        records.add(getRecordFromLine(scanner.nextLine()));
	    }
	}
	System.out.println("Number of songs in the file "+records.size());
	for(List<String> list: records) {
		for(String s: list) {
			if(s.equals("E")) {
				count++;
			}
		}
	}
	System.out.println("Number of songs with Key E in the file "+count);

	}
	
}
