#This is a spring boot app and goes by jar packaging.

Go to your project application-properties and
#/* You need to change the file path based on your system */
path.to.csv=E:\\.code\\file-io\\submissions\\hanisntsolo\\csv-spotify-data-logger\\src\\main\\resources\\spotify-2023.csv

#In a server like scenario the file path is in opt/ directory and is volume mapping is fixed most of the times.

In order to run this app locally you need to fire command

java -jar path/to/jar

Example in the project base dir

java -jar target/csv-spotify-data-logger-0.0.1-SNAPSHOT.jar