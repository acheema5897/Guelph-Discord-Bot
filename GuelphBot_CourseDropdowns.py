from bs4 import BeautifulSoup
import requests
import disnake
from GuelphBot_Functions import *
class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Add the dropdown to our view object.
        self.add_item(Dropdown_A_to_C())
        self.add_item(Dropdown_E_to_H())
        self.add_item(Dropdown_I_to_N())
        self.add_item(Dropdown_O_to_Z())

class Course_DropdownView(disnake.ui.View):
    def __init__(self, courses):
        super().__init__()
        # Add the dropdown to our view object.
        self.add_item(Course_Dropdown(courses))
        if (len(courses) > 24):
            self.add_item(Course_Dropdown2(courses))
        if (len(courses) > 49):
            self.add_item(Course_Dropdown3(courses))
        if (len(courses) > 74):
            self.add_item(Course_Dropdown4(courses))
        if (len(courses) > 99):
            self.add_item(Course_Dropdown5(courses))

class Course_Dropdown5(disnake.ui.StringSelect):
    def __init__(self, courses):
        self.courses = courses
        options = []
        index = 99
        for course in courses[99:]:
            if (index == 124): break
            options.append(disnake.SelectOption(label=course[1], description=course[2], value=f"{index}"))
            index += 1

        super().__init__(
            placeholder="Select Course",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        await inter.response.edit_message(embed=self.courses[int(self.values[0])][0], view=Course_DropdownView(self.courses))

class Course_Dropdown4(disnake.ui.StringSelect):
    def __init__(self, courses):
        self.courses = courses
        options = []
        index = 74
        for course in courses[74:]:
            if (index == 99): break
            options.append(disnake.SelectOption(label=course[1], description=course[2], value=f"{index}"))
            index += 1

        super().__init__(
            placeholder="Select Course",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        await inter.response.edit_message(embed=self.courses[int(self.values[0])][0], view=Course_DropdownView(self.courses))




class Course_Dropdown3(disnake.ui.StringSelect):
    def __init__(self, courses):
        self.courses = courses
        options = []
        index = 49
        for course in courses[49:]:
            if (index == 74): break
            options.append(disnake.SelectOption(label=course[1], description=course[2], value=f"{index}"))
            index += 1

        super().__init__(
            placeholder="Select Course",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        await inter.response.edit_message(embed=self.courses[int(self.values[0])][0], view=Course_DropdownView(self.courses))



class Course_Dropdown2(disnake.ui.StringSelect):
    def __init__(self, courses):
        self.courses = courses
        options = []
        index = 24
        for course in courses[24:]:
            if (index == 49): break
            options.append(disnake.SelectOption(label=course[1], description=course[2], value=f"{index}"))
            index += 1

        super().__init__(
            placeholder="Select Course",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        await inter.response.edit_message(embed=self.courses[int(self.values[0])][0], view=Course_DropdownView(self.courses))
class Course_Dropdown(disnake.ui.StringSelect):
    def __init__(self, courses):
        self.courses = courses
        options = [disnake.SelectOption(label="Go Back", description="Go back to alphabetical index", emoji='↩️')]
        index = 0
        for course in courses:
            if (index == 24): break
            options.append(disnake.SelectOption(label=course[1], description=course[2], value=f"{index}"))
            index += 1

        super().__init__(
            placeholder="Select Course",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        if (self.values[0] == "Go Back"):
            embed_list = disnake.Embed(title="Guelph Courses",
                                       description="Use the dropdown below to pick an area of study to search for courses.")
            await inter.response.edit_message(embed=embed_list, view=DropdownView())
        else:
            await inter.response.edit_message(embed=self.courses[int(self.values[0])][0], view=Course_DropdownView(self.courses))


class Dropdown_A_to_C(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Go Back", description="Go back to alphabetical index", emoji='↩️'),
            disnake.SelectOption(label="ACCT", description="Accounting"),
            disnake.SelectOption(label="AGR", description="Agriculture"),
            disnake.SelectOption(label="ANSC", description="Animal Science"),
            disnake.SelectOption(label="ANTH", description="Anthropology"),
            disnake.SelectOption(label="ARAB", description="Arabic"),
            disnake.SelectOption(label="ARTH", description="Art History"),
            disnake.SelectOption(label="ASCI", description="Arts and Sciences"),

            disnake.SelectOption(label="BIOC", description="Biochemistry"),
            disnake.SelectOption(label="BIOL", description="Biology"),
            disnake.SelectOption(label="BIOM", description="Biomedical Science"),
            disnake.SelectOption(label="BLCK", description="Black Canadian Studies"),
            disnake.SelectOption(label="BOT", description="Botany"),
            disnake.SelectOption(label="BUS", description="Business"),

            disnake.SelectOption(label="CHEM", description="Chemistry"),
            disnake.SelectOption(label="CHIN", description="Chinese"),
            disnake.SelectOption(label="CLAS", description="Classical Studies"),
            disnake.SelectOption(label="COOP", description="Co-operative Education"),
            disnake.SelectOption(label="CIS", description="Computing and Information Science"),
            disnake.SelectOption(label="CRWR", description="Creative Writing"),
            disnake.SelectOption(label="CROP", description="Crop Science"),
            disnake.SelectOption(label="CTS", description="Culture and Technology Studies")
        ]

        super().__init__(
            placeholder="A to C",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The `self` object refers to the
        # StringSelect object, and the `values` attribute gets a list of the user's
        # selected options. We only want the first one.
        if (self.values[0] == "Go Back"):
            embed_list = disnake.Embed(title="Guelph Courses",
                                       description="Use the dropdown below to pick an area of study to search for courses.")
            await inter.response.edit_message(embed=embed_list, view=DropdownView())
        else:
            url = f"https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/{self.values[0].lower()}/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            courses = soup.find_all("div", "courseblock")
            course_list = create_embed_list(courses)
            intro_embed = disnake.Embed(title="Course Select", description="Use dropdown below to select courses.")
            await inter.response.edit_message(embed=intro_embed, view=Course_DropdownView(course_list))
class Dropdown_E_to_H(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            # E (9 areas) + Go Back option (1) = (10)
            disnake.SelectOption(label="Go Back", description="Go back to alphabetical index", emoji='↩️'),
            disnake.SelectOption(label="ECON", description="Economics"),
            disnake.SelectOption(label="ENGG", description="Engineering"),
            disnake.SelectOption(label="ENGL", description="English"),
            disnake.SelectOption(label="EDRD", description="Environmental Design and Rural Development"),
            disnake.SelectOption(label="ENVM", description="Environmental Management"),
            disnake.SelectOption(label="ENVS", description="Environmental Sciences"),
            disnake.SelectOption(label="EQN", description="Equine"),
            disnake.SelectOption(label="EURO", description="European Studies"),
            disnake.SelectOption(label="XSEN", description="External Courses - Seneca"),
            # F (5)
            disnake.SelectOption(label="FRHD", description="Family Relations and Human Development"),
            disnake.SelectOption(label="FIN", description="Finance"),
            disnake.SelectOption(label="FOOD", description="Food Science"),
            disnake.SelectOption(label="FARE", description="Food, Agricultural and Resource Economics"),
            disnake.SelectOption(label="FREN", description="French Studies"),
            # G (3)
            disnake.SelectOption(label="GEOG", description="Geography"),
            disnake.SelectOption(label="GERM", description="German Studies"),
            disnake.SelectOption(label="GREK", description="Greek Studies"),
            # H (6)
            disnake.SelectOption(label="HIST", description="History"),
            disnake.SelectOption(label="HORT", description="Horticultural Science"),
            disnake.SelectOption(label="HTM", description="Hospitality and Tourism Management"),
            disnake.SelectOption(label="HK", description="Human Kinetics"),
            disnake.SelectOption(label="HROB", description="Human Resources and Organizational Behaviour"),
            disnake.SelectOption(label="HUMN", description="Humanities"),


        ]

        super().__init__(
            placeholder="E to H",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The `self` object refers to the
        # StringSelect object, and the `values` attribute gets a list of the user's
        # selected options. We only want the first one.
        if (self.values[0] == "Go Back"):
            embed_list = disnake.Embed(title="Guelph Courses",
                                       description="Use the dropdown below to pick an area of study to search for courses.")
            await inter.response.edit_message(embed=embed_list, view=DropdownView())
        else:
            await inter.response.defer()
            url = f"https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/{self.values[0].lower()}/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            courses = soup.find_all("div", "courseblock")
            course_list = create_embed_list(courses)
            intro_embed = disnake.Embed(title="Course Select", description="Use dropdown below to select courses.")
            await inter.response.edit_message(embed=intro_embed, view=Course_DropdownView(course_list))

class Dropdown_I_to_N(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            # E (9 areas) + Go Back option (1) = (10)
            disnake.SelectOption(label="Go Back", description="Go back to alphabetical index", emoji='↩️'),
            disnake.SelectOption(label="IES", description="Indigenous Environmental Science"),
            disnake.SelectOption(label="INDG", description="Indigenous Studies"),
            disnake.SelectOption(label="IBIO", description="Integrative Biology"),
            disnake.SelectOption(label="IAEF", description="Interdisciplinary Agriculture, Environment and Food"),
            disnake.SelectOption(label="IPS", description="Interdisciplinary Physical Science"),
            disnake.SelectOption(label="ISS", description="Interdisciplinary Social Science"),
            disnake.SelectOption(label="UNIV", description="Interdisciplinary University"),
            disnake.SelectOption(label="IDEV", description="International Development Studies"),
            disnake.SelectOption(label="ITAL", description="Italian Studies"),
            # J (1)
            disnake.SelectOption(label="JLS", description="Justice and Legal Studies"),
            # L (3)
            disnake.SelectOption(label="LARC", description="Landscape Architecture"),
            disnake.SelectOption(label="LAT", description="Latin"),
            disnake.SelectOption(label="LING", description="Linguistics"),
            # M (7)
            disnake.SelectOption(label="MGMT", description="Management"),
            disnake.SelectOption(label="MCS", description="Marketing and Consumer Studies"),
            disnake.SelectOption(label="MATH", description="Mathematics"),
            disnake.SelectOption(label="MICR", description="Microbiology"),
            disnake.SelectOption(label="MCB", description="Molecular and Cellular Biology"),
            disnake.SelectOption(label="MBG", description="Molecular Biology and Genetics"),
            disnake.SelectOption(label="MUSC", description="Music"),
            # N (3)
            disnake.SelectOption(label="NANO", description="Nanoscience"),
            disnake.SelectOption(label="NEUR", description="Neuroscience"),
            disnake.SelectOption(label="NUTR", description="Nutrition"),
        ]

        super().__init__(
            placeholder="I to N",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The `self` object refers to the
        # StringSelect object, and the `values` attribute gets a list of the user's
        # selected options. We only want the first one.
        if (self.values[0] == "Go Back"):
            embed_list = disnake.Embed(title="Guelph Courses",
                                       description="Use the dropdown below to pick an area of study to search for courses.")
            await inter.response.edit_message(embed=embed_list, view=DropdownView())
        else:
            code = self.values[0].lower()
            if (code == "iaef"):
                code = "ieaf"
            url = f"https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/{code}/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            courses = soup.find_all("div", "courseblock")
            course_list = create_embed_list(courses)
            intro_embed = disnake.Embed(title="Course Select", description="Use dropdown below to select courses.")
            await inter.response.edit_message(embed=intro_embed, view=Course_DropdownView(course_list))


class Dropdown_O_to_Z(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            # O (2 areas) + Go Back option (1) = (3)
            disnake.SelectOption(label="Go Back", description="Go back to alphabetical index", emoji='↩️'),
            disnake.SelectOption(label="ONEH", description="One Health"),
            disnake.SelectOption(label="OAGR", description="Organic Agriculture"),
            # P (8 areas)
            disnake.SelectOption(label="PATH", description="Pathology"),
            disnake.SelectOption(label="PHIL", description="Philosophy"),
            disnake.SelectOption(label="PHYS", description="Physics"),
            disnake.SelectOption(label="PBIO", description="Plant Biology"),
            disnake.SelectOption(label="POLS", description="Political Science"),
            disnake.SelectOption(label="POPM", description="Population Medicine"),
            disnake.SelectOption(label="PORT", description="Portuguese"),
            disnake.SelectOption(label="PSYC", description="Psychology"),
            # R (1 area)
            disnake.SelectOption(label="REAL", description="Real Estate and Housing"),
            # S (7 areas)
            disnake.SelectOption(label="SXGN", description="Sexualities, Genders and Social Change"),
            disnake.SelectOption(label="SOC", description="Sociology"),
            disnake.SelectOption(label="SOAN", description="Sociology and Anthropology"),
            disnake.SelectOption(label="SPAN", description="Spanish and Hispanic Studies"),
            disnake.SelectOption(label="SPMT", description="Sport and Event Management"),
            disnake.SelectOption(label="STAT", description="Statistics"),
            disnake.SelectOption(label="SART", description="Studio Art"),
            # T (2 areas)
            disnake.SelectOption(label="THST", description="Theatre Studies"),
            disnake.SelectOption(label="TOX", description="Toxicology"),
            # V (1 area)
            disnake.SelectOption(label="VETM", description="Veterinary Medicine"),
            # W (1 area)
            disnake.SelectOption(label="WMST", description="Women's Studies"),
            # Z (1 area)
            disnake.SelectOption(label="ZOO", description="Zoology"),
        ]

        super().__init__(
            placeholder="O to Z",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The `self` object refers to the
        # StringSelect object, and the `values` attribute gets a list of the user's
        # selected options. We only want the first one.
        if (self.values[0] == "Go Back"):
            embed_list = disnake.Embed(title="Guelph Courses",
                                       description="Use the dropdown below to pick an area of study to search for courses.")
            await inter.response.edit_message(embed=embed_list, view=DropdownView())
        else:
            code = self.values[0].lower()
            url = f"https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/{code}/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            courses = soup.find_all("div", "courseblock")
            course_list = create_embed_list(courses)
            #await inter.response.edit_message(embed=course_list[0][0], view=Buttons(course_list))
            intro_embed = disnake.Embed(title="Course Select", description="Use dropdown below to select courses.")
            await inter.response.edit_message(embed=intro_embed, view=Course_DropdownView(course_list))
