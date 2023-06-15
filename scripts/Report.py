import aspose.pdf as ap
import sqlite3 as sql

class ReportPDF:
    def __init__(self):
        super().__init__()
        self.vt=sql.connect("C:/Users/AHMET/Desktop/PythonProje/scripts/Db/user_db.sqlite")
    def Raporla(self,rows):
        try:
            self.document=ap.Document()
            self.page = self.document.pages.add()
            count=0
            for row in rows:
                count=count+1
                text=str(count)+": "
                for parca in row:
                    text=text+str(parca)+" - "
                text_fragment= ap.text.TextFragment(text)
                self.page.paragraphs.add(text_fragment)
                count=count+1
            print("Rapor Hazırlandı.")
            self.document.save("scripts/temp/Rapor.pdf")
            return 1
        except:
            print("Hata Oldu!")
            return -1
    def RaporData(self,kId):
        im=self.vt.cursor()
        im.execute(f"SELECT * FROM SonIslemler WHERE userid={kId}")
        rows=im.fetchall()
        result=self.Raporla(rows)
        return result



