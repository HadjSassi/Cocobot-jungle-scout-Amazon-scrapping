from JungleScout.Jungle.Jungle_Scout import Jungle_Scout
import os
import shutil
import openpyxl
import pandas as pd

download_folder = "/home/keranis/Downloads"
volumeRechercheDuMotClePrincipal = ""
profondeurDuMarche_nbrDeVendeursAvecLeCAVise = ""
nbrDeVendeursAvec75ReviewsEtMoins = ""
nbrDeVendeursAvecUnRatingDe4EtoilesEtMoins = ""
nbrDeVendeursAvecDeLisingNonOptimise = ""
nbrDeVendeursFBM = ""
nbrDeVendeursAvecUneOffreSimilaire = ""
laMargeDeProfit = ""
produitEstConsidereDangereuxOuToxique = ""
produitestDansUneCategorieRestriente = ""
produitDisposeDunBrevet = ""
nbDeVendeursAvec500review = ""
BSRConstant_verifieLaSaisonnalite = ""
constanceDesPrix_siLesPrixSontStablesOuAlaHausse = ""
nombreDeProduitsQuiSontVendusParAmazon = ""
verifierLeCoutParClicSurLeMotClePrincipal = ""
nbreDOffreDeMarquePopulaire = ""
nbrDeVendeursAvecDesVentesEnCroissances = ""
nbrDeVendeursAvecUnTauxDeReviews5EtPlus = ""

targeted_revenue = 8768  # Replace with your targeted revenue
# targeted_revenue = int(input("Donner le chiffre affaire visés"))

# query = input("What would you search ?")
query = "I phone 10"

if __name__ == '__main__':

    # with Jungle_Scout(True) as bot:
    #     bot.Amazon_Jungle_Scout_Extension(query)

    csv_folder = os.path.join(os.getcwd(), "../CSVs")
    # # Supprimer le dossier et tout son contenu
    # shutil.rmtree(csv_folder)
    # # Recréer le dossier vide
    # os.makedirs(csv_folder)
    #
    # # Get the list of files in the download folder, sorted by modification time
    # files = sorted([f for f in os.listdir(download_folder) if os.path.isfile(os.path.join(download_folder, f))],
    #                key=lambda f: os.path.getmtime(os.path.join(download_folder, f)))
    #
    # # Select the last two files
    # last_two_files = files[-2:]
    #
    # # Move the last two files to the current folder
    # for file in last_two_files:
    #     source = os.path.join(download_folder, file)
    #     destination = os.path.join(csv_folder, file)
    #     shutil.move(source, destination)
    #     # print(f"Moved '{file}' to the '../CSVs' folder.")

    files = os.listdir(csv_folder)
    matching_files = [file for file in files if file.startswith("Search Term")]
    if matching_files:
        file_path = os.path.join(csv_folder, matching_files[-1])  # Get the path of the last matching file
        df = pd.read_csv(file_path)
        # Convert the 'Évaluation' column to numeric type
        df['Évaluation'] = pd.to_numeric(df['Évaluation'], errors='coerce')
        df['Avis'] = pd.to_numeric(df['Avis'], errors='coerce')
        df['Ventes mensuelles'] = pd.to_numeric(df['Ventes mensuelles'], errors='coerce')

        profondeurDuMarche_nbrDeVendeursAvecLeCAVise = len(df[df['Revenus mensuels'] == targeted_revenue])
        print("Profondeur du marché (nombre de vendeurs avec un chiffre d'affaires visé):",
              profondeurDuMarche_nbrDeVendeursAvecLeCAVise)
        nbrDeVendeursAvec75ReviewsEtMoins = len(df[df['Avis'] <= 75])
        print("Nombre de vendeurs avec 75 avis ou moins:", nbrDeVendeursAvec75ReviewsEtMoins)
        nbrDeVendeursAvecUnRatingDe4EtoilesEtMoins = len(df[df['Évaluation'] <= 4])
        print("Nombre de vendeurs avec une évaluation de 4 étoiles ou moins:",
              nbrDeVendeursAvecUnRatingDe4EtoilesEtMoins)
        nbrDeVendeursFBM = df["Type de vendeur"].value_counts()["FBM"]
        print("Number of FBA values:", nbrDeVendeursFBM)
        nbDeVendeursAvec500review = len(df[df['Avis'] >= 500])
        print("Nombre de vendeurs avec 500 avis ou plus:", nbDeVendeursAvec500review)
        nombreDeProduitsQuiSontVendusParAmazon = len(df[df['Type de vendeur'] == 'FBA'])
        print("Nombre de produits vendus par Amazon:", nombreDeProduitsQuiSontVendusParAmazon)
        df['Taux_reviews'] = df['Avis'] / df['Ventes mensuelles']
        filtered_df = df[df['Taux_reviews'] >= 0.05]
        nbrDeVendeursAvecUnTauxDeReviews5EtPlus = len(filtered_df)
        print("Nombre de vendeurs avec un taux de reviews de 5% ou plus:", nbrDeVendeursAvecUnTauxDeReviews5EtPlus)

        matching_files = [file for file in files if file.startswith("Keyword")]
        if matching_files:
            file_path = os.path.join(csv_folder, matching_files[-1])  # Get the path of the last matching file
            df = pd.read_csv(file_path, delimiter=',', skiprows=3)
            volumeRechercheDuMotClePrincipal = df.iloc[0, 1]
            print("Volume Recherche Du Mot Cle Principal:", volumeRechercheDuMotClePrincipal)
        else:
            print("Please Contact The administrator")
    else:
        print("Please Contact The administrator ")

    file_path = "rapport.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    # Get the first sheet
    first_sheet = workbook.worksheets[0]
    # Create a new sheet and copy the data from the first sheet
    sheet = workbook.copy_worksheet(first_sheet)
    sheet.title = query
    for row in first_sheet.iter_rows(values_only=True):
        sheet.append(row)
    sheet["E6"] = volumeRechercheDuMotClePrincipal
    sheet["E7"] = profondeurDuMarche_nbrDeVendeursAvecLeCAVise
    sheet["E9"] = nbrDeVendeursAvec75ReviewsEtMoins
    sheet["E10"] = nbrDeVendeursAvecUnRatingDe4EtoilesEtMoins
    sheet["E11"] = nbrDeVendeursAvecDeLisingNonOptimise
    sheet["E12"] = nbrDeVendeursFBM
    sheet["E13"] = nbrDeVendeursAvecUneOffreSimilaire
    sheet["E15"] = laMargeDeProfit
    sheet["E16"] = produitEstConsidereDangereuxOuToxique
    sheet["E17"] = produitestDansUneCategorieRestriente
    sheet["E18"] = produitDisposeDunBrevet
    sheet["E20"] = nbDeVendeursAvec500review
    sheet["E21"] = BSRConstant_verifieLaSaisonnalite
    sheet["E22"] = constanceDesPrix_siLesPrixSontStablesOuAlaHausse
    sheet["E23"] = nombreDeProduitsQuiSontVendusParAmazon
    sheet["E24"] = verifierLeCoutParClicSurLeMotClePrincipal
    sheet["E25"] = nbreDOffreDeMarquePopulaire
    sheet["E26"] = nbrDeVendeursAvecDesVentesEnCroissances
    sheet["E27"] = nbrDeVendeursAvecUnTauxDeReviews5EtPlus

    # Save the changes
    workbook.save(file_path)
