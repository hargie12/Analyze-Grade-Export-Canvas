<html>
   <body>
    <h1>Clean and Analyze Grades Export from Canvas CSV</h1>
    <p> This script is designed to look at a Canvas Grades Export and pull retention information. This script was designed for Midterm grades but could be used at any interval.</p>
    <h2>Importing Libraries</h2>
    <p>The code imports the pandas and numpy libraries, which will be used for data manipulation and analysis.</p>
    <h2>Setting Pandas Options</h2>
    <p>The pandas options are set to display all rows and columns in the DataFrame when it is printed to the console.</p>
    <h2>Reading in Midterm Grades</h2>
    <p>The code reads in a CSV file containing midterm grades and stores it in a pandas DataFrame called 'grades'.</p>
    <h2>Handling Missing Data</h2>
    <p>Any blank values in the 'current score' column are replaced with 0.</p>
    <h2>Assigning Letter Grades</h2>
    <p>The code defines a set of conditions for assigning letter grades based on the student's current score. It then uses these conditions to assign letter grades to each student and stores the result in a new column called 'grade'.</p>
    <h2>Exporting Results</h2>
    <p>The modified grades data is exported to a CSV file. The code also extracts students who are failing "defined as having a current score less than 70" and exports this data to a separate CSV file.</p>
    <h2>Analyzing Results</h2>
    <p>The code groups the grades data by course and grade, then sorts the resulting data by course. It converts the data to a DataFrame and adds a column called 'count' to show the number of students with each grade in each course. The DataFrame is then printed to the console and exported to a CSV file.</p>
    <p>The code also analyzes the number of failing courses for each student and exports a list of students failing 2 or more courses to a CSV file.</p>
  </body>
</html>
