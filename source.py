import time
import webbrowser
import matplotlib.pyplot as plt
import generatePDF

new = 2 # open in a new tab, if possible
def generate_html_report(activities, total_carbon,total_carbonList):
    # Generate the Grapgh for the activities and save it in .png format
    # ***creating Grapgh 1 for Energy used**** #
    labels1=[] # Names of the activites
    valSize1=[] #size of the proportion on the graph
    labels1=['Jan','Feb','March','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
    # for value in total_carbonList:
    #     valSize1.append(value)
    valSize1.extend([5572.416,3262.112,6798.428])
    valSize1.append(total_carbonList[0])
    valSize1.extend([0,0,0,0,0,0,0,0])
    #colors = ['#558e21', '#9BCF53', '#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7']
    # Create a pie chart
    plt.figure(figsize=(9,4),dpi=100)  # Set the size of the figure (optional)
    for i in range(len(labels1)):
        if valSize1[i]>0:
            plt.text(i, valSize1[i] + 1, str(valSize1[i]), ha='center')
    plt.bar(labels1, valSize1, color='#89be4d',width = 0.7)
    plt.xlabel('Months',fontfamily='serif', fontsize=12)
    plt.ylabel('Carbon Emitted',fontfamily='serif', fontsize=12)
    
    # Add a title
    plt.title('Total Carbon Calculated for Energy Used')
    # Save the plot as a PNG image
    plt.savefig('Carbon_pie_chart1.png')
    
    # ***creating Grapgh 2 for Waste Generated**** #
    labels2=[] # Names of the activites
    valSize2=[] #size of the proportion on the graph
    labels2=['Jan','Feb','March','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
    # for value in total_carbonList:
    #     valSize2.append(value)
    valSize2.extend([16738.2,18114.66,11549.428])
    valSize2.append(total_carbonList[1])
    valSize2.extend([0,0,0,0,0,0,0,0])
    #colors = ['#558e21', '#9BCF53', '#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7']
    # Create a pie chart
    plt.figure(figsize=(9,4),dpi=100)  # Set the size of the figure (optional)
    for i in range(len(labels2)):
        if valSize2[i]>0:
            plt.text(i, valSize2[i] + 1, str(valSize2[i]), ha='center')
    plt.bar(labels2, valSize2, color='#a989c5',width = 0.7)
    plt.xlabel('Months',fontfamily='serif', fontsize=12)
    plt.ylabel('Carbon Emitted',fontfamily='serif', fontsize=12)
    
    # Add a title
    plt.title('Total Carbon Calculated for Waste Generated')
    # Save the plot as a PNG image
    plt.savefig('Carbon_pie_chart2.png')
    
    # ***creating Grapgh 3 for Business Travel**** #
    labels3=[] # Names of the activites
    valSize3=[] #size of the proportion on the graph
    labels3=['Jan','Feb','March','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
    
    # valSize3.append(value)
    valSize3.extend([320.23,168.5,421.14])
    valSize3.append(total_carbonList[2])
    valSize3.extend([0,0,0,0,0,0,0,0])
    #colors = ['#558e21', '#9BCF53', '#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7','#5665b7']
    # Create a pie chart
    plt.figure(figsize=(9,4),dpi=100)  # Set the size of the figure (optional)
    for i in range(len(labels3)):
        if valSize3[i]>0:
            plt.text(i, valSize3[i] + 1, str(valSize3[i]), ha='center')
    plt.bar(labels3, valSize3, color='#f2a86f',width = 0.7)
    plt.xlabel('Months',fontfamily='serif', fontsize=12)
    plt.ylabel('Carbon Emitted',fontfamily='serif', fontsize=12)
    
    # Add a title
    plt.title('Total Carbon Calculated for Business Travelled')
    # Save the plot as a PNG image
    plt.savefig('Carbon_pie_chart3.png')

    #**************#
    with open('report_data.txt', 'r') as file:
        info_content = file.read()
    with open('suggestions.txt', 'r') as file:
        sugg_content = file.read()
        
    # Define the HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en" style="font-size:17px">
    <head onload="window.print()">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
         <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.9.2/html2pdf.bundle.js"></script>

        <title>Carbon Footprint Report</title>
        <style>
            html{{
                font-size: 17px;
            }}
            .title {{
            font-size: 60px;
            font-weight:bolder;
            text-align: center;
            padding-left: 350px;
            padding-top: 70px;
            width: 500px;
            }}
            body {{
                font-family: Aptos;
                font-size: 17px;
                border: 3px solid rgb(154, 145, 145);
                padding: 100px;
            }}
            h1 {{
                color: #333;
            }}
            h3{{
                padding-left: 15px;
            }}
            .h2{{
                padding-left:10px
            }}
            p {{
                margin-bottom: 10px;
                padding-left: 30px;
                text-align: justify;
                text-justify: inter-word;
            }}
            
            .icon {{
                width: 100px; /* Adjust the width of the icon */
                height: 100px; /* Adjust the height of the icon */
                background-image: url('Images/BackgroundImage_.png'); /* URL of the icon */
                background-size: cover;
                margin-right: 10px; /* Adjust the spacing between the icon and title */
                padding-top: 0px;
                padding-bottom: 60px;
            }}
            dl {{
                display: grid;
                grid-template-columns: 1fr 1fr; /* Two columns */
                gap: 10px;
            }}
            dt {{
                font-weight: bold;
                margin-bottom: 5px;
            }}
            dd {{
                margin-bottom: 10px;
            }}
            
            
        </style>
    </head>
    <body>
     
        
        <div class="container">
        <div class="icon">
        <div class="title">Carbon Footprint</div>
        </div>
        </div>
        <p> A Carbon Footprint is an impression determined worth or record that makes it conceivable to look at the aggregate sum of
        greenhouse gases that an activity, product, company or country adds to the atmosphere.
        <ul>
        <li>Carbon impressions are typically revealed in lots of outflows (CO2-same) per unit of correlation. Such units can be for instance tons CO2-eq each year,
        per kilogram of protein for consumption, per kilometer travelled, per piece of clothing and so forth. </li>
        <li>An item's carbon impression incorporates the emanations for the whole life cycle. These run from the creation along the production network to its last utilization and removal.</li>
        </ul></p>
        </br>
        <h2>The overall carbon footprint for the year 2024, as of April 2024 is <strong>{total_carbon:.2f} kg CO2</strong></h2>
            </br>
            <h2>Energy Usage Imapct on Carbon Emission :</h2>
            <img src="Carbon_pie_chart1.png" alt="Matplotlib Plot">
            </br>
            <h2>Impact of Waste Generated on Carbon Emission:</h2>
            <img src="Carbon_pie_chart2.png" alt="Matplotlib Plot">
            </br>
            <h2>Impact of Business Travel on Carbon Emission:</h2>
            <img src="Carbon_pie_chart3.png" alt="Matplotlib Plot">
            </br>
            
         <h2> Factors that contribute to Carbon Emissions:</h2>   
        </br>
        <div class="card-container">
        <div class="card" >
        <div class="card-header">
        <h3>Energy Usage</h3>
        </div>
        <div class="card-body">
        <a href="#Energy">
            <img  src="Images/energy.jpg" alt="Energy Used" class="card-img">
            </a>
        </div>
        </div>
         <div class="card" >
         <div class="card-header">
        <h3>Waste Generated</h3>
        </div>
        <div class="card-body">
        <a href="#Waste">
            <img  src="Images/waste.jpg" alt="Waste generated" class="card-img">
        </a>
        </div>
        </div>
         <div class="card" >
         <div class="card-header">
        <h3>Buisness Travelled</h3>
        </div>
        <div class="card-body">
        <a href="#Travel">
            <img  src="Images/businessTravel.jpeg" alt="Business Travel" class="card-img">
        </a>
        </div>
        </div>
        </div>
        
        <div class="wrap">
        {info_content}
        </div>
        <h2>Consider taking actions to reduce your carbon footprint.</h2>
            <div class="wrap">
                {sugg_content}
            </div>
            
            
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open("carbon_footprint_report.html", "w") as html_file:
        html_file.write(html_content)

    #To open the created HTML file on the browser. (Also, we need to mention the absolute path for the url)
    url = "file:///Users/sherinhartman/Documents/GitHub/Carbon_FootprintTool/carbon_footprint_report.html" 
    webbrowser.open(url,new=new)
    time.sleep(2)
    generatePDF.save_html_as_pdf('/Users/sherinhartman/Documents/GitHub/Carbon_FootprintTool/carbon_footprint_report.html','CarbonFootprint_Report')
    
    


def main():
    #Get user input for activities and their corresponding carbon values
    activities = {}
    activities1=[]
    value=[]
    total_carbonList=[]
    
    for activity in ['Energy Used', 'Waste Generated', 
                      'Business Travelled']:
        try:
            if (activity=='Energy Used'):
                value1 = float(input(f"What is your average monthly electricity bill in euros: "))
                value2=float(input(f"What is your average monthly natural gas bill in euros: "))
                value3=float(input(f"What is your average monthly fuel bill for transportation in euros: "))
                total_carbon1=round((value1)*(12)*(0.0005)+(value2)*(12)*(0.0053)+(value3)*(12)*(2.32),3)
                value.extend([value1,value2,value3])
                activities[activity] = value
            elif(activity=='Waste Generated'):
                value4=float(input(f"How much waste do you generate per month in kilograms? : "))
                value5=float(input(f"How much of that waste is recycled or composted(in percentage)? : "))/100
                total_carbon2=round((value4)*(12)*(0.57-value5),3)
                value.extend([value4,value5])
                activities[activity] = value
            elif(activity=='Business Travelled'):
                value6=float(input(f"How many kilometers do your employees travel per year for business purposes? : "))
                value7=float(input(f"What is the average fuel efficiency of the vehicles used for business travel in litres per 100 kilometers : "))
                total_carbon3=round((value6)*(1/value7)*(2.31),3)
                value.extend([value6,value7])
                activities[activity] = value
            else:
                print("No activites mentioned at the moment")
            
        except ValueError:
                print("Error", "Please enter valid numerical values for all activities.")
                return
    #value.extend([value1,value2,value3,value4,value5,value6,value7])
    total_carbonList.extend([total_carbon1,total_carbon2,total_carbon3])
    
    activities1.append(activities)
    # Calculate total carbon footprint
    total_carbon = sum(total_carbonList)
        
        
        
    # Generate HTML report and display it
    generate_html_report(activities, total_carbon,total_carbonList)
    
    # def generatePdf():
    #     generatePDF.save_html_as_pdf('/Users/sherinhartman/Documents/GitHub/Carbon_FootprintTool/carbon_footprint_report.html','CarbonFootprint_Report.pdf')

    
if __name__ == "__main__":
    main()
    