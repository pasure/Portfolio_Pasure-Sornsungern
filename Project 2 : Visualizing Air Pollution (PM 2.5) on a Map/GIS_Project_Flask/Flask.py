from sqlalchemy import create_engine
import urllib
import pandas as pd
from pandasql import sqldf
import datetime as dt
from flask import Flask, render_template, request, send_file ,Response
from io import BytesIO

app = Flask(__name__)

# Settings
user = ''
password = ''
host = 'gis.cokgqfecgwug.us-east-1.rds.amazonaws.com,1433'
db = 'Project_PM25'
db5B = '5B'
SchemaName = 'dbo'
TableName = 'AirPollutionPM25'
# SourceFile = "D:\\SPATIAL DATABASES AND GIS APPLICATIONS\\Project_GIS\\WHO_2008_2017.xlsx"
# SourceFile5B = "D:\\SPATIAL DATABASES AND GIS APPLICATIONS\\Project_GIS\\5B.xlsx"

# Configure the Connection
Engine = create_engine(f'mssql://{user}:{password}@{host}/{db}?driver=SQL+Server')
Engine5B = create_engine(f'mssql://{user}:{password}@{host}/{db5B}?driver=SQL+Server')


# Load the sheet into a DataFrame
# df = pd.read_excel(SourceFile, sheet_name = 'WHO_AirQuality_Database_2018', header = 0)

# Clear the Data in Target Table
sql = 'Truncate Table AirPollutionPM25'
sqlUpdate = "UPDATE AirPollutionPM25 SET Geom = geometry:: STGeomFromText('POINT('+convert(varchar(20),longitude)+' '+convert(varchar(20),latitude)+')',4326)"

# with Engine.begin() as conn:
#     conn.execute(sql)
    
# # Load the Data in DataFrame into Table
# df.to_sql(TableName, con=Engine, schema=SchemaName, if_exists='append', index=False)

# with Engine.begin() as conn:   
#     conn.execute(sqlUpdate) 

print(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' | Data Imported Successfully')

# Query Top 5 Results
qurey5 = ("select TOP 5 country, city, Year,pm25, latitude,	longitude, population, wbinc16_text, Region, conc_pm25,	color_pm25,	Geom.STAsText() AS Geom from AirPollutionPM25 WHERE city='Espoo'")
dfTop5 = pd.read_sql(qurey5,Engine)

qYears = ("select Year from AirPollutionPM25 Group By Year ORDER BY Year DESC")
qColor = ("select color_pm25 from AirPollutionPM25 Group By color_pm25 ORDER BY color_pm25 ASC")    
dfYears = pd.read_sql(qYears,Engine)
dfColor = pd.read_sql(qColor,Engine) 

@app.route('/')
def index():
    return render_template("index.html",data=dfTop5.to_html(classes=["table"]))

@app.route('/toExcel1.html', methods=['POST','GET'])
def toExcel1():
    if request.method == 'POST':        
        # Query
        excel4AQuery = ("SELECT Year, country , city , pm25 FROM AirPollutionPM25 WHERE pm25 > 50 AND Year = '2015' ORDER BY Year")
        result4A = pd.read_sql(excel4AQuery,Engine) 

        # Export Excel
        output = BytesIO()
        writer = pd.ExcelWriter(output)
        result4A.to_excel(writer,index=False)
        writer.close()
        output.seek(0)
        
        return send_file(output, attachment_filename="2015_PM25_Greater Than 50.xlsx", as_attachment=True)     
    else:
        return render_template("toExcel1.html")

@app.route('/toExcel2.html', methods=['POST','GET'])
def toExcel2(): 
        if request.method == 'POST':        
            # Query
            excel4BQuery = ("SELECT country , AVG(pm25) As AveragePM25 FROM AirPollutionPM25 GROUP BY country ORDER BY AVG(pm25) DESC")
            result4B = pd.read_sql(excel4BQuery,Engine) 

            # Export Excel
            output = BytesIO()
            writer = pd.ExcelWriter(output)
            result4B.to_excel(writer,index=False)
            writer.close()
            output.seek(0)
            
            return send_file(output, attachment_filename="AllCountries_AVG(PM2.5).xlsx", as_attachment=True)            
        else:   
            return render_template("toExcel2.html")
    
@app.route('/toExcel3.html', methods=['POST','GET'])
def toExcel3():    
        qCountries = ("select country from AirPollutionPM25 Group By country")
        dfCountries = pd.read_sql(qCountries,Engine)        
        
        if request.method == 'POST':
            countrySelect = request.form.get('countrySelect')
            # Query
            excel4CQuery = ("SELECT country ,city, pm25 ,Year FROM AirPollutionPM25 WHERE country = '"+str(countrySelect)+"' ORDER BY Year DESC")
            result4C = pd.read_sql(excel4CQuery,Engine) 

            # Export Excel
            output = BytesIO()
            writer = pd.ExcelWriter(output)
            result4C.to_excel(writer,index=False)
            writer.close()
            output.seek(0)
            
            return send_file(output, attachment_filename=""+str(countrySelect)+"_PM25.xlsx", as_attachment=True) 
            
        else:
            return render_template("toExcel3.html",country=list(dfCountries.to_records()))
           

@app.route('/toExcel4.html', methods=['POST','GET'])
def toExcel4():         
        if request.method == 'POST':        
            YearsSelect = request.form.get('YearsSelect')
            ColorsSelect = request.form.get('ColorSelect')
            # Query
            excel4DQuery = ("SELECT SUM(population) As  SumofPopulation FROM AirPollutionPM25 WHERE Year = '"+str(YearsSelect)+"' AND color_pm25 = '"+str(ColorsSelect)+"'")
            result4D = pd.read_sql(excel4DQuery,Engine) 

            # Export Excel
            output = BytesIO()
            writer = pd.ExcelWriter(output)
            result4D.to_excel(writer,index=False)
            writer.close()
            output.seek(0)
            
            return send_file(output, attachment_filename="""SUM(population)_"""+str(YearsSelect)+"_"+str(ColorsSelect)+".xlsx", as_attachment=True)           
        else:
            return render_template("toExcel4.html",Years=list(dfYears.to_records()),Color=list(dfColor.to_records()))



@app.route('/visualization1.html', methods=['POST','GET'])
def visualization1():       
    if request.method == 'POST': 
        YearsSelect = request.form.get('YearsSelect')
        excel5AQuery = ("SELECT country, city , longitude , latitude FROM AirPollutionPM25 WHERE Year = '"+str(YearsSelect)+"'")
        result5A = pd.read_sql(excel5AQuery,Engine)
        return render_template("visualization1.html",Years=list(dfYears.to_records()),lonLatall=list(result5A.to_records()))
        
    return render_template("visualization1.html",Years=list(dfYears.to_records()))

@app.route('/visualization2.html', methods=['POST','GET'])
def visualization2():
    # result5B = pd.read_excel(SourceFile5B, sheet_name = 'Query', header = 0)
    excel5BQuery = ("SELECT * FROM Distance ")
    result5B = pd.read_sql(excel5BQuery,Engine5B)
    if request.method == 'POST':
        return render_template("visualization2.html",top50=list(result5B.to_records()))
    
    return render_template("visualization2.html")

@app.route('/visualization3.html', methods=['POST','GET'])
def visualization3():
    if request.method == 'POST':
        excel5CQuery = ("SELECT DISTINCT country, city, longitude, latitude FROM AirPollutionPM25 WHERE country IN ('Myanmar', 'Malaysia')")
        result5C = pd.read_sql(excel5CQuery,Engine)
        return render_template("visualization3.html",neighbor=list(result5C.to_records()))

    return render_template("visualization3.html")

@app.route('/visualization4.html', methods=['POST','GET'])
def visualization4():
    if request.method == 'POST':
        excel5DQuery = ("SELECT country, city, longitude, latitude FROM AirPollutionPM25 WHERE country = 'Thailand'")
        result5D = pd.read_sql(excel5DQuery,Engine)
        return render_template("visualization4.html",mbr=list(result5D.to_records()))
    
    return render_template("visualization4.html")

@app.route('/visualization5.html', methods=['POST','GET'])
def visualization5():
    if request.method == 'POST':
        excel5EQuery = ("SELECT country, city, longitude, latitude FROM AirPollutionPM25 WHERE country IN (SELECT TOP 1 country FROM AirPollutionPM25 WHERE Year = '2011' GROUP BY country ORDER BY COUNT(city) DESC) AND Year = '2011'")
        result5E = pd.read_sql(excel5EQuery,Engine)
        return render_template("visualization5.html",top=list(result5E.to_records()))

    return render_template("visualization5.html")

@app.route('/visualization6.html', methods=['POST','GET'])
def visualization6():
    if request.method == 'POST':
        YearsSelect = request.form.get('YearsSelect')
        excel5FQuery = ("SELECT country, city, longitude , latitude FROM AirPollutionPM25 WHERE wbinc16_text = 'Low income' AND Year = '"+str(YearsSelect)+"'")
        result5F = pd.read_sql(excel5FQuery,Engine)
        return render_template("visualization6.html",Years=list(dfYears.to_records()),lowIncome=list(result5F.to_records()))
    
    return render_template("visualization6.html",Years=list(dfYears.to_records()))


if __name__ == "__main__":
    app.run(debug=True,threaded=True)