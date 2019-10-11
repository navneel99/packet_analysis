
## Assignment 3 of Computer Networks

<b> The pdf with the problem statement is attached.</b>

### Using csv_parser.py

Import the parser, as you would do for a normal library.

<code> import csv_parser

VAR_NAME=csv_parser.fileReader(CSV_FILE,<i>[SEPARATOR]</i>)
</code>

The default separator is <b>","</b>

#### Attributes of the fileReader

The fileReader object has attributes which help in generating plots and all that is required in the assignment.

<table>
<tr><th>Attribute Name</th><th>Type</th><th>Info</th></tr>
<tr><td>rawdata</td><td>list of list</td><td>The bigger list contains all the rows,while the smaller list has all the columns</td></tr>
<tr><td>tcpdata</td><td>list of list</td><td>Contains only the rows with TCP protocol</td></tr>
<tr><td>ftpdata</td><td>list of list</td><td>Contains only the data with FTP protocol</td></tr>
<tr><td>srciplist</td><td>list</td><td>Contains all the unique source IPs in the CSV</td></tr>
<tr><td>destiplist</td><td>list</td><td>Contains all the unique destination IPs in the CV</td></tr>
<tr><td>serverips</td><td>list</td><td>Contains all the Unique Server IPs in the CSV</td></tr>
<tr><td>clientips</td><td>list</td><td>Contains all the Unique Client IPs in the CSV</td></tr>
<tr><td>tcpflows</td><td>Dictionary,(4-tuple):[Rows of Data]</td><td>Used for maintaining the TCP flows in the document</td></tr>
</table>
<b>Each Row of Data is as follows:</b>
<table>
<tr><th>packet_number</th><th>rel_time(from 0)</th><th>source_ip</th><th>destination_ip</th><th>protocol</th><th>packet_length</th><th>info</th></tr>
</table>

### Methods of the fileReader object

<table>
<tr>
<th>Function Name</th><th>Argument(s)</th><th>Returns</th><th>Description</th>
</tr>
<tr>
<td>generate_duration_flow</td><td>4-tuple</td><td>list</td><td> Generates a list of connection durations.<i>Single Connection results in a list with 1 element</i></td>
</tr>
<tr>
<td>generate_bytes_sent</td><td>4-tuple</td><td>list</td><td> Generates a list of bytes sent over each connection duration.<i>Single Connection results in a list with 1 element</i></td>
</tr>
</table>
