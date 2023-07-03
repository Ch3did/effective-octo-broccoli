


class XpathNotations:
    
    @classmethod
    def get_categories(self) -> str:
        return '//*[@id="app"]/div[2]/div/header/div[4]/ul/li'
    
    @classmethod
    def get_category_element(self, element):
        return f'//*[@id="app"]/div[2]/div/header/div[4]/ul/li[{element+1}]/a'