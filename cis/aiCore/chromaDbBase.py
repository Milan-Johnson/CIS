import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=["College of Engineering Kottarakkara has been the leading technical institution in Kerala since it’s venture in 2004. CE Kottarakkara offers B.Tech in Computer Science & Engineering (Artificial Intelligence & Machine learning), B.Tech in Computer Science & Engineering and Electronics & Communication Engineering, reflecting the modern technological advancements through its updated syllabus."],
    metadatas=[{"title": "college"}],
    ids=["id1"]
)
collection.add(
    documents=["A fully automated modern Library & Information Centre(LIC) is on its way to becoming an outstanding learning resource centre catering to the ever growing and uncompromising information and intellectual requirements of the students, faulty, and researchers."],
    metadatas=[{"title": "library"}],
    ids=["id2"]
)
collection.add(
    documents=["Hostel for boys and girls with all amenities have been provided by the college. Both the hostels have spacious rooms and Mess halls. Separate facilities for studying is provided in both the hostels."],
    metadatas=[{"title": "hostel"}],
    ids=["id3"]
)
collection.add(
    documents=["The Labs and Workshops of CEK are well maintained and state of the art ones. They include Computer Lab, Electronics Lab and Electrical Lab. The infrastructure in these labs are adequate enough to prepare the students to deal with modern technologies through regular lab sessions under the supervision of experienced and highly qualified Technical staff and skilled faculties to prepare students for real world scenario."],
    metadatas=[{"title": "lab"}],
    ids=["id4"]
)
collection.add(
    documents=["The organisations which are currently active in the college are REACT, FENESTRA, IEEE, IEDC, NSS and Placement cell. Rising Engineering Association for Computer Science and Engineering (REACT) is a departmental association of Computer Science and Engineering students at college of engineering, Kottarakkara. The association performs various activities such as coordinating and conducting seminar and workshops, arranging training sessions for students etc. A project exhibition was conducted in the year 2014. A departmental library is also arranged at the computer lab for the student’s reference purpose.FENESTRA is the association of the Electronics and Communication students of College of Engineering Kottarakkara. The association aims at improving the technical skills of the students by organizing and conducting different workshops and technical competitions. The Institute of Electrical and Electronics Engineers (IEEE) is a professional association. The IEEE cell in our college aims to provide the oppurtunity to explore new technology for students"],
    metadatas=[{"title": "organisation"}],
    ids=["id5"]
)
collection.add(
    documents=["To pursue knowledge and to develop leadership by quality education and need based interdisciplinary research. "],
    metadatas=[{"title": "mission"}],
    ids=["id6"]
)
collection.add(
    documents=["To impart academic excellence by offering state-of-the-art programmes.To breed knowledge and to utilize cutting-edge research and consultancy, for community development To prop scientific innovation and inculcate entrepreneurial outlook amongst students for sustained growth in society To cultivate additional skills in professional programmes To instill ethical, moral and social responsibilities To impart importance of participation and leadership."],
    metadatas=[{"title": "vision"}],
    ids=["id7"]
)

collection.add(
    documents=["The college have latest infrastructures such as Laboratories, Canteen, Gym, Library, Workshops, Sports facilities, Modernised seminar hall."],
    metadatas=[{"title": "infrastructure"}],
    ids=["id8"]
)
collection.add(
    documents=["Candidates who have passed Higher Secondary Examination, Kerala , or Examination recognized as equivalent thereto, with 50% marks in Mathematics separately, and 50% marks in Mathematics, Physics and Chemistry put together are eligible for admission.The number of student intake CSE is 120 per year, for AI and ML is 60 per year, for ECE is 30 seats per year,In addition to this 2 seats in CS branch is reserved for Tuition Fee Waiver(TFW) Scheme as per AICTE directions (Allotment done by Commissioner for Entrance examinations.All seats(Govt. Fees seats - Fees decided by the Government) filled by the Commissioner for Entrance Examinations"],
    metadatas=[{"title": "admission"}],
    ids=["id9"]
)
collection.add(
    documents=["Various scholarships are available to the students such as eGrantz, MCM, AICTE provided scholarships."],
    metadatas=[{"title": "scholarship"}],
    ids=["id10"]
)
collection.add(
    documents=["The college encourages the students to provide arts so that the students can express there talents and extracurricular skills. Arts day is conducted annually every year by the students. All the students except final years are expected to provide a small sum of money to conduct the program. Everyone can participate in the programs availbale to them. Various solo and group programs are conducted. The students get an opportuninty to express their talents and increase their morale."],
    metadatas=[{"title": "arts"}],
    ids=["id11"]
)
collection.add(
    documents=["The college has great intrest in conducting Sports day celebrations. Sports day is conducted annually by the students.Everyone can participate in a bunch of sports and athletic events. solo and group games are there ,students get the opportunity to show their athletic skills and abilities.this is the ultimate chance for the students to showcase thier skills inn sports. The college supports students to take part in various sports competitions and programs."],
    metadatas=[{"title": "sports"}],
    ids=["id12"]
)
collection.add(
    documents=["The college provides College bus facilities, the students are required to pay a transportation fees annually for the same. The college bus travels upto kollam and picks students enroute. College bus saves a lot of time compared to pricate buses."],
    metadatas=[{"title": "transportation"}],
    ids=["id13"]
)
collection.add(
    documents=["The college provides assistance in placement training. From 3rd year onwards college gives placement guidance and provide classes about how to attend interviews. During campus selection various Companies such  as UST, TCS, Infosys, Wipro, etc are some of the major companies that are recruting students from the college"],
    metadatas=[{"title": "placements"}],
    ids=["id14"]
)
collection.add(
    documents=["The college has been providing really good results in the past few years with the combined  effort of both students and teachers. IN the year 2021 KTU EC 1st rank holder was FEBY who was a CEK product."],
    metadatas=[{"title": "achievement"}],
    ids=["id15"]
)
collection.add(
    documents=["The college has a high-speed wifi campus, students will be able to acces this wifi after they fill in  the wifi request form."],
    metadatas=[{"title": "wifi"}],
    ids=["id16"]
)

results = collection.query(
    query_texts=["wifi of college"],
    n_results=2
)
print(results)