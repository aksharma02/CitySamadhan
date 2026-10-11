from datetime import datetime, timedelta
import random
from app import app, db, User, Complaint

SEED_DATA = [
    {
        "author": "Aarav Sharma",
        "email": "aarav.sharma@example.com",
        "phone": "9811223344",
        "state": "Delhi",
        "city": "New Delhi",
        "department": "Electricity Board",
        "title": "Exposed high-voltage transformer cable hanging loose near pedestrian path",
        "description": "An exposed insulated wire from the roadside distribution box has detached and is dangling just 4 feet off the pavement right outside the Metro Gate. High risk of electrocution during night and rain.",
        "location": "Lajpat Nagar IV, Central Market Rd",
        "status": "In Process",
        "upvotes": 18,
        "days_ago": 2
    },
    {
        "author": "Priya Nair",
        "email": "priya.nair@example.com",
        "phone": "9822334455",
        "state": "Karnataka",
        "city": "Bangalore",
        "department": "Public Works Department",
        "title": "Deep trench left unfilled after fiber optical cable digging",
        "description": "Telecom contractor excavated a 3-foot trench along 100 Feet Road two weeks ago and left without backfilling. Two scooter riders suffered minor injuries yesterday.",
        "location": "Indiranagar 100 Feet Road, Near 12th Main",
        "status": "Reported",
        "upvotes": 12,
        "days_ago": 1
    },
    {
        "author": "Rajesh Patel",
        "email": "rajesh.patel@example.com",
        "phone": "9833445566",
        "state": "Gujarat",
        "city": "Ahmedabad",
        "department": "Water Supply Authority",
        "title": "Major potable water pipeline fracture flooding residential lane",
        "description": "Treated drinking water is gushing out under high pressure from an underground pipeline fracture since 6 AM. Millions of liters of clean water getting wasted while road is submerged.",
        "location": "Vastrapur Lake Road, Opp Alpha One Mall",
        "status": "In Process",
        "upvotes": 22,
        "days_ago": 3
    },
    {
        "author": "Sneha Mukherjee",
        "email": "sneha.mukherjee@example.com",
        "phone": "9844556677",
        "state": "West Bengal",
        "city": "Kolkata",
        "department": "Municipal Waste Management",
        "title": "Overflowing waste vat spilling onto tram tracks and roadway",
        "description": "Garbage has not been lifted for 4 days. Vegetable and fish waste is decomposing in the open, causing unbearable stench and attracting stray animals blocking traffic.",
        "location": "Gariahat Crossing, Near Triangular Park",
        "status": "Resolved",
        "upvotes": 15,
        "days_ago": 6
    },
    {
        "author": "Vikram Rathore",
        "email": "vikram.rathore@example.com",
        "phone": "9855667788",
        "state": "Rajasthan",
        "city": "Jaipur",
        "department": "Drainage Department",
        "title": "Open uncovered sewer manhole on poorly lit curve",
        "description": "Cast iron lid was stolen or removed 5 days ago. Locals placed a wooden branch as an informal warning, but it remains a severe hazard for night commuters.",
        "location": "Vaishali Nagar, Near Amrapali Circle",
        "status": "In Process",
        "upvotes": 16,
        "days_ago": 2
    },
    {
        "author": "Ananya Deshmukh",
        "email": "ananya.deshmukh@example.com",
        "phone": "9866778899",
        "state": "Maharashtra",
        "city": "Pune",
        "department": "Traffic Management Department",
        "title": "Traffic signals stuck on perpetual blinker at chaotic 4-way crossroad",
        "description": "All 4 signals at the junction have been uncalibrated for 48 hours, creating severe vehicular jams and multiple near-collisions during office hours.",
        "location": "Kothrud, Paud Road Intersection",
        "status": "Reported",
        "upvotes": 9,
        "days_ago": 1
    },
    {
        "author": "Rohan Gupta",
        "email": "rohan.gupta@example.com",
        "phone": "9877889900",
        "state": "Uttar Pradesh",
        "city": "Noida",
        "department": "Electricity Board",
        "title": "Continuous streetlights failure across entire residential sector",
        "description": "Over 12 streetlights across Street 4 and 5 are completely dead for a week. The dark stretch has become unsafe for female commuters returning from the metro station.",
        "location": "Sector 62, Block B Residential Area",
        "status": "In Process",
        "upvotes": 14,
        "days_ago": 4
    },
    {
        "author": "Meera Iyer",
        "email": "meera.iyer@example.com",
        "phone": "9888990011",
        "state": "Tamil Nadu",
        "city": "Chennai",
        "department": "Drainage Department",
        "title": "Severe sewage backflow in stormwater drainage channels",
        "description": "Domestic blackwater has entered the storm drain, causing foul overflow onto shop fronts and breeding swarms of mosquitoes ahead of the monsoon.",
        "location": "T. Nagar, Usman Road North",
        "status": "Reported",
        "upvotes": 11,
        "days_ago": 3
    },
    {
        "author": "Amit Kumar",
        "email": "amit.kumar@example.com",
        "phone": "9899001122",
        "state": "Bihar",
        "city": "Patna",
        "department": "Municipal Waste Management",
        "title": "Unregulated open municipal garbage dumping near public school",
        "description": "Waste collection tractor dumping unsegregated trash directly adjacent to Government High School boundary wall. Urgent intervention required.",
        "location": "Boring Road, Near Chauraha",
        "status": "Reported",
        "upvotes": 8,
        "days_ago": 2
    },
    {
        "author": "Pooja Verma",
        "email": "pooja.verma@example.com",
        "phone": "9812345678",
        "state": "Uttar Pradesh",
        "city": "Lucknow",
        "department": "Public Works Department",
        "title": "Multiple crater-sized potholes formed on main hospital arterial road",
        "description": "Heavy monsoon wash-off created half-meter deep craters. Ambulances ferrying critical patients to Civil Hospital are forced to slow down to a crawl.",
        "location": "Hazratganj to Civil Hospital Connector",
        "status": "In Process",
        "upvotes": 24,
        "days_ago": 5
    },
    {
        "author": "Karthik Reddy",
        "email": "karthik.reddy@example.com",
        "phone": "9823456789",
        "state": "Telangana",
        "city": "Hyderabad",
        "department": "Water Supply Authority",
        "title": "Severely discolored, foul-smelling municipal tap water supply",
        "description": "Tap water supplied this morning is turbid brown with high sediment and sulfur odor. Appears to be mixing with sewer seepage. Unfit for domestic use.",
        "location": "Banjara Hills, Road No. 10",
        "status": "Reported",
        "upvotes": 19,
        "days_ago": 1
    },
    {
        "author": "Divya Joshi",
        "email": "divya.joshi@example.com",
        "phone": "9834567890",
        "state": "Maharashtra",
        "city": "Mumbai",
        "department": "Urban Development Authority",
        "title": "Broken pedestrian footpath tiles and dangerous rebar exposure",
        "description": "Footpath renovation left half-finished 3 months ago. Broken pavers and protruding steel rebar have tripped several senior citizens walking to the railway station.",
        "location": "Andheri East, MV Road near Station",
        "status": "Resolved",
        "upvotes": 13,
        "days_ago": 8
    },
    {
        "author": "Sanjay Rao",
        "email": "sanjay.rao@example.com",
        "phone": "9845678901",
        "state": "Karnataka",
        "city": "Mysore",
        "department": "Municipal Waste Management",
        "title": "Illegal dumping of hotel and poultry slaughter waste in vacant plot",
        "description": "Commercial establishments dumping animal waste late at night in municipal open ground. Severe sanitation emergency threatening local neighborhood health.",
        "location": "Gokulam 3rd Stage, 5th Cross",
        "status": "In Process",
        "upvotes": 10,
        "days_ago": 3
    },
    {
        "author": "Sunita Yadav",
        "email": "sunita.yadav@example.com",
        "phone": "9856789012",
        "state": "Haryana",
        "city": "Gurgaon",
        "department": "Electricity Board",
        "title": "Frequent Phase voltage collapse causing motor burnout",
        "description": "Single-phasing condition recurring every afternoon between 2 PM and 5 PM for the past 10 days. Residential water pumps unable to run.",
        "location": "DLF Phase 3, U Block",
        "status": "Reported",
        "upvotes": 7,
        "days_ago": 2
    },
    {
        "author": "Farhan Ahmed",
        "email": "farhan.ahmed@example.com",
        "phone": "9867890123",
        "state": "Delhi",
        "city": "Delhi",
        "department": "Drainage Department",
        "title": "Stormwater culvert choked with non-biodegradable plastic silt",
        "description": "Culvert entry is 90% blocked by debris and plastic packaging. Even a brief shower will submerge adjoining houses under two feet of stagnant runoff.",
        "location": "Mayur Vihar Phase 1, Pocket 4",
        "status": "In Process",
        "upvotes": 15,
        "days_ago": 4
    },
    {
        "author": "Neha Chawla",
        "email": "neha.chawla@example.com",
        "phone": "9878901234",
        "state": "Punjab",
        "city": "Chandigarh",
        "department": "Traffic Management Department",
        "title": "Missing speed limit boards and broken convex mirror at blind turn",
        "description": "The safety mirror installed at Sector 18 curve has shattered, leaving drivers completely blind to oncoming vehicles.",
        "location": "Sector 18B, Near Inner Market",
        "status": "Resolved",
        "upvotes": 6,
        "days_ago": 9
    },
    {
        "author": "Harpreet Singh",
        "email": "harpreet.singh@example.com",
        "phone": "9889012345",
        "state": "Punjab",
        "city": "Amritsar",
        "department": "Public Works Department",
        "title": "Damaged heritage cobblestone pavement near Golden Temple corridor",
        "description": "Heavy tourist battery rickshaws have broken the decorative stone pavers, creating stumbling traps along the heritage walkway.",
        "location": "Heritage Street, Near Town Hall",
        "status": "Reported",
        "upvotes": 17,
        "days_ago": 3
    },
    {
        "author": "Deepa Kulkarni",
        "email": "deepa.kulkarni@example.com",
        "phone": "9890123456",
        "state": "Maharashtra",
        "city": "Nagpur",
        "department": "Water Supply Authority",
        "title": "Low water pressure in municipal pipeline unable to reach overhead tanks",
        "description": "Water pressure dropped to trickle for 6 consecutive days. Entire block dependent on expensive private water tankers.",
        "location": "Dharampeth, Near Coffee House",
        "status": "Reported",
        "upvotes": 11,
        "days_ago": 2
    },
    {
        "author": "Manish Tiwari",
        "email": "manish.tiwari@example.com",
        "phone": "9801234567",
        "state": "Madhya Pradesh",
        "city": "Indore",
        "department": "Municipal Waste Management",
        "title": "Construction sand and gravel dumped onto municipal tree basins",
        "description": "Private house construction piling up raw gravel over roadside trees, choking roots and restricting public pavement width.",
        "location": "Vijay Nagar, Scheme 54",
        "status": "Resolved",
        "upvotes": 8,
        "days_ago": 7
    },
    {
        "author": "Ritu Agarwal",
        "email": "ritu.agarwal@example.com",
        "phone": "9813572468",
        "state": "Rajasthan",
        "city": "Udaipur",
        "department": "Municipal Corporation",
        "title": "Stray dog pack menace near Government Girls School gate",
        "description": "Pack of aggressive stray dogs gathering near the municipal primary school entrance. Multiple incidents of students being chased this week.",
        "location": "Fatehpura, Near Old Post Office",
        "status": "Reported",
        "upvotes": 14,
        "days_ago": 1
    },
    {
        "author": "Suresh Menon",
        "email": "suresh.menon@example.com",
        "phone": "9824681357",
        "state": "Kerala",
        "city": "Kochi",
        "department": "Public Works Department",
        "title": "Sunken road surface around sewer manhole casing",
        "description": "Asphalt has subsided by 4 inches around the manhole ring, creating a harsh bump that jolts vehicles and causes two-wheelers to wobble.",
        "location": "Kaloor, Near Jawaharlal Nehru Stadium",
        "status": "In Process",
        "upvotes": 9,
        "days_ago": 3
    },
    {
        "author": "Kavita Sen",
        "email": "kavita.sen@example.com",
        "phone": "9835792468",
        "state": "Assam",
        "city": "Guwahati",
        "department": "Drainage Department",
        "title": "Monsoon drain silting causing mud deposition on GS Road",
        "description": "Recent hillside runoff filled roadside gutters with red silt, causing dirty slurry to spread across both lanes during light rainfall.",
        "location": "GS Road, Near Christian Basti",
        "status": "Reported",
        "upvotes": 12,
        "days_ago": 2
    },
    {
        "author": "Rahul Roy",
        "email": "rahul.roy@example.com",
        "phone": "9846801357",
        "state": "Jharkhand",
        "city": "Ranchi",
        "department": "Electricity Board",
        "title": "Tree branches heavily tangled with overhead high-tension line",
        "description": "Overgrown gulmohar branches touching 11kV overhead lines causing sparking whenever breeze blows. Urgent pruning requested before major hazard.",
        "location": "Kanke Road, Near CMPDI Campus",
        "status": "In Process",
        "upvotes": 16,
        "days_ago": 4
    },
    {
        "author": "Swati Mishra",
        "email": "swati.mishra@example.com",
        "phone": "9857912468",
        "state": "Uttar Pradesh",
        "city": "Varanasi",
        "department": "Municipal Waste Management",
        "title": "Garbage bins not emptied along ghat approach lanes",
        "description": "Tourist flow is high but municipal dustbins have not been emptied since Saturday. Debris overflowing onto ancient stone steps.",
        "location": "Assi Ghat Approach Rd, Lanka",
        "status": "Resolved",
        "upvotes": 21,
        "days_ago": 5
    },
    {
        "author": "Deepak Chauhan",
        "email": "deepak.chauhan@example.com",
        "phone": "9868023479",
        "state": "Uttarakhand",
        "city": "Dehradun",
        "department": "Public Works Department",
        "title": "Retaining wall crack widening along hillside road margin",
        "description": "A 10-foot vertical fracture noticed on the stone retaining wall along Rajpur Road curve. If heavy rain occurs, slope may collapse onto lower houses.",
        "location": "Rajpur Road, Near Old Toll Post",
        "status": "In Process",
        "upvotes": 23,
        "days_ago": 3
    },
    {
        "author": "Shalini Bose",
        "email": "shalini.bose@example.com",
        "phone": "9879134580",
        "state": "West Bengal",
        "city": "Siliguri",
        "department": "Traffic Management Department",
        "title": "Broken pedestrian signal button at busy national highway crossing",
        "description": "Pedestrian pelican button not working. Elderly residents and school kids forced to dodge 60km/h highway traffic to cross.",
        "location": "Sevoke Road, Near Planet Mall Junction",
        "status": "Reported",
        "upvotes": 7,
        "days_ago": 1
    },
    {
        "author": "Alok Tripathy",
        "email": "alok.tripathy@example.com",
        "phone": "9880245691",
        "state": "Odisha",
        "city": "Bhubaneswar",
        "department": "Water Supply Authority",
        "title": "Damaged air release valve spraying high pressure water jet",
        "description": "Pipeline air valve broke yesterday afternoon. Constant 20-foot water fountain shooting into air, eroding nearby sidewalk foundation.",
        "location": "Saheed Nagar, Near Durga Mandap",
        "status": "Resolved",
        "upvotes": 15,
        "days_ago": 6
    },
    {
        "author": "Vandana Hegde",
        "email": "vandana.hegde@example.com",
        "phone": "9891356702",
        "state": "Karnataka",
        "city": "Hubli",
        "department": "Municipal Waste Management",
        "title": "Commercial cardboard packaging dumped in municipal storm gutter",
        "description": "Nearby wholesale market vendors dumping packaging cartons directly inside the open rainwater channel, causing acute blockages.",
        "location": "Station Road, Near Cotton Market",
        "status": "Reported",
        "upvotes": 5,
        "days_ago": 2
    },
    {
        "author": "Gaurav Bansal",
        "email": "gaurav.bansal@example.com",
        "phone": "9802467813",
        "state": "Haryana",
        "city": "Faridabad",
        "department": "Electricity Board",
        "title": "Underground power cable joint blast leaving Sector in total darkness",
        "description": "Loud underground blast heard followed by power cutoff in Sector 15. Discom emergency line continuously engaged or unreachable.",
        "location": "Sector 15, Main Market Lane",
        "status": "In Process",
        "upvotes": 18,
        "days_ago": 1
    },
    {
        "author": "Shilpa Rathi",
        "email": "shilpa.rathi@example.com",
        "phone": "9813588924",
        "state": "Rajasthan",
        "city": "Jodhpur",
        "department": "Public Works Department",
        "title": "Unmarked high speed-breaker causing vehicle axle damages",
        "description": "Newly laid asphalt speed breaker lacks yellow diagonal stripes or warning board. At least 5 vehicles scraped their underside in 24 hours.",
        "location": "Ratanada, Circuit House Road",
        "status": "Reported",
        "upvotes": 11,
        "days_ago": 2
    },
    {
        "author": "Nitin Saxena",
        "email": "nitin.saxena@example.com",
        "phone": "9824699035",
        "state": "Uttar Pradesh",
        "city": "Agra",
        "department": "Municipal Corporation",
        "title": "Encroached public green belt turned into illegal unauthorized parking",
        "description": "Designated municipal park buffer green zone illegally fenced off and converted into commercial car parking, damaging planted saplings.",
        "location": "Fatehabad Road, Near Tourist Complex",
        "status": "Reported",
        "upvotes": 8,
        "days_ago": 3
    },
    {
        "author": "Preeti Das",
        "email": "preeti.das@example.com",
        "phone": "9835700146",
        "state": "Chhattisgarh",
        "city": "Raipur",
        "department": "Drainage Department",
        "title": "Broken precast drain slab creating a trap for pedestrian footfalls",
        "description": "Concrete slab cover over drain collapsed under pedestrian weight. A 2-foot hole now exposed directly in front of grocery stores.",
        "location": "Pandri, Cloth Market Main Road",
        "status": "In Process",
        "upvotes": 10,
        "days_ago": 4
    },
    {
        "author": "Tarun Bhatia",
        "email": "tarun.bhatia@example.com",
        "phone": "9846811257",
        "state": "Madhya Pradesh",
        "city": "Bhopal",
        "department": "Water Supply Authority",
        "title": "Public tube-well hand pump hand-lever dismantled and missing",
        "description": "The sole community hand pump catering to low-income residents in Ward 12 has its handle broken off. Residents struggling for basic water.",
        "location": "Shahpura, Sector B Near Community Center",
        "status": "Reported",
        "upvotes": 13,
        "days_ago": 2
    },
    {
        "author": "Jyoti Prasad",
        "email": "jyoti.prasad@example.com",
        "phone": "9857922368",
        "state": "Bihar",
        "city": "Gaya",
        "department": "Municipal Waste Management",
        "title": "Uncollected organic waste decomposing along pilgrimage riverbank",
        "description": "Massive plastic and floral waste accumulated along river steps. Needs emergency municipal sanitation team deployment.",
        "location": "Falgu River Ghat Road, Vishnupad",
        "status": "Resolved",
        "upvotes": 16,
        "days_ago": 7
    },
    {
        "author": "Ashwin Pillai",
        "email": "ashwin.pillai@example.com",
        "phone": "9868033479",
        "state": "Kerala",
        "city": "Thiruvananthapuram",
        "department": "Electricity Board",
        "title": "Streetlight pole rusted through base and swaying in sea breeze",
        "description": "Cast iron pole near coastal bypass has rusted completely through its foundation bolts. Could collapse onto passing traffic at any moment.",
        "location": "Shanghumukham Beach Road, Valiyathura",
        "status": "In Process",
        "upvotes": 14,
        "days_ago": 3
    }
]

def seed():
    with app.app_context():
        added_count = 0
        for item in SEED_DATA:
            # Check or create User
            user = User.query.filter_by(email=item["email"]).first()
            if not user:
                user = User(
                    name=item["author"],
                    email=item["email"],
                    phone=item["phone"],
                    password="password123",
                    city=item["city"],
                    state=item["state"],
                    notifications_enabled=True
                )
                db.session.add(user)
                db.session.commit()

            # Check if this complaint already exists
            existing = Complaint.query.filter_by(title=item["title"], user_id=user.id).first()
            if not existing:
                complaint_time = datetime.utcnow() - timedelta(days=item["days_ago"], hours=random.randint(1, 12))
                complaint = Complaint(
                    title=item["title"],
                    description=item["description"],
                    location=item["location"],
                    state=item["state"],
                    city=item["city"],
                    department=item["department"],
                    status=item["status"],
                    timestamp=complaint_time,
                    user_id=user.id,
                    upvotes=item["upvotes"],
                    downvotes=random.randint(0, 2),
                    thread_count=random.randint(0, 3)
                )
                db.session.add(complaint)
                added_count += 1

        db.session.commit()
        total_complaints = Complaint.query.count()
        total_users = User.query.count()
        print(f"Seeding completed successfully! Added: {added_count} new complaints.")
        print(f"Total Users in DB: {total_users}, Total Complaints in DB: {total_complaints}")

if __name__ == "__main__":
    seed()

