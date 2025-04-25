import disnake

class Degree_DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Add the dropdown to our view object.
        self.add_item(Degree_Dropdown())



class Degree_Dropdown(disnake.ui.StringSelect):
    def __init__(self):

        options = [disnake.SelectOption(label="(B.A.Sc.)", description="Bachelor of Applied Science"),
                   disnake.SelectOption(label="(B.A.)", description="Bachelor of Arts"),
                   disnake.SelectOption(label="(B.A.S.)", description="Bachelor of Arts and Sciences"),
                   disnake.SelectOption(label="(B.B.R.M.)", description="Bachelor of Bio-Resource Management Degree"),
                   disnake.SelectOption(label="(B.Comm.)", description="Bachelor of Commerce"),
                   disnake.SelectOption(label="(B.Comp.)", description="Bachelor of Computing"),
                   disnake.SelectOption(label="(B.Eng.)", description="Bachelor of Engineering"),
                   disnake.SelectOption(label="(B.I.E.S.P.)", description="Bachelor of Indigenous Environmental Science and Practice"),
                   disnake.SelectOption(label="(B.L.A.)", description="Bachelor of Landscape Architecture"),
                   disnake.SelectOption(label="(B.O.H.)", description="Bachelor of One Health"),
                   disnake.SelectOption(label="(B.Sc.)", description="Bachelor of Science"),

                   disnake.SelectOption(label="[B.Sc.(Agr.)]", description="Bachelor of Science in Agriculture"),
                   disnake.SelectOption(label="[B.Sc.(Env.)]", description="Bachelor of Science in Environmental Sciences"),
                   disnake.SelectOption(label="Doctor of Veterinary Medicine (D.V.M.)", description="")

                   ]

        super().__init__(
            placeholder="Select Course",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        degree_embed = disnake.Embed(title=f"{self.values}", description="Use the dropdown below.")
        await inter.response.edit_message(embed=degree_embed)