import click

from food_analysis.analysis.api.api_recepts import ReceptAnalysis
from food_analysis.analysis.recepts_files.recepts_files import Recepts

@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', "--name", nargs=1)
@click.argument("ingridients", nargs=-1)
@click.option('-f', "--file", type=click.File('r'))
def get_calories(name, ingridients, file):
    if file is not None:
        dict = get_recept(file)
        name_new = dict["name"]
        ingridients_new = dict["ingridients"]
    else:
        name_new = name
        ingridients_new = []
        for i in ingridients:
            ingridients_new.append(i.replace("_", " "))

    api = ReceptAnalysis()
    calories = api.get_calories(name_new, ingridients_new)
    click.echo(calories)

@cli.command()
@click.option('-n', "--name", nargs=1)
@click.argument("ingridients", nargs=-1)
@click.option('-f', "--file", type=click.File('r'))
def get_analysis(name, ingridients, file):
    if file is not None:
        dict = get_recept(file)
        name_new = dict["name"]
        ingridients_new = dict["ingridients"]
    else:
        name_new = name
        ingridients_new = []
        for i in ingridients:
            ingridients_new.append(i.replace("_", " "))

    api = ReceptAnalysis()
    analysis = api.create_report(name_new, ingridients_new)
    click.echo(analysis)

@cli.command()
@click.argument("dir")
@click.argument("file")
def make_analysis_file(dir, file):
    analysis = Recepts(dir, file)
    click.echo(analysis.write_report())

def get_recept(file):
    recept_name = ""
    recept_ingredients = []
    if file is not None:
        line0 = file.readline().split(': ')
        if (line0[0] == "Name") & (len(line0) == 2):
            recept_name = line0[1]

        line1 = file.readline()
        if line1 == "Ingredients:\n":
            end = True
            while end == True:
                line = file.readline()
                recept_ingredients.append(line)
                if (line == "Description:\n") | (line == ""):
                    end = False

    return {"name": recept_name, "ingridients": recept_ingredients}

if __name__ == '__main__':
    cli()


