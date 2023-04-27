import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
import random
import userpage


# create the Lab Technician registration form
class LTRegistration(tk.Frame):


    def __init__(self, master,user,pswd):
        super().__init__(master)
        self.master = master
        self.user=user
        self.pswd=pswd
        
        #tk.Label(self, text="Donor Registration", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)
        self.master.title("Donor Registration")
        self.frame = ttk.Frame(self.master, padding="30 15 30 15")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.frame.grid(column=2, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        
        self.city_options = {
            "Alabama": ["Auburn", "Birmingham", "Decatur", "Dothan", "Florence", "Gadsden", "Huntsville", "Mobile", "Montgomery", "Tuscaloosa"],
            "Alaska": ["Anchorage", "Fairbanks", "Juneau", "Sitka", "Ketchikan", "Wasilla", "Kenai", "Kodiak", "Bethel", "Palmer"],
            "Arizona" :['Phoenix', 'Tucson', 'Mesa', 'Chandler', 'Glendale', 'Scottsdale', 'Gilbert', 'Tempe', 'Peoria', 'Surprise', 'Yuma', 'Avondale', 'Flagstaff', 'Goodyear', 'Lake Havasu City', 'Buckeye', 'Casa Grande', 'Sierra Vista', 'Maricopa', 'Oro Valley', 'Prescott', 'Bullhead City', 'Prescott Valley', 'Marana', 'Apache Junction', 'Kingman', 'Queen Creek', 'El Mirage', 'San Luis', 'Sahuarita', 'Fountain Hills', 'Nogales', 'Eloy', 'Somerton', 'Douglas', 'Payson', 'Coolidge', 'Cottonwood', 'Chino Valley', 'Show Low', 'Sedona', 'Winslow', 'Safford', 'Camp Verde', 'Globe', 'Page', 'Wickenburg', 'Holbrook', 'Thatcher', 'Colorado City', 'Bisbee', 'Taylor', 'Guadalupe', 'Snowflake', 'Clifton', 'Dewey-Humboldt', 'Wellton', 'St. Johns', 'Carefree', 'Willcox', 'Williams', 'Parker', 'Superior', 'Patagonia', 'Springerville', 'Kearny', 'Huachuca City', 'Miami', 'Hayden', 'Tombstone', 'Claypool', 'Jerome', 'Fredonia', 'Oatman', 'Pima', 'Star Valley', 'Mammoth', 'Tusayan', 'Quartzsite', 'Duncan', 'Gila Bend', 'Patagonia Lake', 'Winkelman', 'Young', 'Fredonia (Navajo Reservation)', 'Yarnell', 'Cordes Lakes', 'Pinetop-Lakeside', 'Kachina Village', 'Pinetop Country Club', 'New Kingman-Butler', 'Munds Park', 'Gu Oidak', 'Cibola', 'Bouse', 'Grand Canyon Village', 'Ajo', 'Seligman', 'Ali Chukson', 'Top-of-the-World', 'Houck', 'Red Rock', 'Picture Rocks', 'Mesa del Caballo', 'Sacate Village', 'Greasewood', 'Oro Valley CDP (Pima County)', 'Shongopovi', 'Yucca', 'Tubac', 'Anthem', 'Oljato-Monument Valley', 'Tsaile', 'Three Points', 'Ak Chin', 'Pirtleville', 'Swift Trail Junction', 'Sunizona', 'Rock Point', 'Arivaca Junction', 'Sweet Water Village'],
            "Arkansas":
              ["Little Rock", "Fort Smith", "Fayetteville", "Springdale", "Jonesboro", "North Little Rock", "Conway", "Rogers", "Bentonville", "Pine Bluff"],
            "California":
              ["Los Angeles", "San Diego", "San Jose", "San Francisco", "Fresno", "Sacramento", "Long Beach", "Oakland", "Bakersfield", "Anaheim"],
            "Colorado":
              ["Denver", "Colorado Springs", "Aurora", "Fort Collins", "Lakewood", "Thornton", "Arvada", "Westminster", "Pueblo", "Centennial"],
            "Connecticut":
              ["Bridgeport", "New Haven", "Hartford", "Stamford", "Waterbury", "Norwalk", "Danbury", "New Britain", "Bristol", "Meriden"],
            "Delaware":
              ["Wilmington", "Dover", "Newark", "Middletown", "Smyrna", "Milford", "Seaford", "Georgetown", "Elsmere", "New Castle"],
            "Florida":
              ["Jacksonville", "Miami", "Tampa", "Orlando", "St. Petersburg", "Hialeah", "Tallahassee", "Fort Lauderdale", "Port St. Lucie", "Cape Coral"],
            "Georgia":
              ["Atlanta", "Columbus", "Augusta", "Macon", "Savannah", "Athens", "Sandy Springs", "Roswell", "Albany", "Johns Creek"],
            "Hawaii":
              ["Honolulu", "Hilo", "Kailua", "Kaneohe", "Waipahu", "Pearl City", "Waimalu", "Mililani", "Kahului", "Kihei"],
            "Idaho":
              ["Boise", "Nampa", "Meridian", "Idaho Falls", "Pocatello", "Caldwell", "Coeur d'Alene", "Twin Falls", "Lewiston", "Moscow"],
            "Illinois":
              ["Chicago", "Aurora", "Rockford", "Joliet", "Naperville", "Springfield", "Peoria", "Elgin", "Waukegan", "Cicero"],
            "Indiana":
              ["Anderson", "Bloomington", "Carmel", "Elkhart", "Evansville", "Fishers", "Fort Wayne", "Gary", "Goshen", "Greenfield", "Greenwood", "Hammond", "Hobart", "Indianapolis", "Jeffersonville", "Kokomo", "LaPorte", "Lafayette", "Lawrence", "Logansport", "Marion", "Michigan City", "Mishawaka", "Muncie", "Noblesville", "Plainfield", "Plymouth", "Richmond", "Seymour", "Shelbyville", "South Bend", "Terre Haute", "Valparaiso", "West Lafayette"],
            "Iowa":
              ["Ames", "Ankeny", "Bettendorf", "Burlington", "Cedar Falls", "Cedar Rapids", "Clinton", "Council Bluffs", "Davenport", "Des Moines", "Dubuque", "Fort Dodge", "Indianola", "Iowa City", "Marion", "Marshalltown", "Mason City", "Muscatine", "Newton", "North Liberty", "Oskaloosa", "Ottumwa", "Sioux City", "Urbandale", "Waterloo", "Waukee", "Waverly", "West Des Moines"],
            "Kansas":
              ["Emporia", "Garden City", "Hays", "Hutchinson", "Junction City", "Kansas City", "Lawrence", "Leavenworth", "Leawood", "Lenexa", "Manhattan", "Newton", "Olathe", "Overland Park", "Pittsburg", "Prairie Village", "Salina", "Shawnee", "Topeka", "Wichita"],
            "Kentucky":
              ["Ashland", "Bowling Green", "Covington", "Danville", "Elizabethtown", "Florence", "Frankfort", "Georgetown", "Henderson", "Hopkinsville", "Lexington", "Louisville", "Madisonville", "Mayfield", "Murray", "Newport", "Nicholasville", "Owensboro", "Paducah", "Radcliff", "Richmond", "Shelbyville", "Shepherdsville", "Somerset", "Winchester"],
            "Louisiana":
              ["Alexandria", "Baton Rouge", "Bossier City", "Central", "Hammond", "Houma", "Kenner", "Lafayette", "Lake Charles", "Mandeville", "Monroe", "Natchitoches", "New Iberia", "New Orleans", "Opelousas", "Pineville", "Ruston", "Shreveport", "Slidell", "Sulphur", "Thibodaux"],
             "Maine":
              ["Auburn", "Augusta", "Bangor", "Biddeford", "Brunswick", "Ellsworth", "Gardiner", "Hallowell", "Lewiston", "Old Orchard Beach", "Old Town", "Portland", "Presque Isle", "Rockland", "Saco", "South Portland", "Waterville", "Westbrook", "Windham", "Yarmouth"],
            "Maryland":
              ["Annapolis", "Baltimore", "Bethesda", "Bowie", "College Park", "Cumberland", "Easton", "Frederick", "Gaithersburg", "Greenbelt", "Hagerstown", "Laurel", "Rockville", "Salisbury", "Takoma Park", "Westminster"],
            "Massachusetts":
              ["Amherst", "Attleboro", "Barnstable", "Boston", "Brockton", "Cambridge", "Chicopee", "Fall River", "Fitchburg", "Framingham", "Haverhill", "Lawrence", "Leominster", "Lowell", "Lynn", "Malden", "Marlborough", "Medford", "Methuen", "New Bedford", "Newton", "Northampton", "Peabody", "Pittsfield", "Quincy", "Revere", "Salem", "Somerville", "Springfield", "Taunton", "Waltham", "Watertown", "Westfield", "Weymouth", "Woburn", "Worcester"],
            "Michigan":
              ["Ann Arbor", "Battle Creek", "Bay City", "Birmingham", "Bloomfield Hills", "Cadillac", "Charlevoix", "Dearborn", "Detroit", "East Lansing", "Flint", "Grand Haven", "Grand Rapids", "Hancock", "Holland", "Houghton", "Interlochen", "Iron Mountain", "Ironwood", "Ishpeming", "Jackson", "Kalamazoo", "Lansing", "Livonia", "Ludington", "Mackinac Island", "Marquette", "Menominee", "Midland", "Monroe", "Mount Clemens", "Mount Pleasant", "Muskegon", "Niles", "Petoskey", "Pontiac", "Port Huron", "Royal Oak", "Saginaw", "Saint Ignace", "Saint Joseph", "Sault Sainte Marie", "Traverse City", "Troy", "Warren", "Wyandotte", "Ypsilanti"],
            "Minnesota":
              ["Albert Lea", "Alexandria", "Austin", "Bemidji", "Brainerd", "Crookston", "Duluth", "Ely", "Faribault", "Fergus Falls", "Hastings", "Hibbing", "International Falls", "Little Falls", "Mankato", "Minneapolis", "Moorhead", "New Ulm", "Northfield", "Owatonna", "Pipestone", "Red Wing", "Rochester", "Saint Cloud", "Saint Paul", "Sauk Centre", "South Saint Paul", "Stillwater", "Virginia", "Willmar", "Winona"],
            "Mississippi":
              ["Bay Saint Louis", "Biloxi", "Canton", "Clarksdale", "Columbus", "Greenville", "Greenwood", "Gulfport", "Hattiesburg", "Hernando", "Holly Springs", "Jackson", "Laurel", "Meridian", "Natchez", "Ocean Springs", "Oxford", "Pascagoula", "Philadelphia", "Ridgeland", "Southaven", "Starkville", "Tupelo", "Vicksburg"],
        
            "Missouri":
              ["Branson", "Cape Girardeau", "Columbia", "Independence", "Jefferson City", "Joplin", "Kansas City", "Kirksville", "Lee's Summit", "O'Fallon", "Rolla", "Sedalia", "Springfield", "St. Charles", "St. Joseph", "St. Louis"],
            "Montana":
              ["Billings", "Bozeman", "Butte", "Great Falls", "Havre", "Helena", "Kalispell", "Miles City", "Missoula"],
            "Nebraska":
              ["Bellevue", "Fremont", "Grand Island", "Hastings", "Kearney", "Lincoln", "Norfolk", "North Platte", "Omaha", "Papillion", "Scottsbluff"],
            "Nevada":
              ["Boulder City", "Carson City", "Elko", "Henderson", "Las Vegas", "Mesquite", "North Las Vegas", "Reno", "Sparks"],
            "New Hampshire":
              ["Berlin", "Claremont", "Concord", "Dover", "Franklin", "Keene", "Laconia", "Lebanon", "Manchester", "Nashua", "Portsmouth", "Rochester"],
            "New Jersey":
              ["Asbury Park", "Atlantic City", "Bayonne", "Camden", "Cape May", "Clifton", "East Orange", "Edison", "Elizabeth", "Hackensack", "Hoboken", "Irvington", "Jersey City", "Lakewood", "Long Beach Island", "Long Branch", "Millville", "Morristown", "New Brunswick", "Newark", "Ocean City", "Passaic", "Paterson", "Perth Amboy", "Plainfield", "Princeton", "Red Bank", "Toms River", "Trenton", "Union City", "Vineland", "West New York"],
            "New Mexico":
              ["Alamogordo", "Albuquerque", "Artesia", "Carlsbad", "Clovis", "Deming", "Farmington", "Gallup", "Grants", "Hobbs", "Las Cruces", "Las Vegas", "Los Alamos", "Portales", "Rio Rancho", "Roswell", "Santa Fe", "Silver City", "Taos"],
            "New York":
             ["Albany", "Auburn", "Binghamton", "Buffalo", "Cohoes", "Elmira", "Glens Falls", "Gloversville", "Hornell", "Hudson", "Johnstown", "Kingston", "Lackawanna", "Little Falls", "Lockport", "Long Beach", "Mechanicville", "Middletown", "Mount Vernon", "New Rochelle", "New York City", "Newburgh", "Niagara Falls", "North Tonawanda", "Ogdensburg", "Olean", "Oneida", "Oneonta", "Oswego", "Peekskill", "Plattsburgh", "Port Jervis", "Poughkeepsie", "Rensselaer", "Rochester", "Rome", "Rye", "Saratoga Springs", "Schenectady", "Sherrill", "Syracuse", "Tonawanda", "Troy", "Utica", "Watertown", "Watervliet", "White Plains", "Yonkers"],
        
       
            "North Carolina":
             ["Albemarle", "Asheboro", "Asheville", "Belmont", "Boone", "Burlington", "Chapel Hill", "Charlotte", "Concord", "Durham", "Eden", "Elizabeth City", "Fayetteville", "Gastonia", "Goldsboro", "Greensboro", "Greenville", "Halifax", "Henderson", "Hickory", "High Point", "Hillsborough", "Jacksonville", "Kannapolis", "Kinston", "Laurinburg", "Lenoir", "Lexington", "Lumberton", "Morganton", "Mount Airy", "New Bern", "Newton", "North Wilkesboro", "Oxford", "Plymouth", "Raeford", "Raleigh", "Reidsville", "Roanoke Rapids", "Rocky Mount", "Salisbury", "Sanford", "Shelby", "Statesville", "Tarboro", "Thomasville", "Washington", "Wilmington", "Wilson", "Winston-Salem"],
        
            "North Dakota":
             ["Bismarck", "Devils Lake", "Dickinson", "Fargo", "Grand Forks", "Jamestown", "Mandan", "Minot", "Rugby", "Valley City", "Wahpeton", "Williston"],
        
            "Ohio":
             ["Akron", "Alliance", "Ashtabula", "Athens", "Barberton", "Bedford", "Bellefontaine", "Bowling Green", "Bucyrus", "Cadiz", "Cambridge", "Canton", "Celina", "Chillicothe", "Cincinnati", "Cleveland", "Columbus", "Conneaut", "Coshocton", "Cuyahoga Falls", "Dayton", "Defiance", "Delaware", "East Cleveland", "East Liverpool", "Elyria", "Euclid", "Findlay", "Gallipolis", "Greenville", "Hamilton", "Kent", "Kenton", "Kettering", "Lakewood", "Lancaster", "Lima", "Lorain", "Mansfield", "Marietta", "Marion", "Martins Ferry", "Massillon", "Medina", "Mentor", "Middletown", "Milan", "Mount Vernon", "Napoleon", "New Philadelphia", "Newark", "Niles", "North College Hill", "Norwalk", "Norwood", "Oberlin", "Painesville", "Parma", "Piqua", "Portsmouth", "Ravenna", "Reading", "Saint Clairsville", "Sandusky", "Shaker Heights", "Sidney", "Springfield", "Steubenville", "Tiffin", "Toledo", "Troy", "Uhrichsville", "Upper Arlington", "Upper Sandusky", "Urbana", "Van Wert", "Vermilion", "Wapakoneta", "Warren", "Washington Court House", "Wauseon", "Waverly", "Westerville", "Wheeling", "Whitehall", "Willard", "Willoughby", "Wilmington", "Wooster", "Worthington", "Xenia", "Youngstown", "Zanesville"],
        
            "Rhode Island":
              ["Central Falls", "Cranston", "East Providence", "Newport", "Pawtucket", "Providence", "Warwick", "Westerly", "Woonsocket"],
            "South Carolina":
              ["Abbeville", "Aiken", "Anderson", "Beaufort", "Camden", "Charleston", "Columbia", "Darlington", "Florence", "Gaffney", "Georgetown", "Greenville", "Greenwood", "Hartsville", "Lancaster", "Mount Pleasant", "Myrtle Beach", "Newberry", "North Augusta", "Orangeburg", "Rock Hill", "Spartanburg", "Sumter", "Union", "Walterboro"],
            "South Dakota":
              ["Aberdeen", "Belle Fourche", "Brookings", "Canton", "Custer", "De Smet", "Deadwood", "Hot Springs", "Huron", "Lead", "Madison", "Milbank", "Mitchell", "Mobridge", "Pierre", "Rapid City", "Sioux Falls", "Spearfish", "Sturgis", "Vermillion", "Watertown", "Yankton"],
            "Tennessee":
              ["Alcoa", "Athens", "Chattanooga", "Clarksville", "Cleveland", "Columbia", "Cookeville", "Dayton", "Elizabethton", "Fayetteville", "Franklin", "Gallatin", "Gatlinburg", "Greeneville", "Jackson", "Johnson City", "Jonesborough", "Kingsport", "Knoxville", "La Follette", "Lebanon", "Maryville", "Memphis", "Morristown", "Murfreesboro", "Nashville", "Norris", "Oak Ridge", "Shelbyville", "Tullahoma"],
            "Texas":
              ["Abilene", "Alpine", "Amarillo", "Arlington", "Austin", "Baytown", "Beaumont", "Big Spring", "Borger", "Brownsville", "Bryan", "Canyon", "Cleburne", "College Station", "Corpus Christi", "Crystal City", "Dallas", "Del Rio", "Denton", "Eagle Pass", "Edinburg", "El Paso", "Fort Worth", "Freeport", "Galveston", "Garland", "Goliad", "Greenville", "Harlingen", "Houston", "Huntsville", "Irving", "Johnson City", "Kilgore", "Killeen", "Kingsville", "Laredo", "Longview", "Lubbock", "Lufkin", "Marshall", "McAllen", "McKinney", "Mesquite", "Midland", "Mount Pleasant", "Nacogdoches", "New Braunfels", "Odessa", "Orange", "Pampa", "Paris", "Pasadena", "Pecos", "Pharr", "Plainview", "Plano", "Port Arthur", "Port Lavaca", "Richardson", "San Angelo", "San Antonio", "San Felipe", "San Marcos", "Sherman", "Sweetwater", "Temple", "Texarkana", "Texas City", "Tyler", "Uvalde", "Victoria", "Waco", "Weatherford", "Weslaco", "Wichita Falls", "Ysleta"],
            "Utah":
              ["Alta", "American Fork", "Bountiful", "Brigham City", "Cedar City", "Clearfield", "Delta", "Fillmore", "Green River", "Heber City", "Kanab", "Layton", "Lehi", "Logan", "Manti", "Moab", "Monticello", "Murray", "Nephi", "Ogden", "Orderville", "Orem", "Panguitch", "Park City", "Payson", "Price", "Provo", "Richfield", "Roosevelt", "Salt Lake City", "Spanish Fork", "Springville", "St. George", "Summit", "Tooele", "Vernal"],
            "Vermont":
              ["Barre", "Bellows Falls", "Bennington", "Brattleboro", "Burlington", "Essex", "Manchester", "Middlebury", "Montpelier", "Newport", "Poultney", "Rutland", "Saint Albans", "Saint Johnsbury", "Sharon", "Winooski", "Woodstock"],

       
            "Virginia":
              ["Abingdon", "Alexandria", "Bristol", "Charlottesville", "Chesapeake", "Danville", "Fairfax", "Falls Church", "Fredericksburg", "Hampton", "Hanover", "Hopewell", "Lexington", "Lynchburg", "Manassas", "Martinsville", "New Market", "Newport News", "Norfolk", "Petersburg", "Portsmouth", "Reston", "Richmond", "Roanoke", "Staunton", "Suffolk", "Virginia Beach", "Waynesboro", "Williamsburg", "Winchester"],
            "Washington":
              ["Aberdeen", "Anacortes", "Auburn", "Bellevue", "Bellingham", "Bremerton", "Centralia", "Coulee Dam", "Coupeville", "Ellensburg", "Ephrata", "Everett", "Hoquiam", "Kelso", "Kennewick", "Longview", "Moses Lake", "Oak Harbor", "Olympia", "Pasco", "Point Roberts", "Port Angeles", "Pullman", "Puyallup", "Redmond", "Renton", "Richland", "Seattle", "Spokane", "Tacoma", "Vancouver", "Walla Walla", "Wenatchee", "Yakima"],
            "West Virginia":
              ["Beckley", "Bluefield", "Charles Town", "Charleston", "Clarksburg", "Elkins", "Fairmont", "Grafton", "Harpers Ferry", "Hillsboro", "Hinton", "Huntington", "Keyser", "Lewisburg", "Logan", "Martinsburg", "Morgantown", "Moundsville", "New Martinsville", "Parkersburg", "Philippi", "Point Pleasant", "Princeton", "Romney", "Shepherdstown", "South Charleston", "Summersville", "Weirton", "Welch", "Wellsburg", "Weston", "Wheeling"],
            "Wisconsin":
              ["Appleton", "Ashland", "Baraboo", "Belmont", "Beloit", "Eau Claire", "Fond du Lac", "Green Bay", "Hayward", "Janesville", "Kenosha", "La Crosse", "Lake Geneva", "Madison", "Manitowoc", "Marinette", "Menasha", "Milwaukee", "Neenah", "New Glarus", "Oconto", "Oshkosh", "Peshtigo", "Portage", "Prairie du Chien", "Racine", "Rhinelander", "Ripon", "Sheboygan", "Spring Green", "Stevens Point", "Sturgeon Bay", "Superior", "Waukesha", "Wausau", "Wauwatosa", "West Allis", "West Bend"],

            "Wyoming":
              ["Buffalo", "Casper", "Cheyenne", "Cody", "Douglas", "Evanston", "Gillette", "Green River", "Jackson", "Lander", "Laramie", "Newcastle", "Powell", "Rawlins", "Riverton", "Rock Springs", "Sheridan", "Ten Sleep", "Thermopolis", "Torrington", "Wheatland", "Worland"]
        
        }


        self.canvas = tk.Canvas(self.frame, width=600,height=800)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        

        scrollable_frame = ttk.Frame(self.canvas)
        #scrollable_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        scrollbar.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.E), padx=(0, 5), pady=5, rowspan=2)
        
        #canvas.config(scrollregion=canvas.bbox("all")) 
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")


        scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.yview_moveto(0.0)
        # add a frame to the canvas
        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # create the form fields
        title = ttk.Label(self.frame, text=30*" "+"Registration Form", font=("bold", 18))
        title.grid(column=0, row=0, columnspan=2, pady=10)

        label_fname = ttk.Label(self.frame, text="First Name:")
        label_fname.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
        self.entry_fname = ttk.Entry(self.frame)
        self.entry_fname.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)

        label_lname = ttk.Label(self.frame, text="Last Name:")
        label_lname.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
        self.entry_lname = ttk.Entry(self.frame)
        self.entry_lname.grid(column=1, row=2, padx=10, pady=5, sticky=tk.W)

        label_username = ttk.Label(self.frame, text="Username:")
        label_username.grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
        self.entry_username = ttk.Entry(self.frame)
        self.entry_username.grid(column=1, row=3, padx=10, pady=5, sticky=tk.W)

        label_password = ttk.Label(self.frame, text="Password:")
        label_password.grid(column=0, row=4, padx=10, pady=5, sticky=tk.W)
        self.entry_password = ttk.Entry(self.frame, show="*")
        self.entry_password.grid(column=1, row=4, padx=10, pady=5, sticky=tk.W)


        label_confirm_password = ttk.Label(self.frame, text="Confirm Password:")
        label_confirm_password.grid(column=0, row=5, padx=10, pady=5, sticky=tk.W)
        self.entry_confirm_password = ttk.Entry(self.frame, show="*")
        self.entry_confirm_password.grid(column=1, row=5, padx=10, pady=5, sticky=tk.W)

    
        

        label_state = ttk.Label(self.frame, text="State:")
        label_state.grid(column=0, row=7, padx=10, pady=5, sticky=tk.W)
        
        self.combobox_state = ttk.Combobox(self.frame, values=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"])
        self.combobox_state.grid(column=1, row=7, padx=10, pady=5, sticky=tk.W)
        self.combobox_state.bind("<<ComboboxSelected>>", self.set_city_options)
        
        label_city = ttk.Label(self.frame, text="City:")
        label_city.grid(column=0, row=8, padx=10, pady=5, sticky=tk.W)
        
        self.combobox_city = ttk.Combobox(self.frame, values=["Select a state first"])
        self.combobox_city.grid(column=1, row=8, padx=10, pady=5, sticky=tk.W)

        # label_city = ttk.Label(self.frame, text="City:")
        # label_city.grid(column=0, row=11, padx=10, pady=5, sticky=tk.W)
        # self.combobox_city = ttk.Combobox(self.frame, values=["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose"])
        # self.combobox_city.grid(column=1, row=11, padx=10, pady=5, sticky=tk.W)

        # label_state = ttk.Label(self.frame, text="State:")
        # label_state.grid(column=0, row=12, padx=10, pady=5, sticky=tk.W)
        # self.combobox_state = ttk.Combobox(self.frame, values=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"])
        # self.combobox_state.grid(column=1, row=12, padx=10, pady=5, sticky=tk.W)
        
        label_street = ttk.Label(self.frame, text="Street:")
        label_street.grid(column=0, row=9, padx=10, pady=5, sticky=tk.W)
        self.entry_street = ttk.Entry(self.frame)
        self.entry_street.grid(column=1, row=9, padx=10, pady=5, sticky=tk.W)

        label_zip_code = ttk.Label(self.frame, text="Zip Code:")
        label_zip_code.grid(column=0, row=10, padx=10, pady=5, sticky=tk.W)
        self.entry_zip_code = ttk.Entry(self.frame)
        self.entry_zip_code.grid(column=1, row=10, padx=10, pady=5, sticky=tk.W)
    
        
        label_phone = ttk.Label(self.frame, text="Phone:")
        label_phone.grid(column=0, row=11, padx=11, pady=5, sticky=tk.W)
        self.entry_phone = ttk.Entry(self.frame)
        self.entry_phone.grid(column=1, row=11, padx=11, pady=5, sticky=tk.W)
    
        label_email = ttk.Label(self.frame, text="Email:")
        label_email.grid(column=0, row=12, padx=12, pady=5, sticky=tk.W)
        self.entry_email = ttk.Entry(self.frame)
        self.entry_email.grid(column=1, row=12, padx=12, pady=5, sticky=tk.W)
       

        # create the submit button
        self.button_submit = ttk.Button(self.frame, text="Register", command=self.submit)
        self.button_submit.grid(column=1, row=18, pady=10)
        
        self.button_back = ttk.Button(self.frame, text="Back", command=self.back)
        self.button_back.grid(column=1, row=19, pady=10)
        
    def set_city_options(self, event=None):
        self.combobox_city.set("") # set city to blank
        self.combobox_city['values'] = [] # clear previous values
        state = self.combobox_state.get()
        if state in self.city_options:
            city_options = self.city_options[state]
        else:
            city_options = ["Select a state first"]
        self.combobox_city['values'] = city_options            
    
    def submit(self):
        # get the form data
        lab_technician_fname = self.entry_fname.get()
        lab_technician_lname = self.entry_lname.get()
        lab_technician_username = self.entry_username.get()
        lab_technician_password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()
        street = self.entry_street.get()
        city = self.combobox_city.get()
        state = self.combobox_state.get()
        zip_code = self.entry_zip_code.get()
        lab_technician_phone = self.entry_phone.get()
        lab_technician_email = self.entry_email.get()

        
        mydb = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT bloodbank_name FROM bloodbank")

        # fetch all the results and store them in a list
        bloodbank_names = mycursor.fetchall()
        
        # randomly select a blood bank name from the list
        bloodbank_name = random.choice(bloodbank_names)[0]


        # check if the password and confirm password match
        if lab_technician_password != confirm_password:
            messagebox.showerror("Error", "Password and confirm password do not match!")
            return

        # check if the username and password are not already in the database
        try:
            mycursor.execute("select check_registration(%s)", (lab_technician_username,))
            result = mycursor.fetchone()
            if result[0]==1:
                messagebox.showerror("Error", "Username already exists!")
                return
    
            # insert the data into the database

            sql = "INSERT INTO lab_technician (lab_technician_fname, lab_technician_lname, lab_technician_username, lab_technician_password , street, city, state, zip_code, lab_technician_phone, lab_technician_email, bloodbank_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
           
        
            mycursor.execute(sql, (lab_technician_fname, lab_technician_lname, lab_technician_username, lab_technician_password , street, city, state, zip_code, lab_technician_phone, lab_technician_email, bloodbank_name))
            mydb.commit()
            messagebox.showinfo("Success", "You are registered successfully!")
            self.master.destroy()
            userpage.MyApp(self.user,self.pswd).deiconify()
            #self.master.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
        finally:
            mycursor.close()
                
                
                
                
    def back(self):
        
       self.master.destroy()
       userpage.MyApp(self.user,self.pswd).deiconify()
           
                





