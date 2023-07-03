class XpathNotations:
    @classmethod
    def get_date_btn(self) -> str:
        return (
            '//*[@id="site-content"]/div[1]/div[1]/div[2]/div/div/div[1]/div/div/button'
        )

    @classmethod
    def get_btn_year(self):
        return '//*[@id="site-content"]/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/ul/li[5]/button'

    @classmethod
    def get_btn_section(self):
        return (
            '//*[@id="site-content"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/button'
        )

    @classmethod
    def get_section_list(self):
        return '//*[@id="site-content"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/ul/li'

    @classmethod
    def get_section(self, index):
        return f'//*[@id="site-content"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/ul/li[{index}]/label'

    @classmethod
    def get_search_field(self):
        return '//*[@id="searchTextField"]'

    @classmethod
    def get_search_btn(self):
        return '//*[@id="site-content"]/div/div[1]/div[1]/form/div[1]/button/svg'
