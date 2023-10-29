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

        /*******************************************Total Songs in Key of E**************************/

        int rowB;
        int countESong = 0;
        string toFind = "E";
        for (rowB = 1; rowB <= worksheet.UsedRangeRowMax; rowB++)
        {

            Cell cell = worksheet.Cell(rowB, 15);
            if (cell.Value != null)
            {
                string cellValue = (string)cell.Value;
                if (string.Equals(cellValue, toFind, StringComparison.OrdinalIgnoreCase))
                {
                    countESong++;
                }
            }
        }
        Console.WriteLine($"Total Songs in Key of E: {countESong}");
        Console.WriteLine($"*******************************************************");

        /************************Occurrences of Values in a Specified Column and Most Common Value************************/

        Console.WriteLine($"Occurrences of values in a specified column:\n");
        /*Console.Write("Write name of a column from .csv file(to find Occurrences of Values) and press enter: ");
        string columnName = Console.ReadLine() ?? "";*/
        string columnName = "artist(s)_name"; //Specified column
        if (columnName != null && columnName != "")
        {
            Console.WriteLine($"||| Specified Column Name: {columnName} |||\n");

            string cellValue;
            string[] workSheetMax = new string[worksheet.UsedRangeRowMax];

            // Find the column index based on the column name.
            int columnIndex = -1;
            for (int col = 0; col <= worksheet.UsedRangeColumnMax; col++)
            {
                Cell headerCell = worksheet.Cell(0, col);

                #pragma warning disable CS8600
                string cellValue2 = Convert.ToString(headerCell.Value);
                #pragma warning restore CS8600

                if (string.Equals(cellValue2, columnName, StringComparison.OrdinalIgnoreCase))
                {
                    columnIndex = col;
                    break;
                }
            }

            if (columnIndex != -1)
            {
                for (int csvRow = 1; csvRow <= worksheet.UsedRangeRowMax; csvRow++)
                {
                    Cell cell = worksheet.Cell(csvRow, columnIndex);

                    #pragma warning disable CS8600
                    cellValue = Convert.ToString(cell.Value);
                    #pragma warning restore CS8600

                    if (cellValue != null)
                        workSheetMax[csvRow - 1] = cellValue;
                }

                List<string> valuesList = workSheetMax.ToList();
                var valueCounts = valuesList.GroupBy(value => value).Select(group => new
                {
                    Value = group.Key,
                    Count = group.Count()
                }).ToList();
                foreach (var count in valueCounts)
                {
                    Console.WriteLine($">{count.Value}: occured {count.Count} time(s).");
                    /*Console.WriteLine("-------------------------------------------------------------------------------");*/
                }

                //----Most common value-----
                var mostCommonValue = valuesList.GroupBy(value => value).Select(group => new
                {
                    Value = group.Key,
                    Count = group.Count()
                }).OrderByDescending(group => group.Count).First().Value;

                Console.WriteLine("-------------------------------------------------------------------------------");
                Console.WriteLine($"{mostCommonValue} is the most common value in specified column {columnName}.");
                Console.WriteLine($"*******************************************************************************");
            }
            else
            {
                Console.WriteLine($"Column '{columnName}' not found in the worksheet.");
            }


        }
        else
        {
            Console.WriteLine($"{columnName} Column name is INVALID");
        }

        document.Close();

        Console.WriteLine("Press any key to exit.");
        Console.ReadKey();
    }
}
