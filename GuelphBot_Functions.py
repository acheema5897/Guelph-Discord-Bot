import disnake
def create_embed_list(courses):
    embed_list = []
    for course in courses:
        course_code = course.find_next("span", "text detail-code margin--small text--semibold text--big").text
        course_title = course.find("span", "text detail-title margin--small text--semibold text--big").text
        course_credit = course.find("span", "text detail-hours_html margin--small text--semibold text--big").text
        course_locations = course.find("span", "text detail-location_s_ margin--default").span.text
        try:
            course_terms = course.find("span", "text detail-typically_offered margin--small text--semibold text--big").text
        except AttributeError:
            course_terms = "Unspecified"
        try:
            course_description = course.find("p", "courseblockextra noindent").text
        except AttributeError:
            course_description = ""
        try:
            course_departments = course.find("span", "text detail-department_s_ margin--default").span.text
        except:
            course_departments = "Unspecified"
        # Labs & Lectures
        try:
            course_labs_and_lectures = course.find("span",
                                                   "text detail-inst_method margin--small text--semibold text--big").text
            if ',' in course_labs_and_lectures:
                course_lectures, course_labs = course_labs_and_lectures.split(',')
                course_lectures, course_labs = course_lectures[6], course_labs[6]
            elif "LEC" in course_labs_and_lectures:
                course_lectures = course_labs_and_lectures[6]
                course_labs = "0"
            elif "LAB" in course_labs_and_lectures:
                course_labs = course_labs_and_lectures[6]
                course_lectures = "0"
        except AttributeError:
            course_labs = "0"
            course_lectures = "0"
        # Course Offerings
        try:
            course_offerings = course.find("span", "text detail-offering margin--default").span.text
        except AttributeError:
            course_offerings = ""
        # Restrictions
        try:
            course_restrictions = course.find("span", "text detail-restriction margin--default").span.text
        except AttributeError:
            course_restrictions = "None"
        # Pre-requisites
        try:
            course_prerequisites = course.find("span", "text detail-prerequisite_s_ margin--default").span.text
        except AttributeError:
            course_prerequisites = "None"

        #course_embed = disnake.Embed(title=f"{course_codeZ} {course_title} {course_terms} {course_credit}", description=f"{course_description}")
        course_embed = disnake.Embed(title=f"{course_title}", description=f"{course_description}")
        course_embed.add_field(name="Course Code", value=f"{course_code}")
        course_embed.add_field(name="Terms Offered", value=f"{course_terms}")
        course_embed.add_field(name="Credit", value=f"{course_credit}")
        course_embed.add_field(name="Lectures", value=f"{course_lectures}")
        course_embed.add_field(name="Labs", value=f"{course_labs}")
        course_embed.add_field(name="Restrictions", value=f"{course_restrictions}")
        course_embed.add_field(name="Prerequisites", value=course_prerequisites.replace('*', '\*'))
        course_embed.add_field(name="Departments", value=f"{course_departments}")
        course_embed.add_field(name="Locations", value=f"{course_locations}")
        if (course_offerings != ""):
            course_embed.add_field(name="Offering(s)", value=f"{course_offerings}")
        embed_list.append([course_embed, course_code, course_title])
    return embed_list