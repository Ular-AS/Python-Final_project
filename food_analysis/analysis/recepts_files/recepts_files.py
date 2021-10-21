import os
from food_analysis.analysis.api.api_recepts import ReceptAnalysis

class Recepts:
    def __init__(self,in_dir,file):
        if not os.path.isdir(in_dir):
            raise ValueError("Directory not found")
        if not os.path.isfile(os.path.join(in_dir, file)):
            raise ValueError("File not found")
        self.in_dir = in_dir
        self.out_dir = os.path.join(self.in_dir, "Analysis")
        self.analysis = ReceptAnalysis()
        self.file = file

    def get_recept(self):
        recept_name = ""
        recept_ingredients = []
        with open(os.path.join(self.in_dir, self.file)) as f:
            line0 = f.readline().split(': ')
            if (line0[0] == "Name") & (len(line0) == 2):
                recept_name = line0[1]
                recept_name = recept_name.replace("\n", "")

            line1 = f.readline()
            if line1 == "Ingredients:\n":
                while True:
                    line = f.readline()
                    line = line.replace("\n", "")
                    if (line == "Description:") | (line == ""):
                        break
                    recept_ingredients.append(line)

        return {"name": recept_name, "ingridients": recept_ingredients}

    def _make_out_dir(self):
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

    def write_report(self):
        self._make_out_dir()
        recept_dict = self.get_recept()
        text = self.analysis.create_report(recept_dict["name"], recept_dict["ingridients"])
        f = open(os.path.join(self.out_dir, self.file), 'w')
        f.write(str(text))
        f.close()
        return "Recipe analysis is formed"
