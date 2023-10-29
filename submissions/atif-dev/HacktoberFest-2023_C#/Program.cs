using System;
using System.Diagnostics;
using System.Xml.Linq;
using Bytescout.Spreadsheet;

class Program
{
    static void Main(string[] args)
    {
        string filePath = "spotify-2023.csv"; /*File location: \bin\Debug\net7.0*/
        Spreadsheet document = new Spreadsheet();

        document.LoadFromFile(filePath);

        //Read data from the first worksheet.
        Worksheet worksheet = document.Workbook.Worksheets[0];

     /*******************************************Total No. Of Songs*******************************/

        int row;
        int totalSongs = 0; 
        for (row = 1; row <= worksheet.UsedRangeRowMax; row++)
        {
            /*Cell cell = worksheet.Cell(row, 0); //first column*/
            totalSongs++;
        }

        Console.WriteLine($"*******************************************************");
        Console.WriteLine($"Total Songs: {totalSongs}");
        Console.WriteLine($"*******************************************************");

        document.Close();

        Console.WriteLine("Press any key to exit.");
        Console.ReadKey();
    }
}
